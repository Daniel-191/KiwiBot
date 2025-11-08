from discord.ext import commands
from helpers.responses import success
class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        id = guild.id
        icon = guild.icon.url if guild.icon else None
        name = guild.name
        description = guild.description
        owner = guild.owner
        members = guild.member_count
        channels = len(guild.channels)
        categories = len(guild.categories)
        roles = len(guild.roles)
        rules = guild.rules_channel
        emojis = len(guild.emojis)
        threads = len(guild.threads)
        voice_channels = len(guild.voice_channels)
        vanity_url = guild.vanity_url
        verification_level = guild.verification_level
        created_at = guild.created_at.strftime("%Y-%m-%d %H:%M:%S UTC")

        fields = [
            ("Server ID:", id, True),
            ("Server Name:", name, True),
            ("Server Description:", description, True),
            ("Server Owner:", owner, True),
            ("Rules Channel:", rules, True),
            ("Verification Level:", verification_level, True),
            ("Members Count:", members, True),
            ("Categories Count:", categories, True),
            ("Channels Count:", channels, True),
            ("Voice Channels Count:", voice_channels, True),
            ("Threads Count:", threads, True),
            ("Roles Count:", roles, True),
            ("Emojis Count:", emojis, True),
            ("Vanity Url:", vanity_url, True),
            ("Created At:", created_at, True)

        ]
        footer = f"Server ID: {id}"

        await ctx.send(embed=success("🏠 Guild Information", f"Hello! I'm {self.bot.user.name}, here's what I know about this guild:", fields=fields, icon_url=icon, footer_icon=icon, footer_text=footer))

async def setup(bot):
    await bot.add_cog(ServerInfo(bot))
