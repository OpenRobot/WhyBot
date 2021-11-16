import config
import discord
from discord.ext import commands
from discord.ext.commands.bot import when_mentioned_or

bot = commands.Bot(command_prefix=when_mentioned_or("w!", "w?"), activity=discord.Activity(type=discord.ActivityType.playing, name="w!help | an epic bot"), slash_commands=True)

@bot.command(aliases=["latency"])
async def ping(ctx):
    await ctx.reply(f"🏓Pong! `{round(bot.latency*1000)}ms`")

bot.load_extension("jishaku")

bot.run(config.token)