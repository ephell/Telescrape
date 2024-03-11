from typing import Awaitable, Callable

from telethon import TelegramClient
from telethon.errors.rpcerrorlist import (
    PhoneCodeEmptyError,
    PhoneCodeExpiredError,
    PhoneCodeHashEmptyError,
    PhoneCodeInvalidError,
    PhoneNumberBannedError,
    PhoneNumberInvalidError,
    PhoneNumberOccupiedError
)


class Client(TelegramClient):

    def __init__(
        self, 
        username: str, 
        phone_number: int, 
        api_id: str, 
        api_hash: str,
        open_code_input_dialog_and_get_input: None | Callable[[], Awaitable[None | str]] = None,
    ):
        self._username = username
        self._phone_number = phone_number
        self._api_id = api_id
        self._api_hash = api_hash
        super().__init__(self._username, self._api_id, self._api_hash)
        self._open_code_input_dialog_and_get_input = open_code_input_dialog_and_get_input

    async def login(self):
        try:
            print(f"Signing in as: {self._username} ... ")

            try:
                await self.connect()
            except OSError:
                print("Failed to connect.")
                return None

            if not await self.is_user_authorized():
                print("User is not authorized. Sending code request ... ")
                code_request = await self.send_code_request(self._phone_number)
                print("Code request sent.")

                if self._open_code_input_dialog_and_get_input is not None:
                    print("Waiting for code from the input dialog ... ")
                    code = await self._open_code_input_dialog_and_get_input()
                else:
                    code = input("Enter the login code you received from Telegram (app/SMS): ")
                print("Received code:", code)

                if code == "":
                    print("Received code is an empty string.")
                    return None
                elif code is not None:
                    await self.sign_in(
                        self._phone_number, 
                        code, 
                        phone_code_hash=code_request.phone_code_hash
                    )
                else:
                    print("Login cancelled.")
                    return None

            print("Signed in successfully!")
            return self
        except Exception as e:
            print(f"An error occured while signing in: {e}.")
            return None

    async def logout(self):
        await self.disconnect()

