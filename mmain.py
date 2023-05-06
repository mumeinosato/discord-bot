import discord
import discord.ext
from discord.ext import commands
from dislash import InteractionClient, slash_commands, Option, OptionType
from janome.tokenizer import Tokenizer
import markovify
from googletrans import Translator
import subprocess
from subprocess import PIPE
import time

bot = commands.Bot(command_prefix="mu:", help_command=None)
slash = InteractionClient(bot)
test_guilds = [706416588160499793]
tr = Translator()
voice = None
player = None
discord_voice_channel_id = '711331627283906628' # 特定のボイスチャンネルを指定
youtube_url = 'https://www.youtube.com/watch?v=sqcu2Pble2Y' # youtubeのURLを指定

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
    await bot.change_presence(activity=discord.Game(f"ヘルプは mu:help | 導入サーバー数: {len(bot.guilds)} | スラッシュコマンド実装中"))
    print("起動しました")
    from cogs import commands
    bot.add_cog(commands.commands(bot))

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
    name="user",
    description="IDからユーザーを検索します" ,
    options = [
        Option('userid', 'user', OptionType.STRING),
    ],
)
async def user(inter, userid=None):
    if userid is not None:
        user = await bot.fetch_user(userid)
        ###icon = await bot.avatar_url_as(usid)
        embed = discord.Embed(title="ユーザー情報",description=str(user),color=0x4169e1)
        ###embed.add_field(title="",value=icon)
        await inter.send(embed=embed)
        print(user.name, user.discriminator, str(user))    
    else:
        await inter.reply('Useridを入力してください')

@slash.command(
    name="serverinfo",
    description="サーバーの情報を表示します" ,
    guild_ids = test_guilds
)
async def serverinfo(inter):
    guild = inter.message.guild
    roles =[role for role in guild.roles]
    text_channels = [text_channels for text_channels in guild.text_channels]
    embed = discord.Embed(title=f"ServerInfo - {guild.name}", timestamp=inter.message.created_at, color=0x4169e1)
    embed.set_thumbnail(url=inter.guild.icon_url)
    embed.add_field(name=":arrow_forward:地域", value=f"{inter.guild.region}",inline=False)
    embed.add_field(name=":arrow_forward:チャンネル数", value=f"{len(text_channels)}",inline=False)
    embed.add_field(name=":arrow_forward:ロール数", value=f"{len(roles)}",inline=False)
    embed.add_field(name=":arrow_forward:サーバーブースター", value=guild.premium_subscription_count ,inline=False)
    embed.add_field(name=":arrow_forward:メンバー数", value=guild.member_count,inline=False)
    embed.add_field(name=":arrow_forward:サーバー設立日", value=guild.created_at,inline=False)
    embed.set_footer(text=f"実行者:{inter.author}", icon_url=inter.author.avatar_url)
    await inter.send(embed=embed)

@slash.command(
    name="translation",
    description="翻訳します" ,
    options = [
        Option('text', '翻訳する語句', OptionType.STRING),
        Option('original_language', '元の言語', OptionType.STRING),
        Option('target_language', '翻訳後の言語', OptionType.STRING),
    ],
    guild_ids = test_guilds
)
async def translation(inter, text=None, original_language=None, target_language=None):
    print(text)
    print(original_language)
    print(target_language)
    """"
    if text is not None:
        if original_language is not None:
            result = tr.translate(text, src=original_language, dest=target_language).text
            embed = discord.Embed(title="翻訳結果", color=0x4169e1)
            embed.add_field(name=original_language+"→"+target_language, value=text+"--->"+result, inline=False)
            await inter.send(embed=embed)
        else:
            result = tr.translate(text, src="en", dest="ja").text
            embed = discord.Embed(title="翻訳結果", color=0x4169e1)
            embed.add_field(name="英語→日本語", value=text+"--->"+result, inline=False)
            await inter.send(embed=embed)
    else:
        await inter.reply('テキストを入力してください')   
    """

@slash.command(
    name="mcid",
    description="Minecraftのユーザー情報を検索します(javaのみ)" ,
    options = [
        Option('mcid', 'MCID', OptionType.STRING),
    ],
)
async def mcid(inter, mcid=None):
    if mcid is not None:
        await inter.reply("https://ja.namemc.com/profile/"+mcid)
    else:
        await inter.reply('MCIDを入力してください')

@slash.command(
    name="register_word",
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

    elif message.content.startswith("mu:"):
        return

    elif message.content.startswith("!play"):
        if message.author.voice_channel is None:
            await bot.send_message(message.channel ,'ボイスチャンネルに参加してからコマンドを打ってください。')
            return
        if voice == None:
            # ボイスチャンネルIDが未指定なら
            if discord_voice_channel_id == '':
                voice = await bot.join_voice_channel(message.author.voice_channel)
            # ボイスチャンネルIDが指定されていたら
            else:
                voice = await bot.join_voice_channel(bot.get_channel(discord_voice_channel_id))
        # 接続済みか確認
        elif(voice.is_connected() == True):
            # 再生中の場合は一度停止
            if(player.is_playing()):
                player.stop()
            # ボイスチャンネルIDが未指定なら
            if discord_voice_channel_id == '':
                await voice.move_to(message.author.voice_channel)
            # ボイスチャンネルIDが指定されていたら
            else:
                await voice.move_to(bot.get_channel(discord_voice_channel_id))
        # youtubeからダウンロードし、再生
        player = await voice.create_ytdl_player(youtube_url)
        player.start()
        return
    
    # 再生中の音楽を停止させる
    elif message.content.startswith("!stop"):
        if(player.is_playing()):
                player.stop()
                return
    
    # botをボイスチャットから切断させる
    elif message.content.startswith("!disconnect"):
        if voice is not None:
            await voice.disconnect()
            voice = None
            return        

    else:
        guild = message.channel
        print(f"{guild.name}からメッセージが来ました！")
        channelid = discord.utils.get(message.guild.channels, name=guild.name)
        channel = bot.get_channel(channelid)
        getmsg = message.content 
        print(getmsg)
        if "@" in getmsg:
            print("取得した文字列に@が入っていました")
        else:
            if "http" in getmsg:
                print("取得した文字列にhttpが入っていました")
            else:
                f = open('/home/mumeinosato/discord-bot/marukovi.txt', 'a', encoding='UTF-8')
                f.write(""+getmsg+"\n")
                f.close()
                print("["+getmsg+"]が登録されました")
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