import asyncio
import sys

from qasync import QEventLoop

from src.gui.application.application import Application
from src.gui.main_window.main_window import MainWindow


def main():
    app = Application(sys.argv)
    event_loop = QEventLoop(app)
    asyncio.set_event_loop(event_loop)
    app_close_event = asyncio.Event()
    app.aboutToQuit.connect(app_close_event.set)

    main_window = MainWindow(app)
    main_window.show()

    with event_loop:
        event_loop.run_until_complete(app_close_event.wait())


if __name__ == '__main__':
    main()
