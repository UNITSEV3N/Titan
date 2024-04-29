# Start Up File for T.I.T.A.N

import logging
from discord.ext import commands
from source.core.loader import *
import aiosqlite
import datetime
import os

logging.getLogger("discord").setLevel(logging.WARN)
modules = ["source.cogs.gpt_module"]

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

        # Rich Presence (change it to ur prefered settings)
        # OPTIONS
        # -------------------------- #
        # do_not_disturb
        # online
        # offline
        # idle
        # -------------------------- #

        await self.change_presence(status=discord.Status.do_not_disturb,
                                   activity=discord.CustomActivity(f"{ABOUT_ME}"))

client = Titan()

if __name__ == "__main__":
    client.run(BOT_TOKEN, log_level=logging.WARN)
