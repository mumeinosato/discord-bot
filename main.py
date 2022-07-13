import discord.ext
from discord.ext import commands
from dislash import InteractionClient, slash_commands, Option, OptionType
import sys 
import pya3rt 
#import traceback

with open('/home/mumeinosato/discord-bot/token.txt', 'r') as fin:
    content = fin.read()
token = content

with open('/home/mumeinosato/discord-bot/talkapi.txt', 'r') as fin:
    talkapi = fin.read()
TALK_API_KEY = talkapi

bot = commands.Bot(command_prefix="mu:", help_command=None), pya3rt.TalkClient(TALK_API_KEY)
slash = InteractionClient(bot)
test_guilds = [706416588160499793]

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
        f = open('/home/mumeinosato/discord-bot/markovi.txt', 'a', encoding='UTF-8')
        f.write(text+"\n")
        f.close()
        await inter.reply("登録しました")
        print(text+"が登録されました")
    else:
        await inter.reply('引数がありません')

@slash.command(
    nmae="ai_stop",
    description="自動返信を停止します" ,
)
async def ai_stop(inter):
    if talkai == 1:
        talkai = 0
    else:
        talkai = 1


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

    elif message.content.startswith('こんにちは'):
            channel_name = message.content.replace('こんにちは', '')
            channel = discord.utils.get(message.guild.channels, name=channel_name)
            last_msg = await channel.fetch_message(channel.last_message_id)
            last_msg_content = last_msg.content
            response = bot.talk(last_msg_content)
            await message.channel.send(((response['results'])[0])['reply'])
    
    await bot.process_commands(message)

bot.run(token)