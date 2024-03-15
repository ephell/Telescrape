import asyncio
import traceback
from typing import Self

from telethon import TelegramClient
from telethon.errors.rpcerrorlist import (
    FloodWaitError,
    PhoneCodeEmptyError,
    PhoneCodeExpiredError,
    PhoneCodeHashEmptyError,
    PhoneCodeInvalidError,
    PhoneNumberBannedError,
    PhoneNumberInvalidError
)

from src.gui.login_widget.login_widget import LoginWidget


class Client(TelegramClient):

    def __init__(
        self, 
        username: str, 
        phone_number: int, 
        api_id: str, 
        api_hash: str,
        login_widget: LoginWidget | None = None
    ):
        self._username = username
        self._phone_number = phone_number
        self._api_id = api_id
        self._api_hash = api_hash
        self._password = None # ToDo: add support. This is 2FA.
        self._login_widget = login_widget
        super().__init__(self._username, self._api_id, self._api_hash)

    async def login(self) -> Self | None:
        if self._login_widget is None:
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
        print(f"Signing in as: {self._username} ... ")
        await self.start(self._phone_number, self._password)
        if await self.get_me() is not None:
            return self
        return None

    async def _login_via_gui(self):
        print("Signing in via GUI ... ")

        self._login_widget.set_status_message(f"Signing in as: '{self._username}' ... ")
        self._login_widget.show()

        try:
            if not self.is_connected():
                await self.connect()

            if await self.is_user_authorized():
                self._login_widget.set_status_image_success()
                self._login_widget.set_status_message(
                    f"'{self._username}' is already authorized. Successfully logged in ... "
                )
                return self

            try:
                self._login_widget.set_status_message(
                    f"'{self._username}' is not authorized. Sending the login code request ... "
                )
                code_request = await self.send_code_request(self._phone_number)
                self._login_widget.set_status_message("Waiting for login code ... ")
            except PhoneNumberInvalidError:
                self._login_widget.set_status_image_fail()
                self._login_widget.set_status_message("Provided phone number is invalid.")
                return None
            except PhoneNumberBannedError:
                self._login_widget.set_status_image_fail()
                self._login_widget.set_status_message("Provided phone number is banned.")
                return None
            except FloodWaitError as e:
                self._login_widget.set_status_image_fail()
                self._login_widget.set_status_message(
                    "Too many login attempts. "
                    f"Try again in {e.seconds // 60} minutes and {e.seconds % 60} seconds."
                )
                return None

            while True:
                code = await self._login_widget.open_login_code_input_dialog_and_get_input()
                if code == "":
                    await self._login_widget.open_error_message_box("Login code field cannot be empty.")
                elif code is not None:
                    try:
                        await self.sign_in(
                            self._phone_number, 
                            code, 
                            phone_code_hash=code_request.phone_code_hash
                        )
                        if await self.get_me() is not None:
                            self._login_widget.set_status_image_success()
                            self._login_widget.set_status_message("Successfully logged in!")
                            return self
                        return None
                    except (
                        PhoneCodeEmptyError,
                        PhoneCodeExpiredError,
                        PhoneCodeHashEmptyError,
                        PhoneCodeInvalidError
                    ):
                        await self._login_widget.open_error_message_box("Invalid login code.")
                else:
                    self._login_widget.set_status_image_fail()
                    self._login_widget.set_status_message("Login cancelled.")
                    return None

        except Exception as e:
            self._login_widget.set_status_image_fail()
            self._login_widget.set_status_message(f"An unhandled exception occured while logging in.")
            print(f"An unhandled error occured in '{self.login.__name__}': {e}.")
            traceback.print_exc()
            return None


if __name__ == "__main__":
    import asyncio

    from client import Client
    from scraper import Scraper

    async def main():
        client = Client(
            "Raska Good",
            37060751782,
            "14112344",
            "90d2a30e6a391fee8c99f38476d4bf46",
        )
        await client.login()
        # await asyncio.sleep(1)
        # scraper = Scraper(client)
        # await scraper.scrape()
        await client.logout()

    asyncio.run(main())
