import asyncio

from telethon import TelegramClient


class LoginHandler:

    def __init__(self, username, phone_number, api_id, api_hash):
        self.username = username
        self.phone_number = phone_number
        self.api_id = api_id
        self.api_hash = api_hash

    async def connect(self):
        print(f"Connecting '{self.username}' ... ")
        client = TelegramClient("session", self.api_id, self.api_hash)
        async with client:
            if not await client.is_user_authorized():
                await client.send_code_request(self.phone_number)
                await client.sign_in(self.phone_number, input())
            print(f"'{self.username}' connected successfully.")
            return client

