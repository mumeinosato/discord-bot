import discord
from discord import app_commands
from discord.ext import commands

class tool(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@app_commands.command(name="tool", description="tool一覧を表示します")
async def tool(self, inter: discord.Interaction):
    embed = discord.Embed(title="ツール", description="ツール一覧", color=0x4169e1)
    embed.add_field(name="**天気**", value="全国の天気予報を取得します", inline=False)
    embed.add_field(name="**mcid**", value="Minecraftのプレイヤーを検索します", inline=False)
    await inter.repone.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(tool(bot))
    print("toolを読み込んだよ")        