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
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently
)


class Scraper:

    def __init__(self, client: "Client", active_in_last_days: int = 0):
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

    async def scrape_entity(self, entity: Channel | Chat, esw: "EntityStatusWidget"):
        try:
            users = await self._get_users_from_entity(entity)
            if users is None:
                esw.set_status_fail("Cannot scrape users. Reason: group/chat admin privileges are required.")
                return

            users_data = self._extract_users_data(users)
            self._write_users_data_to_csv(users_data, entity.title)
            esw.set_status_success(f"Finished scraping. Total users scraped: {len(users_data)}.")
        except Exception as e:
            esw.set_status_fail(f"An unhandled exception occured: {e}.")

    async def _get_users_from_entity(self, entity: Channel | Chat) -> List[User]:
        try:
            admins = []
            async for participant in self._client.iter_participants(entity, filter=ChannelParticipantsAdmins):
                admins.append(participant)

            all_users = []
            async for participant in self._client.iter_participants(entity):
                if (
                    not participant.bot 
                    and not participant.is_self
                    and not participant.deleted
                    and not participant.restricted
                    and not participant.scam
                    and not participant.fake
                ):
                    if self._active_in_last_days <= 0:
                        all_users.append(participant)
                    else:
                        if isinstance(participant.status, UserStatusEmpty):
                            continue

                        if hasattr(participant.status, "was_online"):
                            last_online = participant.status.was_online.replace(tzinfo=timezone.utc)
                            day_offset = datetime.now(timezone.utc) - timedelta(days=self._active_in_last_days)

                        if self._active_in_last_days <= 1:
                            if (
                                isinstance(participant.status, UserStatusOnline)
                                or isinstance(participant.status, UserStatusRecently)
                                or (isinstance(participant.status, UserStatusOffline) and last_online >= day_offset)
                            ):
                                all_users.append(participant)
                        elif self._active_in_last_days <= 7:
                            if (
                                isinstance(participant.status, UserStatusOnline)
                                or isinstance(participant.status, UserStatusRecently)
                                or isinstance(participant.status, UserStatusLastWeek)
                                or (isinstance(participant.status, UserStatusOffline) and last_online >= day_offset)
                            ):
                                all_users.append(participant)
                        else:
                            if (
                                isinstance(participant.status, UserStatusOnline)
                                or isinstance(participant.status, UserStatusRecently)
                                or isinstance(participant.status, UserStatusLastWeek)
                                or isinstance(participant.status, UserStatusLastMonth)
                                or (isinstance(participant.status, UserStatusOffline) and last_online >= day_offset)
                            ):
                                all_users.append(participant)

        except ChatAdminRequiredError:
            return None

        return [user for user in all_users if user not in admins]

    def _extract_users_data(self, users: List[User]) -> List[Dict]:
        users_data = []
        for user in users:
            if user.username:
                username = user.username
            else:
                username = ""

            if user.first_name:
                first_name = user.first_name
            else:
                first_name = ""
            if user.last_name:
                last_name= user.last_name
            else:
                last_name = ""
            name = (first_name + ' ' + last_name).strip()

            if user.phone:
                phone = user.phone
            else:
                phone = ""

            users_data.append({
                "id": user.id,
                "access_hash": user.access_hash,
                "full_name": name,
                "username": username,
                "phone": phone
            })
        return users_data

    def _write_users_data_to_csv(self, users_data: List[Dict], scraped_entity_title: str):
        if len(users_data) <= 0:
            return
        
        title_no_illegal_chars = re.sub(r'[<>:"/\\|?*]', '_', scraped_entity_title)
        file_path = os.path.join(self.scraped_data_dir_path, title_no_illegal_chars + ".csv")
        with open(
            file=file_path,
            mode="w", 
            newline="", 
            encoding="utf-8"
        ) as file:
            writer = csv.writer(file)
            writer.writerow(users_data[0].keys())
            for user in users_data:
                writer.writerow(user.values())
