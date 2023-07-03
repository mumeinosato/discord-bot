import discord
from discord import app_commands
from discord.ext import commands

class data(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ##@app_commands.command(name="serverinfo", description="サーバーの情報を表示します")
    ##async def serverinfo(self, inter: discord.Integration)
    ##    guild = inter.
    ##    await inter.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(data(bot))
    print("dataを読み込んだよ")