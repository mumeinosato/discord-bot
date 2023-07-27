import urllib.request
import urllib.parse
import citycheck
import discord
from discord import app_commands
from discord.ext import commands

class weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

api = "https://weather.tsukumijima.net/api/forecast"        

@app_commands.command(name="weather", description="全国の天気予報を取得します")
@app_commands.describe(cid="地域ID")
async def weather(self, inter: discord.Interaction, cid: str):
    params = urllib.parse.urlencode(cid)
    url = api + "?" + params
    data = urllib.request.urlopen(url).read()
    text = data.decode("utf-8")
    embed = discord.Embed(title="ヘルプ", description="すべてスラッシュコマンドに対応する予定です", color=0x4169e1)
    embed.add_field(name="**mcid**", value="Minecraftのプレイヤーを検索します", inline=False)
    await inter.repone.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(weather(bot))
    print("weatherを読み込んだよ") 