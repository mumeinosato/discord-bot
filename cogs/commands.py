import discord
from discord.ext import commands
from dislash import InteractionClient, slash_commands, Option, OptionType

class mycog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx): 

def setup(bot):
    print('commandsファイルを読み込んだよ！')
    bot.add_cog(commands(bot))        