# loads all config and env data to be used through-out the codebase

import os
import discord
import yaml
from dotenv import load_dotenv


def load_rules():
    with open("source/config/rules.yml") as file:
        rules = yaml.safe_load(file)
    return rules


def load_config():
    with open("source/config/config.yml") as file:
        config = yaml.safe_load(file)
    return config


load_dotenv()
RULES = load_rules()
CONFIG = load_config()


# BOT CONSTANTS - TOKENS
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

# CONFIG CONSTANTS
DEFAULT_GUILD = discord.Object(id=CONFIG.get("DEFAULT_GUILD"))
ALLOWED_ROLES = CONFIG.get("ROLES")
AI_MODEL = CONFIG.get("DEFAULT_MODEL")
TEMPERATURE = CONFIG.get("TEMPERATURE")
MAX_TOKENS = CONFIG.get("MAX_TOKENS")

# RULES CONSTANTS
PROTOCOLS = RULES.get("PROTOCOLS")
MISSION_TEMPLATES = RULES.get("MISSION TEMPLATES")

# STATUS and ABOUT ME
ABOUT_ME = CONFIG.get("ABOUT")
STATUS = CONFIG.get("STATUS")
