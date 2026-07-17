from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import BOT_TOKEN
from handlers import start, help_command, handle_document, analyze, stats, clear, report, about
from utils.error_handler import error_handler



def create_bot():
    """Create and run the Telegram bot application."""

    app = Application.builder().token(BOT_TOKEN).build()

    #commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("analyze", analyze))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(CommandHandler("report", report))
    app.add_handler(CommandHandler("about", about))
    app.add_error_handler(error_handler)

    #CSV upload
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document,))


    return app

