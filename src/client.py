from typing import Awaitable, Callable, Self

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
        self._password = None # ToDo: add support. This is 2FA.
        super().__init__(self._username, self._api_id, self._api_hash)
        self._open_login_code_input_dialog_and_get_input = open_login_code_input_dialog_and_get_input

    async def login(self) -> Self | None:
        print(f"Signing in as: {self._username} ... ")
        if self._open_login_code_input_dialog_and_get_input is None:
            login_method = self._login_via_terminal
        else:
            login_method = self._login_via_gui 

        if await login_method() is not None:
            return self
        return None
            
    async def logout(self):
        await self.disconnect()

    async def _login_via_terminal(self):
        print("Signing in via terminal ... ")
        await self.start(self._phone_number, self._password)
        if await self.get_me() is not None:
            return self
        return None

    async def _login_via_gui(self):
        print("Signing in via GUI ... ")
        try:
            try:
                if not self.is_connected():
                    await self.connect()
            except Exception as e:
                print(f"Connecting to Telegram failed: {e}.")
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
                code = await self._open_login_code_input_dialog_and_get_input()

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
                        return None
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
            print(f"An unhandled error occured in '{self.login.__name__}': {e}.")
            return None

    async def logout(self):
        await self.disconnect()

