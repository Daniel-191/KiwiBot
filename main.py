import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
PREFIX = os.getenv("PREFIX")

if TOKEN is None:
    raise RuntimeError("DISCORD_BOT_TOKEN not found in environment")

intents = discord.Intents.default()
intents.message_content = True


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        base = os.path.join(os.path.dirname(__file__), "commands", "utility")
        for filename in os.listdir(base):
            if filename.endswith(".py") and not filename.startswith("_"):
                maybe_coro = self.load_extension(f"commands.utility.{filename[:-3]}")
                if hasattr(maybe_coro, "__await__"):
                    await maybe_coro
        base = os.path.join(os.path.dirname(__file__), "commands", "logs")
        for filename in os.listdir(base):
            if filename.endswith(".py") and not filename.startswith("_"):
                maybe_coro = self.load_extension(f"commands.logs.{filename[:-3]}")
                if hasattr(maybe_coro, "__await__"):
                    await maybe_coro



bot = MyBot(command_prefix=PREFIX, intents=discord.Intents.all())


@bot.event
async def on_ready():
    activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = "Kiwi Tasks"
    )
    await bot.change_presence(
        status=discord.Status.online,
        activity=activity
    )
    print(f"Logged in as {bot.user}!")


if __name__ == "__main__":
    bot.run(TOKEN)
