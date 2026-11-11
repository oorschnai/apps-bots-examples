const { Telegraf } = require("telegraf");

const token = process.env.BOT_TOKEN;
if (!token) {
  throw new Error("BOT_TOKEN is required");
}

const bot = new Telegraf(token);

bot.start((ctx) => ctx.reply("Telegraf bot is running"));

bot.launch().catch((error) => {
  console.error("Telegraf polling stopped", error);
  process.exit(1);
});

process.once("SIGINT", () => bot.stop("SIGINT"));
process.once("SIGTERM", () => bot.stop("SIGTERM"));
