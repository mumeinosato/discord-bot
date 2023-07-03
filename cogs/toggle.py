import discord
from discord import app_commands
from discord.ext import commands
import json
import os

class toggle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="chat", description="AIの返信をon/offします")
    @app_commands.default_permissions(administrator=True)
    async def chat(self, inter: discord.Interaction):
        channel = inter.channel
        id = channel.id
        file_path = os.path.abspath("cogs/json/chat.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    print("ファイルの形式が正しくありません")
                    return
        else:
            data = []
        if id not in data:   
            data.append(id)
            await inter.response.send_message("有効化しました")
        else:
            data.remove(id)   
            await inter.response.send_message("無効化しました")
        with open(file_path, "w") as file:
            json.dump(data, file)    

async def setup(bot):
    await bot.add_cog(toggle(bot))
    print("toggleを読み込んだよ")