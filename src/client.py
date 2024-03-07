from telethon import TelegramClient


class Client:

    def __init__(self, username: str, phone_number: int, api_id: str, api_hash: str):
        self._username = username
        self._phone_number = phone_number
        self._api_id = api_id
        self._api_hash = api_hash
        self._client: TelegramClient = None

    async def __aenter__(self):
        try:
            print(f"Signing in as: {self._username} ... ")
            self._client = TelegramClient(self._username, self._api_id, self._api_hash)
            await self._client.start(self._phone_number)
            print("Signed in successfully!")
            return self._client
        except Exception as e:
            print(f"An error occured while signing in: {e}.")

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._client.disconnect()
        print("Client exited successfully!")
