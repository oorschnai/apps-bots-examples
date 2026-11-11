import os

from vkbottle.bot import Bot


token = os.environ.get("VK_TOKEN")
if not token:
    raise SystemExit("VK_TOKEN is required")

bot = Bot(token)


@bot.on.message(text="/start")
async def start(_) -> str:
    return "VKBottle bot is running"


if __name__ == "__main__":
    bot.run()
