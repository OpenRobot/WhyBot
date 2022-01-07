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


def check_all_message(check_for, message):
    for e in message.embeds:
        if any(item and check_for in item for item in (e.title, e.description)):
            return True
    return False

@bot.event
async def on_message(message):
    if message.author.id == 438057969251254293 or message.author.id == 235148962103951360:
        
        if check_all_message("Greninja-Ash appeared", message):
            await message.channel.set_permissions(message.author, read_messages=False)
            await message.reply("ASH NINJA ALERT, ASH NINJA ALERT, ASH NINJA ALERT\nSEND `OMG ASH NINJA` TO CONFIRM YOU ARE READY TO CATCH THE ASH NINJA!!!")
            def check(msg):
                return msg.content == "OMG ASH NINJA" and msg.channel == message.channel             
            msg = await bot.wait_for("message", check=check)
            if msg.content:
                 await message.channel.set_permissions(message.author, read_messages=True)
                 await msg.reply("Done! Unlocked channel for Myuu. Good luck on catching the Ash Ninja!")

        if check_all_message("★", message) and check_all_message("appeared", message):
            await message.channel.set_permissions(message.author, read_messages=False)
            await message.reply("SHINY ALERT, SHINY ALERT, SHINY ALERT\nSEND `OMG SHINY` TO CONFIRM YOU ARE READY TO CATCH THE SHINY!!!")
            def check(msg):
                return msg.content == "OMG SHINY" and msg.channel == message.channel             
            msg = await bot.wait_for("message", check=check)
            if msg.content:
                 await message.channel.set_permissions(message.author, read_messages=True)
                 await msg.reply("Done! Unlocked channel for Myuu. Good luck on catching the shiny!")
    await bot.process_commands(message)
        

@bot.command(aliases=["latency"])
async def ping(ctx):
    await ctx.reply(f"🏓Pong! `{round(bot.latency*1000)}ms`")


@bot.command()
async def invite(ctx):
    slash_cmd_invite = "https://discord.com/api/oauth2/authorize?client_id=775601025272905739&permissions=8&scope=bot%20applications.commands"
    non_slash_cmd_invite = "https://discord.com/api/oauth2/authorize?client_id=775601025272905739&permissions=8&scope=bot"
    slash_cmd_link = "https://discord.com/api/oauth2/authorize?client_id=775601025272905739&scope=applications.commands"
    await ctx.reply(f"With slash commands: {slash_cmd_invite} \nWithout slash commands: {non_slash_cmd_invite}\n\nIf you are trying to add slash commands to a server that already has the bot use this link: {slash_cmd_link}")


@bot.command()
async def credits(ctx):
    ctx.reply("Owner: whyfai, Developer: whyfai, Creator: whyfai. Basically made solo by whyfai.")

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
