import discord
import discord.ext
from discord.ext import commands
from dislash import InteractionClient, slash_commands, Option, OptionType

bot = commands.Bot(command_prefix="mu:", help_command=None)
slash = InteractionClient(bot)
test_guilds = [706416588160499793]


with open('/home/mumeinosato/discord-bot/token.txt', 'r') as fin:
    content = fin.read()
token = content
print("起動しました")

@slash.command(
    name="help",
    description="helpを表示します" ,
)
async def help(inter):#コマンドを定義するときの関数は必ずContextという引数が渡される。つまり引数を最低一つだけでも書いておかないと動かないので注意
    embed = discord.Embed(title="ヘルプ", description="このヘルプコマンドにはプレフィックスを書いていないため、\n実行には全て`mu:コマンド名`とする必要があります。",color=0x4169e1)
    #↑ここのテキストは自分で修正よろしく
    embed.add_field(name="**help**", value="このコマンドです。",inline=False)
    embed.add_field(name="**about**", value="botについてや、botの招待リンク、サポートサーバーを確認できます。",inline=False)
    embed.add_field(name="**newinfo**", value="新着情報を確認します。",inline=False)
    embed.add_field(name="**globalch**", value="「mumeinosato-global」というチャンネルを作成しグローバルチャットに接続します。",inline=False)
    embed.add_field(name="**game**", value="このbotでできるゲーム一覧を表示します。",inline=False)
    embed.add_field(name="**tool**", value="便利ツール一覧を表示します。",inline=False)
    embed.add_field(name="**servermanagement**", value="サーバー運営に役立つコマンド一覧を表示します。", inline=False)
    embed.add_field(name="**partner**", value="提携しているもの一覧を表示します。",inline=False)
    embed.add_field(name="**myinformation 〔パスワード〕**", value="登録内容を表示します。（パスワードを持っている場合のみアクセスできます。)",inline=False)
    await inter.send(embed=embed)#Contextにはいろいろな情報が入っており、そこから様々な関数、情報にアクセスできる。ctx.sendがその一つ

@slash.command(
    nmae="register_word",
    description="AIの語句登録をします" ,
    options = [
        Option('text', '登録する語句', OptionType.STRING),
    ],
)
async def register_word(inter, text=None):
    if text is not None:
        f = open('/home/mumeinosato/discord-bot/markovi.txt', 'a', encoding='UTF-8')
        f.write(text+"\n")
        f.close()
        await inter.reply("登録しました")
        print(text+"が登録されました")
    else:
        await inter.reply('引数がありません')

#@slash.command(
#    nmae="markovi",
#    description="文を自動生成します" ,
#    guild_ids=test_guilds    
#)
#async def markovi(inter):
    

bot.run(token)