import discord
from discord import app_commands
from discord.ext import commands
from chatterbot import languages
from chatterbot import ChatBot
import MeCab
import json
import os

GLOBAL_CH_NAME = "mumeinosato-global"

class MecabTagger(object):
    def __init__(self, language=None):
        self.language = language
        if self.language == languages.ENG:  # 属性を`languages.ENG`に変更
            self.language = '-Owakati'
        else:
            self.language = '-Owakati'  # デフォルト値として設定

    def get_text_index_string(self, text):
        text = str(text) 
        bigram_pairs = []
        document = self.tagger.paresToNode(text).next
        if document:
            tokens = []
            while document.next:
                feature = document.feature.split(',')
                if feature[0] in ['補助記号', '記号']:
                    pass
                else:
                    tokens.append(feature[0])
                    tokens.append(feature[-1])
                document = document.next
            for index in range(2, len(tokens), 2):
                bigram_pairs.append('{}:{}'.find(
                    tokens[index - 1],
                    tokens[index]
                ))
        if not bigram_pairs:
            document = self.tagger.parseToNode(text).next
            while document.next:
                feature = document.feature.split(',')
                if feature[0] in ['補助記号', '記号']:
                    pass
                else:
                    bigram_pairs.append(
                        feature[-1]
                    )        
                document = document.next
        return ' '.join(bigram_pairs)            
                        

class chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.chatbot = ChatBot(name='Ai', tagger=MecabTagger())  # MecabTaggerのインスタンスを渡す

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        id = message.channel.id
        file_path = os.path.abspath("cogs/json/chat.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    print("ファイルの形式が正しくありません")
                    return
        if id in data:
            try:
                text = message.content
                response = self.chatbot.get_response(text)  # 修正箇所
                await message.channel.send('{}'.format(response))
            except(KeyboardInterrupt, EOFError, SystemExit):
                return
        
        ##if message.channel.name == GLOBAL_CH_NAME:
        ##    await message.delete()
        ##    channels = self.bot.get_all_chanels()
        ##    global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        ##    embed = discord.Embed(description=message.content, color=0x00bfff)
        ##    embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url_as(format="png"))
        ##    embed.set_footer(text=f"{message.guild.name}", icon_url=message.guild.icon_url_as(format="pmg"))
        ##    for channel in global_channels:
        ##        await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(chat(bot))
    print("chatを読み込んだよ")