from discord.ext import commands
from helpers.responses import success
import discord
class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botinfo(self, ctx):
        user = self.bot.user
        profile_pic = user.display_avatar.url
        footer = f"Bot ID: {user.id}"
        footer_pic = user.display_avatar.url
        created_at = user.created_at.strftime("%Y-%m-%d %H:%M:%S UTC")
        latency = round(self.bot.latency * 1000)
        users = sum(g.member_count for g in self.bot.guilds)
        fields = [
            ("Bot Name:", user.display_name, True),
            ("Bot Tag:", user.discriminator, True),
            ("Bot ID:", user.id, True),
            ("Created At:", created_at, True),
            ("Latency:", f"{latency}ms", True),
            ("Total Guilds:", len(self.bot.guilds), True),
            ("Total Users:", users, True),
            ("Library:", f"discord.py {discord.__version__}", True)
            ]
        await ctx.send(embed=success("🤖 Bot Information", f"Hello! I'm {user.name}, here's what I know about myself:", fields=fields, icon_url=profile_pic, footer_icon=footer_pic, footer_text=footer))

async def setup(bot):
    await bot.add_cog(BotInfo(bot))
