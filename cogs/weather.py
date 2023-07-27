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
@app_commands.describe(sid="地域ID")
async def weather(self, inter: discord.Interaction, sid: str):
    cid = citycheck.city(sid)
    if cid != 0:
        params = urllib.parse.urlencode(cid)
        url = api + "?" + params
        data = urllib.request.urlopen(url).read()
        text = data.decode("utf-8")
        embed = discord.Embed(title=text["title"], description=text["publishingOffice"], color=0x4169e1)
        embed.add_field(name="**今日**", value=text["forecasts"][0]["telop"] + "\n 風向:" + text["forecasts"][0]["detail"]["wind"] + "  風量:" + text["forecasts"][0]["detail"]["wave"] , inline=False)
        embed.add_field(name="**明日**", value=text["forecasts"][1]["telop"] + "\n 風向:" + text["forecasts"][1]["detail"]["wind"] + "  風量:" + text["forecasts"][1]["detail"]["wave"] , inline=False)
        await inter.repone.send_message(embed=embed)
    else:
        embed = discord.Embed(title="エラー", description="エラーが発生しました", color=0x4169e1)
        embed.add_field(name="処理できる地域を指定してください", value="[利用可能な都市を調べる](https://raw.githubusercontent.com/mumeinosato/discord-bot/main/cogs/citycheck.py)", inline=False)
        await inter.response.send_message(embed=embed)   

async def setup(bot):
    await bot.add_cog(weather(bot))
    print("weatherを読み込んだよ") 