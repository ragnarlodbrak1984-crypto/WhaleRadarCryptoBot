from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import BOT_TOKEN
from whale_report import generate_report
from whale_ranking import get_whale_ranking


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "✅ WhaleRadarCrypto2026Bot запущен!\n"
        "🐋 Система работает.\n\n"
        "Команды:\n"
        "/report - отчёт китов 24 часа\n"
        "/ranking - рейтинг активности китов\n"
        "/id - показать CHAT_ID"
    )


async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        f"Ваш CHAT_ID: {update.effective_chat.id}"
    )


async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = generate_report()

    await update.message.reply_text(
        text
    )


async def ranking(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = get_whale_ranking()

    await update.message.reply_text(
        text
    )


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("id", myid))
    app.add_handler(CommandHandler("report", report))
    app.add_handler(CommandHandler("ranking", ranking))

    print("Бот запущен...")

    app.run_polling()


if __name__ == "__main__":
    main()