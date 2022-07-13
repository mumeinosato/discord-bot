from pickle import GLOBAL
import discord
from discord.ext import commands
from dislash import InteractionClient, slash_commands, Option, OptionType

GLOBAL_CH_NAME = "mumeinosato-global"

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx): 
        embed = discord.Embed(title="ヘルプ", description="このヘルプコマンドにはプレフィックスを書いていないため、\n実行には全て`mu:コマンド名`とする必要があります。",color=0x4169e1)
    #↑ここのテキストは自分で修正よろしく
        embed.add_field(name="**help**", value="このコマンドです。",inline=False)
        embed.add_field(name="**about**", value="botについてや、botの招待リンク、サポートサーバーを確認できます。",inline=False)
        embed.add_field(name="**newinfo**", value="新着情報を確認します。",inline=False)
        embed.add_field(name="**globalch**", value="「mumeinosato-global」というチャンネルを作成しグローバルチャットに接続します。",inline=False)
        embed.add_field(name="**game**", value="このbotでできるゲーム一覧を表示します。",inline=False)
        embed.add_field(name="**tool**", value="便利ツール一覧を表示します。",inline=False)
        embed.add_field(name="**servermanagement**", value="サーバー運営に役立つコマンド一覧を表示します。", inline=False)
        await ctx.send(embed=embed)#Contextにはいろいろな情報が入っており、そこから様々な関数、情報にアクセスできる。ctx.sendがその一つ

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
        
    
def comanndscog(bot):
    print('commandsファイルを読み込んだよ！')
    bot.add_cog(commands(bot))        