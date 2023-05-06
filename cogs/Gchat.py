from pickle import GLOBAL
from typing_extensions import Self
import discord
from discord.ext import commands
from numpy import tile

GLOBAL_CH_NAME = "mumeinosato-global"

class Gchat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name='on_message')
    async def good_reaction(self, message):
            if message.author.bot:
                return
            if message.channel.name == GLOBAL_CH_NAME:                                                          
                print("success")
                await message.delete() # 元のメッセージは削除しておく
                channels = self.bot.get_all_channels()
                global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
                embed = discord.Embed(
                    description=message.content, color=0x00bfff)
                embed.set_author(name=message.author.display_name,                                                                            
                    icon_url=message.author.avatar_url_as(format="png"))
                embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
                    icon_url=message.guild.icon_url_as(format="png"))# Embedインスタンスを生成、投稿者、投稿場所などの設定
                for channel in global_channels:# メッセージを埋め込み形式で転送
                    await channel.send(embed=embed)
        

def Gchat(bot):
    print('Gchatファイルを読み込んだよ！')
    bot.add_cog(Gchat(bot))   