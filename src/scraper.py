import csv
import os
import re
from typing import TYPE_CHECKING, Dict, List

if TYPE_CHECKING:
    from src.client import Client
    from src.gui.main_window.central_widget.scrape_widget.entity_status_widget.entity_status_widget import EntityStatusWidget

from datetime import datetime, timedelta, timezone

from telethon.errors import ChatAdminRequiredError
from telethon.tl.types import (
    Channel,
    ChannelParticipantsAdmins,
    Chat,
    User,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently
)


class Scraper:

    def __init__(self, client: "Client", active_in_last_days: int = 30):
        self._active_in_last_days = active_in_last_days
        self._client = client
        self.scraped_data_dir_path = os.path.join(os.getcwd(), "scraped_data_dir")
        if not os.path.exists(self.scraped_data_dir_path):
            os.mkdir(self.scraped_data_dir_path)

    async def get_scrapable_entities(self) -> List[Channel | Chat]:
        entities = []
        async for dialog in self._client.iter_dialogs(ignore_migrated=True):
            entity = dialog.entity
            if isinstance(entity, Channel) or isinstance(entity, Chat):
                entities.append(entity)
        return entities

    async def scrape_entity(self, entity: Channel | Chat, esw: "EntityStatusWidget" = None):
        try:
            users = await self._get_users_from_entity(entity)
            if users is None:
                if esw is not None:
                    esw.set_status_fail("Cannot scrape users. Reason: group/chat admin privileges are required.")
                return

            users_data = self._extract_users_data(users)
            self._write_users_data_to_csv(users_data, entity.title)
            print(f"Finished scraping '{entity.title}'. Total users scraped: {len(users_data)}.")
            esw.set_status_success(f"Finished scraping. Total users scraped: {len(users_data)}.")
        except Exception as e:
            if esw is not None:
                esw.set_status_fail(f"An unhandled exception occured: {e}.")

    async def _get_users_from_entity(self, entity: Channel | Chat) -> List[User]:
        print(f"Scraping users from: '{entity.title}' ... ")
        try:
            admins = []
            async for participant in self._client.iter_participants(entity, filter=ChannelParticipantsAdmins):
                if isinstance(participant, User):
                    admins.append(participant)

            all_users = []
            async for participant in self._client.iter_participants(entity):
                if (
                    isinstance(participant, User) 
                    and not participant.bot 
                    and not participant.is_self
                    and not participant.deleted
                    and not participant.restricted
                    and not participant.scam
                    and not participant.fake
                ):
                    if (
                        isinstance(participant.status, UserStatusOnline)
                        or isinstance(participant.status, UserStatusRecently)
                        or isinstance(participant.status, UserStatusLastWeek)
                    ):
                        all_users.append(participant)
                    elif isinstance(participant.status, UserStatusOffline):
                        last_online = participant.status.was_online.replace(tzinfo=timezone.utc)
                        day_offset = datetime.now(timezone.utc) - timedelta(days=self._active_in_last_days)
                        if last_online >= day_offset:
                            all_users.append(participant)

        except ChatAdminRequiredError:
            print(
                f"Cannot scrape users from '{entity.title}'. " 
                "Reason: group/chat admin privileges are required."
            )
            return None

        return [user for user in all_users if user not in admins]

    def _extract_users_data(self, users: List[User]) -> List[Dict]:
        users_data = []
        for user in users:
            if user.username:
                username= user.username
            else:
                username= ""
            if user.first_name:
                first_name= user.first_name
            else:
                first_name= ""
            if user.last_name:
                last_name= user.last_name
            else:
                last_name= ""
            name = (first_name + ' ' + last_name).strip()
            users_data.append({
                "id": user.id,
                "access_hash": user.access_hash,
                "name": name,
                "username": username,
            })
        return users_data

    def _write_users_data_to_csv(self, users_data: List[Dict], scraped_entity_title: str):
        if len(users_data) <= 0:
            print(f"Nothing to write to CSV file. Provided data of '{scraped_entity_title}' is empty.")
            return
        
        title_no_illegal_chars = re.sub(r'[<>:"/\\|?*]', '_', scraped_entity_title)
        file_path = os.path.join(self.scraped_data_dir_path, title_no_illegal_chars + ".csv")
        with open(
            file=file_path,
            mode="w", 
            newline="", 
            encoding="utf-8"
        ) as file:
            print(f"Writing '{scraped_entity_title}' user data to CSV ... ")
            writer = csv.writer(file)
            writer.writerow(users_data[0].keys())
            for user in users_data:
                writer.writerow(user.values())
            print(f"Finished writing '{scraped_entity_title}' user data.")
            print(f"File saved to: '{file_path}'.")
