import config
import discord
from discord.ext import commands
from discord.ext.commands.bot import when_mentioned_or
import asyncpg

bot = commands.Bot(
    command_prefix=when_mentioned_or("w!", "w?"),
    activity=discord.Activity(
        type=discord.ActivityType.playing,
        name="w!help | an epic bot"),
    slash_commands=True)


@bot.event
async def on_ready():
    print(f"{bot.user} is now online!")


@bot.command(aliases=["latency"])
async def ping(ctx):
    await ctx.reply(f"🏓Pong! `{round(bot.latency*1000)}ms`")


@bot.command()
async def invite(ctx):
    slash_cmd_invite = "https://discord.com/api/oauth2/authorize?client_id=775601025272905739&permissions=8&scope=bot%20applications.commands"
    non_slash_cmd_invite = "https://discord.com/api/oauth2/authorize?client_id=775601025272905739&permissions=8&scope=bot"
    slash_cmd_link = "https://discord.com/api/oauth2/authorize?client_id=775601025272905739&scope=applications.commands"
    await ctx.reply(f"With slash commands: {slash_cmd_invite} \nWithout slash commands: {non_slash_cmd_invite}\n\nIf you are trying to add slash commands to a server that already has the bot use this link: {slash_cmd_link}")


@bot.command(aliases=["calc"])
async def calculate(ctx, num1, operation, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except:
        return await ctx.reply("That is not a valid equation!")
    if operation == "+":
        return await ctx.reply(num1+num2)
    elif operation == "-":
        return await ctx.reply(num1-num2)
    elif operation == "x" or operation == "*":
        return await ctx.reply(num1*num2)
    elif operation == "/" or operation == ":":
        return await ctx.reply(num1/num2)

bot.pool = asyncpg.create_pool("postgres://lzlgwlpnvwxypo:83e72fcd73a7cabb9bce0e116a905f238449a3c58ec42b8f489e1b2a890bf5c7@ec2-3-230-219-251.compute-1.amazonaws.com:5432/d39e4n8gbkaogr")

bot.load_extension("jishaku")

bot.run(config.token)
