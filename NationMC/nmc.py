import discord
import discord.ext
from discord.ext import commands
from janome.tokenizer import Tokenizer
import markovify
import random

bot = commands.Bot(command_prefix="nm:", help_command=None)

with open('/home/mumeinosato/discord-bot/marukovi.txt', 'r', encoding="utf-8") as fin:
    text = fin.read()

with open('/home/mumeinosato/nmc-bot/token.txt', 'r') as fin:
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
async def on_message(message):
    if message.author.bot:
        return

    else:
        guild = message.channel
        print(f"{guild.name}からメッセージが来ました！")
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
                x = random.randint(1,5)
                print(x)
                if x == 1:
                    splitted_text_str = text_split(text)
                    text_model_3 = markovify.NewlineText(splitted_text_str, state_size=3)
                    for i in range(1):
                        out = text_model_3.make_sentence(tries=100)
                        sendout = out.replace(' ', '')
                        print(sendout)
                        await message.channel.send(sendout)
    await bot.process_commands(message)                

bot.run(token)    