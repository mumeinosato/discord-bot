from lib2to3.pgen2 import token
import discord
import discord.ext
from discord.ext import commands

bot = commands.Bot(command_prefix="mu:", help_command=None)

with open('/home/mumeinosato/discord-bot/token.txt', 'r') as fin:
    token = fin.read()

bot.run("token")