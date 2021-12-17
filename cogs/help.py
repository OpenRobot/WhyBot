from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["commands"])
    async def help(self, ctx, arg):
        if arg is None:
            embed = discord.Embed(title="w!help", description=f"Run `{ctx.prefix}help <category>` to view the commands for that category!\n\nAvailable prefixes: " + ', '.join([f'`{x}`' for x in await self.bot.get_prefix(ctx.message) if "@" not in x])+"\n\u200b", color=discord.Color.from_rgb(231, 244, 244))
            embed.add_field(name="📜 Others", value=f"`{ctx.prefix}help Others`")
            await ctx.reply(embed=embed)
        elif self.bot.get_command(arg):
            command = self.bot.get_command(arg)
            if command.description is None:
                description = "No description."
            else:
                description = command.description
            embed = discord.Embed(title=command, color=discord.Color.from_rgb(231, 244, 244))
            embed.add_field(name="Description:", value=description, inline=False)
            embed.add_field(name="Usage:", value=f"{ctx.prefix}{command}" if not command.usage else f"{ctx.prefix}{command}"+command.usage, inline=False)
            embed.add_field(name="Cog:", value=command.cog_name)
            await ctx.reply(embed=embed)
        elif self.bot.get_cog(arg):
            cog = self.bot.get_cog(arg)
            commands = cog.get_commands()
            embed = discord.Embed(title=cog.qualified_name, color=discord.Color.from_rgb(231, 244, 244))
            for command in commands:
                description = command.description or "No description."
                embed.add_field(name=command, value=description)
            await ctx.reply(embed=embed)
        else:
            return await ctx.send(f"The command/category with the name `{arg}` cannot be found. Please try again.")