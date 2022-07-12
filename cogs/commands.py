import discord
from discord.ext import commands
from dislash import InteractionClient, slash_commands, Option, OptionType

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

def setup(bot):
    print('commandsファイルを読み込んだよ！')
    bot.add_cog(commands(bot))        