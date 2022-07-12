import discord
import discord.ext
from discord.ext import commands
from dislash import slash_commands, Option, OptionType

bot = commands.Bot(command_prefix="mu:", intents=discord.Intents.all())

with open('/home/mumeinosato/discord-bot/token.txt', 'r') as fin:
    content = fin.read()
token = content
print("起動しました")

bot.run(token)