import imp
from pickle import GLOBAL
import discord
from discord.ext import commands
from dislash import InteractionClient, slash_commands, Option, OptionType
import asyncio
from dataclasses import dataclass
from fileinput import filename
import youtube_dl
import ffmpeg


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

    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.message.guild
        roles =[role for role in guild.roles]
        text_channels = [text_channels for text_channels in guild.text_channels]
        embed = discord.Embed(title=f"ServerInfo - {guild.name}", timestamp=ctx.message.created_at, color=0x4169e1)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name=":arrow_forward:地域", value=f"{ctx.guild.region}",inline=False)
        embed.add_field(name=":arrow_forward:チャンネル数", value=f"{len(text_channels)}",inline=False)
        embed.add_field(name=":arrow_forward:ロール数", value=f"{len(roles)}",inline=False)
        embed.add_field(name=":arrow_forward:サーバーブースター", value=guild.premium_subscription_count ,inline=False)
        embed.add_field(name=":arrow_forward:メンバー数", value=guild.member_count,inline=False)
        embed.add_field(name=":arrow_forward:サーバー設立日", value=guild.created_at,inline=False)
        embed.set_footer(text=f"実行者:{ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def comanndscog(bot):
    print('commandsファイルを読み込んだよ！')
    bot.add_cog(commands(bot))        