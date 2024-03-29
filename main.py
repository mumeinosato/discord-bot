import discord
import discord.ext
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
import traceback

load_dotenv()

token = os.getenv("token")

class Mumeinosato(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="mu:",
            intents=discord.Intents.all()
        )

    async def on_ready(self):
        for file in os.listdir('cogs'):
            if file.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{file[:-3]}')
                    print(f"Loaded cogs: cogs.{file[:-3]}")
                except Exception as e:
                    print(f"cogs.{file[:-3]} failed to load", e)
                    traceback.print_exc()
        try:
            ##await self.load_extension("jishaku") # Load jishaku
            print("Loaded extension: Jishaku")
        except Exception:
            traceback.print_exc()
        await self.tree.sync() # Slash command automatic sync
        await self.change_presence(activity=discord.Game(f"導入サーバー数: {len(bot.guilds)} | ユーザー数: {len(bot.users)}"))
        ##await bot.get_channel(1058005805426814976).send(embed=discord.Embed(title="Startup Program finished!", description=f"Logging in {self.user.name}\nStart time: {discord.utils.format_dt(self.start_time)}"))
        print(f"Startup Program finished!\nLogging in {self.user.name}")



if __name__ == "__main__":
    print("Program starting...")
    bot=Mumeinosato()
    try:
        bot.run(token)
    except Exception:
        print("Program Crashed!\n")
        traceback.print_exc()