# Start Up File for T.I.T.A.N

import logging
from discord.ext import commands
from source.core.loader import *
import aiosqlite
import datetime
import os

logging.getLogger("discord").setLevel(logging.WARN)
modules = ["source.cogs.gpt_module"]

# Checks that the database file doenst exceed a certain size. (1MB)
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
        print(f"Logged in as {self.user.name}")

        # Rich Presence
        # OPTIONS
        # do_not_disturb
        # online
        # offline
        # idle
        await self.change_presence(status=discord.Status.do_not_disturb,
                                   activity=discord.CustomActivity(f"{ABOUT_ME}"))

client = Titan()

if __name__ == "__main__":
    client.run(BOT_TOKEN, log_level=logging.WARN)
