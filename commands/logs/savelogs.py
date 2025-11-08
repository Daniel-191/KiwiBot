import os
import io
import discord
from discord.ext import commands
from helpers.responses import success
from datetime import datetime, timezone
from helpers.supabase import supabase

SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET", "logs")

class SaveLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def savelogs(self, ctx): 
        async def f(guild: discord.Guild):
            now = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
            filename = f"audit-log-{guild.name}-{now}.txt".replace(" ", "_")
            lines = []

            async for entry in guild.audit_logs(limit=None, oldest_first=False):
                lines.append(
                    f"[{entry.created_at.astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}] "
                    f"User: {entry.user} | "
                    f"Action: {entry.action.name} | "
                    f"Target: {entry.target} | "
                    f"Reason: {entry.reason or 'None'}"
                )

            if not lines:
                return f" No audit logs found for `{guild.name}`"

            file_content = "\n".join(lines)
            file_bytes = file_content.encode("utf-8")

            # Upload once, after loop
            res = supabase.storage.from_(SUPABASE_BUCKET).upload(filename, file_bytes)
            return f"Uploaded `{len(lines)}` audit log entries as `{filename}` to Supabase for `{guild.name}`"

        msg = await f(ctx.guild)
        await ctx.send(embed=success("Saved!", msg))


async def setup(bot):
    await bot.add_cog(SaveLogs(bot))
