import discord
import discord.ext
from discord.ext import commands
from dislash import InteractionClient, slash_commands, Option, OptionType
from janome.tokenizer import Tokenizer
import markovify
import subprocess
from subprocess import PIPE
import time

bot = commands.Bot(command_prefix="mu:", help_command=None)
slash = InteractionClient(bot)
test_guilds = [706416588160499793]

with open('/home/mumeinosato/discord-bot/marukovi.txt', 'r', encoding="utf-8") as fin:
    text = fin.read()

with open('/home/mumeinosato/discord-bot/token.txt', 'r') as fin:
    content = fin.read()
token = content

def text_split(text):
    str_table = str.maketrans({
        '。': '',   
        '\n': '。',
        '\r': '',
        '(': '（',
        ')': '）',
        '[': '［',
        ']': '］',
        '"':'”',
        "'":"’",
    })
    text = text.translate(str_table)
    t = Tokenizer()
    tokens = t.tokenize(text, wakati=True)
    splitted_text_list = []
    for i in tokens:
        if i != '。' and i != '！' and i != '？':
            i += ' '
        elif i == '。' or i == '！' or i == '？':
            i = '\n'
        splitted_text_list.append(i)
        splitted_text_str = "".join(splitted_text_list)

    return splitted_text_str

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f"ヘルプは mu:help | 導入サーバー数: {len(bot.guilds)}"))
    print("起動しました")
    from cogs import commands
    await bot.add_cog(commands.commands(bot))
    #await bot.add_cog(Gchat.globalCog(bot))

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
        f = open('/home/mumeinosato/discord-bot/marukovi.txt', 'a', encoding='UTF-8')
        f.write(""+text+"\n")
        f.close()
        await inter.reply("登録しました")
        print("["+text+"]が登録されました")
    else:
        await inter.reply('引数がありません')

""""
@slash.command(
    nmae="mcid",
    description="Minecraftのユーザー情報を検索します(javaのみ)" ,
    options = [
        Option('mcid', 'MCID', OptionType.STRING),
    ],
)
async def register_word(inter, text=None):
    if text is not None:
        await inter.reply("https://ja.namemc.com/profile/"+text)
    else:
        await inter.reply('MCIDを入力してください')
"""

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    GLOBAL_CH_NAME = "mumeinosato-global"
    
    if message.channel.name == GLOBAL_CH_NAME:                                                          
        print("success")
        await message.delete() # 元のメッセージは削除しておく
        channels = bot.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        embed = discord.Embed(
            description=message.content, color=0x00bfff)
        embed.set_author(name=message.author.display_name,                                                                            
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))# Embedインスタンスを生成、投稿者、投稿場所などの設定
        for channel in global_channels:# メッセージを埋め込み形式で転送
            await channel.send(embed=embed)

    else:
        channel_name = message.content.replace()
        channel = discord.utils.get(message.guild.channels, name=channel_name)
        last_msg = await channel.fetch_message(channel.last_message_id)
        last_msg_content = last_msg.content
        print(last_msg_content)
        f = open('/home/mumeinosato/discord-bot/marukovi.txt', 'a', encoding='UTF-8')
        f.write(""+text+"\n")
        f.close()
        print("["+text+"]が登録されました")
        text_split(text)
        splitted_text_str = text_split(text)
        text_model_3 = markovify.NewlineText(splitted_text_str, state_size=3)
        for i in range(1):
            out = text_model_3.make_sentence(tries=100)
            sendout = out.replace(' ', '')
            print(sendout)
            #f = open('/home/mumeinosato/discord-bot/marukovi_output.txt', 'w', encoding='UTF-8')
            #f.write(text_model_3.make_sentence(tries=100))
            #f.close()
            await message.channel.send(sendout)    

    await bot.process_commands(message)

bot.run(token)