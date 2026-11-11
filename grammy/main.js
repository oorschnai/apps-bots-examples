const { Bot } = require("grammy");

const token = process.env.BOT_TOKEN;
if (!token) {
  throw new Error("BOT_TOKEN is required");
}

const bot = new Bot(token);

bot.command("start", (ctx) => ctx.reply("grammY bot is running"));
bot.catch((error) => console.error("grammY handler error", error));

bot.start().catch((error) => {
  console.error("grammY polling stopped", error);
  process.exit(1);
});

process.once("SIGINT", () => bot.stop());
process.once("SIGTERM", () => bot.stop());
