import discord
import discord.ext
from discord.ext import commands

bot = commands.Bot(command_prefix="mu:", help_command=None)

with open('/home/mumeinosato/discord-bot/token.txt', 'r') as fin:
    content = fin.read()
token = content
print("起動しました")

bot.run("token")