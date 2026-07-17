from telegram import _update, Update
from telegram.ext import ContextTypes

from analyzers.csv_analyzer import CSVAnalyzer
from memory.sessions import get_dataset

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):

    path = get_dataset(update.effective_user.id)

    if path is None:

        await update.message.reply_text("📂 Please upload a CSV first.")

        return

    analyzer = CSVAnalyzer(path)

    analyzer.load_data()

    summary = analyzer.get_summary()

    message = f"""
📊 Dataset Summary

Rows: {summary['rows']}
Columns: {summary['columns']}

Columns:
{", ".join(summary['column_names'])}
"""

    await update.message.reply_text(message)




















