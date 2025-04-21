import discord
from discord.ext import commands

# Bot Configuration
BOT_PREFIX = "!"
BOT_TOKEN = "YOUR_BOT_TOKEN"
MUTED_ROLE_NAME = "Muted"

# Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Bot Initialization
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

# ---------------- Events ----------------

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    await bot.change_presence(activity=discord.Game(name="Moderating"))

# ---------------- Utility Commands ----------------

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(name="clear", aliases=["purge"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    try:
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{amount} messages cleared.", delete_after=5)
    except discord.Forbidden:
        await ctx.send("I do not have permission to manage messages.")
    except discord.HTTPException:
        await ctx.send("Clear failed.")
    except commands.errors.MissingRequiredArgument:
        await ctx.send("Please specify an amount of messages to clear.")

@bot.command(name="serverinfo")
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=guild.name, description="Server Information", color=discord.Color.blue())
    embed.add_field(name="Owner", value=guild.owner.mention, inline=False)
    embed.add_field(name="Member Count", value=guild.member_count, inline=False)
    embed.add_field(name="Creation Date", value=guild.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
    embed.set_thumbnail(url=guild.icon.url)
    await ctx.send(embed=embed)

# ---------------- Moderation Commands ----------------

@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked. Reason: {reason}")
    except discord.Forbidden:
        await ctx.send("I do not have permission to kick this member.")
    except discord.HTTPException:
        await ctx.send("Kick failed.")

@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member} has been banned. Reason: {reason}")
    except discord.Forbidden:
        await ctx.send("I do not have permission to kick this member.")
    except discord.HTTPException:
        await ctx.send("Ban failed.")

@bot.command(name="unban")
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.name}#{user.discriminator}")
            return

    await ctx.send(f"Member {member} not found in ban list.")

@bot.command(name="mute")
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason="No reason provided"):
    muted_role = discord.utils.get(ctx.guild.roles, name=MUTED_ROLE_NAME)

    if not muted_role:
        await ctx.send(f"Muted role not found. Please create a role named '{MUTED_ROLE_NAME}'.")
        return

    try:
        await member.add_role(muted_role, reason=reason)
        await ctx.send(f"{member} has been muted. Reason: {reason}")
    except discord.Forbidden:
        await ctx.send("I do not have permission to manage roles.")
    except discord.HTTPException:
        await ctx.send("Mute failed.")

@bot.command(name="unmute")
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member, *, reason="No reason provided"):
    muted_role = discord.utils.get(ctx.guild.roles, name=MUTED_ROLE_NAME)

    if not muted_role:
        await ctx.send("Muted role not found.")
        return

    try:
        await member.remove_role(muted_role, reason=reason)
        await ctx.send(f"{member} has been unmuted. Reason: {reason}")
    except discord.Forbidden:
        await ctx.send("I do not have permission to manage roles.")
    except discord.HTTPException:
        await ctx.send("Unmute failed.")

# ---------------- Run the Bot ----------------

async def main():
    await bot.start(BOT_TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
