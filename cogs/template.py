import discord
from discord import app_commands
from discord.ext import commands

class template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(template(bot))
    print("templateを読み込んだよ") 