import discord
from discord import app_commands
from discord.ext import commands

test_guilds = [989133350784618536, 711554285074382900]

class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="helpを表示します")
    async def help(self, inter: discord.Interaction):
        embed = discord.Embed(title="ヘルプ", description="すべてスラッシュコマンドに対応する予定です", color=0x4169e1)
        embed.add_field(name="**help**", value="このコマンドです", inline=False)
        embed.add_field(name="**about**", value="botについてや、botの招待リンク、サポートサーバーを確認できます", inline=False)
        embed.add_field(name="**globalch**", value="「mumeinosato-global」というチャンネルを作成しグローバルチャットに接続します", inline=False)
        embed.add_field(name="**game**", value="このbotでできるゲーム一覧", inline=False)
        embed.add_field(name="**tool**", value="便利ツール一覧", inline=False)
        embed.add_field(name="**admin**", value="サーバー管理者のみ実行可能", inline=False)
        await inter.response.send_message(embed=embed)

    @app_commands.command(name="about", description="このbotについて")
    async def about(self, inter: discord.Integration):
        embed = discord.Embed(title="このBOTについて", description="コードの書き直し中です", color=0x4169e1)
        embed.add_field(name="作成者", value="Mumeinosato") 
        embed.add_field(name="招待リンク", value="[ここをクリック](https://discord.com/api/oauth2/authorize?client_id=729668738877620255&permissions=8&scope=bot%20applications.commands)", inline=False) 
        embed.add_field(name="サーバー数", value=f"{len(self.bot.guilds)}")
        embed.add_field(name="メンバー数", value=f"{len(self.bot.users)}")
        await inter.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(about(bot))
    print("aboutを読み込んだよ")