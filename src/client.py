import asyncio
import traceback
from typing import TYPE_CHECKING, Optional, Self

if TYPE_CHECKING:
    from src.gui.main_window.main_window import MainWindow
    from src.gui.main_window.central_widget.overlay_widget.overlay_widget import OverlayWidget

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


class Client(TelegramClient):

    def __init__(
        self, 
        username: str, 
        phone_number: int, 
        api_id: str, 
        api_hash: str,
        main_window: Optional["MainWindow"] = None
    ):
        self._username = username
        self._phone_number = phone_number
        self._api_id = api_id
        self._api_hash = api_hash
        self._password = None # ToDo: add support. This is 2FA.
        self._main_window = main_window
        super().__init__(self._username, self._api_id, self._api_hash)

    async def login(self) -> Self | None:
        if self._main_window is None:
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

        login_overlay: OverlayWidget = self._main_window.get_overlay_widget()
        login_overlay.set_message(f"Signing in as: '{self._username}' ... ")
        login_overlay.set_hidden(False)

        try:
            if not self.is_connected():
                await self.connect()

            if await self.is_user_authorized():
                print("Logged in successfullly!")
                return self

            try:
                login_overlay.set_message(
                    f"'{self._username}' is not authorized. Sending the login code request ... "
                )
                code_request = await self.send_code_request(self._phone_number)
                login_overlay.set_message("Waiting for login code ... ")
            except PhoneNumberInvalidError:
                login_overlay.set_image_fail()
                login_overlay.set_message("Provided phone number is invalid.")
                return None
            except PhoneNumberBannedError:
                login_overlay.set_image_fail()
                login_overlay.set_message("Provided phone number is banned.")
                return None
            except FloodWaitError as e:
                login_overlay.set_image_fail()
                login_overlay.set_message(
                    "Too many login attempts. "
                    f"Try again in {e.seconds // 60} minutes and {e.seconds % 60} seconds."
                )
                return None

            while True:
                code = await login_overlay.open_login_code_input_dialog_and_get_input()
                if code == "":
                    await login_overlay.open_error_message_box("Login code field cannot be empty.")
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
                        await login_overlay.open_error_message_box("Invalid login code.")
                else:
                    login_overlay.set_image_fail()
                    login_overlay.set_message("Login cancelled.")
                    return None

        except Exception as e:
            login_overlay.set_image_fail()
            login_overlay.set_message(f"An unhandled exception occured while logging in.")
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
