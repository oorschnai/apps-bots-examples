import asyncio
import logging
import os

from maxapi import Bot, Dispatcher
from maxapi.types import BotStarted, Command, MessageCreated


token = os.environ.get("BOT_TOKEN")
if not token:
    raise SystemExit("BOT_TOKEN is required")

bot = Bot(token)
dispatcher = Dispatcher()


@dispatcher.bot_started()
async def bot_started(event: BotStarted) -> None:
    await event.bot.send_message(
        chat_id=event.chat_id,
        text="maxapi bot is running. Send /start",
    )


@dispatcher.message_created(Command("start"))
async def start(event: MessageCreated) -> None:
    await event.message.answer("maxapi bot is running")


async def main() -> None:
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
