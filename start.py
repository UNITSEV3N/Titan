# Start Up File for T.I.T.A.N

import logging
from discord.ext import commands
from source.core.loader import *
from colorama import Fore, Style
import aiosqlite
import datetime
import os

logging.getLogger("discord").setLevel(logging.WARN)
modules = ["source.cogs.development"]

# Checks that the database file doenst exceed a certain size.
def check_file_size(file_path, max_size):
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        if file_size <= max_size:
            return True
        else:
            return False
    else:
        # File doesn't exist
        return False


class Titan(commands.Bot):
    def __init__(self, command_prefix="!", intents=discord.Intents.all()):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def setup_hook(self):
        for ext in modules:
            await self.load_extension(ext)

        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=DEFAULT_GUILD)
        await self.tree.sync(guild=DEFAULT_GUILD)

    async def on_ready(self):
        print(f"{Fore.RED} \nLogged in as {Style.RESET_ALL}{Fore.GREEN}{self.user.name} {Style.RESET_ALL}\n")
        await self.change_presence(status=discord.Status.do_not_disturb,
                                   activity=discord.CustomActivity(f"Development of {self.user.display_name}"))

    # -----------------------------------------------------------------------------------------------------------------#
        # database

        client.db = await aiosqlite.connect("source/database/titan.db")
        curse = await client.db.cursor()

        guild_id = str(DEFAULT_GUILD.id)
        query_01 = f"CREATE TABLE IF NOT EXISTS guild_{guild_id}(role_id INTEGER, role_name STRING)"
        query_02 = f"CREATE TABLE IF NOT EXISTS guild_{guild_id}_timer( INTEGER, role_name STRING)"
        await curse.execute(query_01)
        await curse.execute(query_02)
        await client.db.commit()

    # -----------------------------------------------------------------------------------------------------------------#
    # Checks

        # Remove this when done testing - TESTING ONLY
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        channel = self.get_channel(1233127815608668203)
        await channel.send(f"{self.user.name} is Online! @{current_time}")

        max_allowed_size = 1024 * 1024  # 1 MB
        if check_file_size(file_path="source/database/titan.db", max_size=max_allowed_size):
            print("File size is within the allowed limit.")
        else:
            print("File size exceeds the allowed limit.")
            user = client.get_user(525006916251025418)
            await user.send("Titan.db has exceeded its limit!")

    # -----------------------------------------------------------------------------------------------------------------#

client = Titan()

if __name__ == "__main__":
    client.run(BOT_TOKEN, log_level=logging.WARN)
