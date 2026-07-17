from bot import create_bot
from utils.logger import Logger

import os


def main():

    Logger.startup()

    if os.path.exists("data/uploads"):
        Logger.success("Upload directory ready")
    else:
        Logger.warning("Upload directory missing")

    if os.path.exists("reports"):
        Logger.success("Reports directory ready")
    else:
        Logger.warning("Reports directory missing")

    Logger.success("Telegram Bot Connected")

    Logger.line()
    Logger.info("Bot is listening for messages...")
    Logger.line()

    app = create_bot()

    app.run_polling()


if __name__ == "__main__":
    main()
























