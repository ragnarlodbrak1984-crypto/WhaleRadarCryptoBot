import asyncio
from telegram import Bot
from config import BOT_TOKEN, CHAT_ID


async def whale_test(bot):
    while True:
        await bot.send_message(
            chat_id=CHAT_ID,
            text="🐋 Whale Radar тест\n✅ Автоматические сообщения работают!"
        )

        await asyncio.sleep(60)


async def main():
    bot = Bot(BOT_TOKEN)
    await whale_test(bot)


if __name__ == "__main__":
    asyncio.run(main())