from discord.ext import commands
from helpers.responses import success

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(embed=success("Pong!", f"Latency: {latency}ms"))

async def setup(bot):
    await bot.add_cog(Ping(bot))
