from discord import Embed

def success(title, desc, fields=None, icon_url=None, footer_user=None, footer_text=None, footer_icon=None):
    embed = Embed(title=title, description=desc, colour=0x05DF72)

    if fields:
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

    if icon_url:
        embed.set_thumbnail(url=icon_url)

    # Custom footer has priority
    if footer_text:
        embed.set_footer(text=footer_text, icon_url=footer_icon)
    elif footer_user:
        embed.set_footer(text=f"Requested by {footer_user.display_name}", icon_url=footer_user.display_avatar.url)

    return embed


def failure(title, desc, fields=None, icon_url=None, footer_user=None, footer_text=None, footer_icon=None):
    embed = Embed(title=title, description=desc, colour=0xE7180B)

    if fields:
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

    if icon_url:
        embed.set_thumbnail(url=icon_url)

    if footer_text:
        embed.set_footer(text=footer_text, icon_url=footer_icon)
    elif footer_user:
        embed.set_footer(text=f"Requested by {footer_user.display_name}", icon_url=footer_user.display_avatar.url)

    return embed
