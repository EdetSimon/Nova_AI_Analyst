import traceback
from telegram import Update
from telegram.ext import ContextTypes


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Log unexpected errors and notify the user."""

    print("\n" + "=" * 60)
    print("❌ UNEXPECTED ERROR")
    print("=" * 60)

    traceback.print_exception(
        type(context.error),
        context.error,
        context.error.__traceback__
    )

    print("=" * 60)

    if isinstance(update, Update) and update.effective_message:
        await update.effective_message.reply_text(
            "⚠ An unexpected error occurred.\n\n"
            "Please try again or upload another dataset."
        )