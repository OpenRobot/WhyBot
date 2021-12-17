import config
import discord
from discord.ext import commands
from discord.ext.commands.bot import when_mentioned_or
import asyncpg

bot = commands.Bot(command_prefix=when_mentioned_or("w!", "w?"), activity=discord.Activity(type=discord.ActivityType.playing, name="w!help | an epic bot"), slash_commands=True)

@bot.command(aliases=["latency"])
async def ping(ctx):
    await ctx.reply(f"🏓Pong! `{round(bot.latency*1000)}ms`")

@bot.command()
async def invite(ctx):
    await ctx.reply("With slash commands: https://discord.com/api/oauth2/authorize?client_id=775601025272905739&permissions=8&scope=bot%20applications.commands \nWithout slash commands: https://discord.com/api/oauth2/authorize?client_id=775601025272905739&permissions=8&scope=bot\n\nIf you are trying to add slash commands to a server that already has the bot use this link: https://discord.com/api/oauth2/authorize?client_id=775601025272905739&scope=applications.commands")

bot.pool = asyncpg.create_pool("postgres://lzlgwlpnvwxypo:83e72fcd73a7cabb9bce0e116a905f238449a3c58ec42b8f489e1b2a890bf5c7@ec2-3-230-219-251.compute-1.amazonaws.com:5432/d39e4n8gbkaogr")

bot.load_extension("jishaku")

bot.run(config.token)