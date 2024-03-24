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

    def __init__(self, client: "Client"):
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
                esw.set_status_fail("Cannot scrape users. Reason: group/chat/channel admin privileges are required.")
                return

            users_data = self._extract_users_data(users)
            self._write_users_data_to_csv(users_data, entity.title)
            esw.set_status_success(f"Finished scraping. Total users scraped: {len(users_data)}.")
        except Exception as e:
            esw.set_status_fail(f"An unhandled exception occured: {e}.")

    async def _get_users_from_entity(
            self, 
            entity: Channel | Chat,
            user_active_in_past_days: int = 0, # 0 = regardless of activity.
            exclude_admins: bool = True,
            exclude_bots: bool = True,
            exclude_deleted_users: bool = True,
            exclude_restricted_users: bool = True,
            exclude_scam_flagged_users: bool = True,
            exclude_fake_flagged_users: bool = True
        ) -> List[User]:
        try:
            all_participants = [p async for p in self._client.iter_participants(entity)]
            if exclude_admins:
                admin_participants = [
                    p async for p in 
                    self._client.iter_participants(entity, filter=ChannelParticipantsAdmins)
                ]
                all_participants = [p for p in all_participants if p not in admin_participants]
        except ChatAdminRequiredError:
            return None

        all_users = []
        for participant in all_participants:
            participant: User = participant
            if (
                (exclude_bots and participant.bot)
                or (exclude_deleted_users and participant.deleted)
                or (exclude_restricted_users and participant.restricted)
                or (exclude_scam_flagged_users and participant.scam)
                or (exclude_fake_flagged_users and participant.fake)
            ):
                continue

            if user_active_in_past_days <= 0:
                all_users.append(participant)
            else:
                if isinstance(participant.status, UserStatusEmpty):
                    continue

                if isinstance(participant.status, UserStatusOffline):
                    last_online = participant.status.was_online.replace(tzinfo=timezone.utc)
                    day_offset = datetime.now(timezone.utc) - timedelta(days=user_active_in_past_days)
                    if last_online >= day_offset:
                        all_users.append(participant)
                else:
                    activity_statuses = set()
                    if user_active_in_past_days <= 1:
                        activity_statuses.add(UserStatusOnline)
                        activity_statuses.add(UserStatusRecently)
                    if user_active_in_past_days >= 6:
                        activity_statuses.add(UserStatusLastWeek)
                        activity_statuses.add(UserStatusLastMonth)
                    if participant.status in activity_statuses:
                        all_users.append(participant)

        return all_users

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
                phone = "Hidden"

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
