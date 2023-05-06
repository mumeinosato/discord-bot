import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

bot = discord.Client(intents=discord.Intents.all())
# または:
# bot = commands.Bot(command_prefix='@', intents=discord.Intents.all())

slash_client = SlashCommand(bot)

@slash_client.slash(name="help", description="ヘルプを表示します")
async def _slash_help(ctx: SlashContext):
    await ctx.send(content="Hello!")

@bot.event
async def on_ready():
  print('bot ready.')

bot.run("")
