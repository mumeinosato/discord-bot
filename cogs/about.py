import discord
from discord import app_commands
from discord.ext import commands

test_guilds = [989133350784618536, 711554285074382900]

class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="helpを表示します")
    async def help(self, inter):
        embed = discord.Embed(title="ヘルプ", description="このヘルプコマンドにはプレフィックスを書いていないため、\n実行には全て`mu:コマンド名`とする必要があります。", color=0x4169e1)
        # ここに追加のコードが続く
        embed.add_field(name="**help**", value="このコマンドです。", inline=False)
        embed.add_field(name="**about**", value="botについてや、botの招待リンク、サポートサーバーを確認できます。", inline=False)
        embed.add_field(name="**newinfo**", value="新着情報を確認します。", inline=False)
        embed.add_field(name="**globalch**", value="「mumeinosato-global」というチャンネルを作成しグローバルチャットに接続します。", inline=False)
        embed.add_field(name="**game**", value="このbotでできるゲーム一覧を表示します。", inline=False)
        embed.add_field(name="**tool**", value="便利ツール一覧を表示します。", inline=False)
        embed.add_field(name="**servermanagement**", value="サーバー運営に役立つコマンド一覧を表示します。", inline=False)
        await inter.send(embed=embed)

async def setup(bot):
    await bot.add_cog(about(bot))
    print("aboutを読み込んだよ")