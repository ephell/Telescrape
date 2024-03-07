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
        try:
            print(f"Signing in as: {self.username} ... ")
            self.client = TelegramClient("session", self.api_id, self.api_hash)
            await self.client.start(self.phone_number)
            print("Signed in successfully!")
            return self.client
        except Exception as e:
            print(f"An error occured while signing in: {e}.")

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.disconnect()
        print("Client exited successfully!")

