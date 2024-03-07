import asyncio

from telethon import TelegramClient

from scraper import Scraper


class Client:

    def __init__(self, username: str, phone_number: int, api_id: str, api_hash: str):
        self.username = username
        self.phone_number = phone_number
        self.api_id = api_id
        self.api_hash = api_hash
        self.client: TelegramClient = None

    async def __aenter__(self):
        print(f"Connecting '{self.username}' ... ")
        self.client = TelegramClient("session", self.api_id, self.api_hash)
        await self.client.start()
        if not await self.client.is_user_authorized():
            await self.client.send_code_request(self.phone_number)
            await self.client.sign_in(self.phone_number, input())
        print(f"'{self.username}' connected successfully.")
        return self.client

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.disconnect()
        print(f"'{self.username}' disconnected successfully.")

