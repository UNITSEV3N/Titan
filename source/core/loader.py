# loads all config and env data to be used through-out the codebase

import os
import discord
import yaml
from dotenv import load_dotenv


def load_config():
    with open("source/config/config_dev.yml") as file:
        config = yaml.safe_load(file)
    return config


load_dotenv()
data = load_config()

# BOT CONSTANTS
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DEFAULT_GUILD = discord.Object(id=os.getenv("DEFAULT_GUILD"))
ALLOWED_ROLES = data["SETUP"]["ROLES"]

# OPEN AI CONSTANTS
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
AI_MODEL = os.getenv("DEFAULT_MODEL")
TEMPERATURE = float(os.getenv("TEMPERATURE"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS"))
PROTOCOLS = data.get("PROTOCOLS")
MISSION_TEMPLATES = data.get("MISSION TEMPLATES")
