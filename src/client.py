from typing import Awaitable, Callable

from telethon import TelegramClient
from telethon.errors.rpcerrorlist import (
    PhoneCodeEmptyError,
    PhoneCodeExpiredError,
    PhoneCodeHashEmptyError,
    PhoneCodeInvalidError,
    PhoneNumberBannedError,
    PhoneNumberInvalidError
)


class Client(TelegramClient):

    def __init__(
        self, 
        username: str, 
        phone_number: int, 
        api_id: str, 
        api_hash: str,
        open_login_code_input_dialog_and_get_input: None | Callable[[], Awaitable[None | str]] = None,
    ):
        self._username = username
        self._phone_number = phone_number
        self._api_id = api_id
        self._api_hash = api_hash
        super().__init__(self._username, self._api_id, self._api_hash)
        self._open_login_code_input_dialog_and_get_input = open_login_code_input_dialog_and_get_input

    async def login(self):
        try:
            print(f"Signing in as: {self._username} ... ")

            try:
                await self.connect()
            except OSError:
                print("Failed to connect.")
                return None

            if await self.is_user_authorized():
                print("User is already authorized. Successfully logged in!")
                return self

            try:
                print("User is not authorized. Sending the login code request ... ")
                code_request = await self.send_code_request(self._phone_number)
                print("Code request sent.")
            except PhoneNumberInvalidError:
                # ToDo: open error message box.
                print("Provided phone number is invalid.")
                return None
            except PhoneNumberBannedError:
                # ToDo: open error message box.
                print("Provided phone number is banned.")
                return None

            while True:
                if self._open_login_code_input_dialog_and_get_input is not None:
                    code = await self._open_login_code_input_dialog_and_get_input()
                else:
                    code = input("Enter the login code you received from Telegram (app/SMS): ")

                if code == "":
                    # ToDo: open error message box.
                    print("Received code is an empty string.")
                    continue
                elif code is not None:
                    try:
                        await self.sign_in(
                            self._phone_number, 
                            code, 
                            phone_code_hash=code_request.phone_code_hash
                        )
                        if await self.get_me() is not None:
                            print("Logged in successfully!")
                        return self
                    except (
                        PhoneCodeEmptyError,
                        PhoneCodeExpiredError,
                        PhoneCodeHashEmptyError,
                        PhoneCodeInvalidError
                    ):
                        print("Invalid login code.")
                else:
                    print("Login cancelled.")
                    return None

        except Exception as e:
            print(f"An error occured while signing in: {e}.")
            return None

    async def logout(self):
        await self.disconnect()

