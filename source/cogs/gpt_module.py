# ChatGPT Integration
# 3 Commands used to create small - medium quest for users
# Has sets of rules and templates it will follow (source/config/check rules.yml)
# Bot has a 1 day cooldown per person (will change it to a 10 per day for the whole guild)

import asyncio
from discord.ext import commands
from discord import app_commands
from openai import OpenAI
from source.core.loader import *

# Open AI Key
OpenAI = OpenAI(api_key=os.environ.get("AI_KEY"))


# TIMERS/COOLDOWNS
TIMER = 86400
RATE = 1


# AI Prompt: max_tokens, temperature, messages, model
# Returns ChatGPT reponse.
# All Quest AI commands use this function
async def ai_prompt(prompt: str):
    try:
        chat_response = OpenAI.chat.completions.create(
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt} Here are your rules: {PROTOCOLS}, Follow these templates given: {MISSION_TEMPLATES}"
                }
            ],
            model=AI_MODEL, )

        return chat_response.choices[0].message.content
    except:
        return "NO KEY! - Please get a key from https://platform.openai.com/api-keys"


class QuestGiver(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    async def check_role(self, interaction):
        user_roles = [role.id for role in interaction.user.roles]
        for role in ALLOWED_ROLES:
            if role in user_roles:
                return True

        await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
        print("\nFailed Request: Incorrect Roles!")
        return False

    # -----------------------------------------------------------------------------------------------------------------#

    # Create-patrol
    # Creates a patrol route from a to b
    # Less accurate feature since the templates are missing some data
    @app_commands.checks.cooldown(RATE, TIMER)
    @app_commands.command(name="create_patrol", description="AI - Creates patrol")
    async def create_patrol(self, interaction, route: str):
        if not await self.check_role(interaction):
            return

        await interaction.response.defer(ephemeral=False)

        prompt = ai_prompt(f"Give me a route: {route}")

        await asyncio.sleep(3)
        await interaction.followup.send(f"{prompt}")

    @create_patrol.error
    async def patrol_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, discord.app_commands.CommandOnCooldown):
            await interaction.response.send_message(
                content=f"DENIED! I can only complete this request once per day. Try again tomorrow!", ephemeral=True)
        else:
            await interaction.response.send_message(content=str(error), ephemeral=True)

    # -----------------------------------------------------------------------------------------------------------------#

    # Create-mission
    # Creates a mission with theme given by user.
    @app_commands.checks.cooldown(RATE, TIMER)
    @app_commands.command(name="create_mission", description="AI - Creates Mission")
    async def create_mission(self, interaction, theme: str):
        if not await self.check_role(interaction):
            return

        await interaction.response.defer(ephemeral=False)

        prompt = ai_prompt(f"This is a mission, generate one for me. Respond with one prompt. "
                           f"\nCreate mission with the theme: {theme}")

        await asyncio.sleep(5)
        await interaction.followup.send(f"{prompt}")

    @create_patrol.error
    async def mission_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, discord.app_commands.CommandOnCooldown):
            await interaction.response.send_message(
                content=f"DENIED! I can only complete this request once per day. Try again tomorrow!", ephemeral=True)
        else:
            await interaction.response.send_message(content=str(error), ephemeral=True)

    # -----------------------------------------------------------------------------------------------------------------#

    # Create-frago
    # Creates a frago mission with themed given by user.
    @app_commands.checks.cooldown(RATE, TIMER)
    @app_commands.command(name="create_frago", description="AI - Creates Frago")
    async def create_frago(self, interaction, theme: str):
        if not await self.check_role(interaction):
            return

        await interaction.response.defer(ephemeral=False)

        prompt = ai_prompt(f"This is a mission, generate one for me. Respond with one prompt. "
                           f"\nCreate mission with the theme: {theme}")

        await asyncio.sleep(5)
        await interaction.followup.send(f"{prompt}")

    @create_frago.error
    async def frago_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, discord.app_commands.CommandOnCooldown):
            await interaction.response.send_message(
                content=f"DENIED! I can only complete this request once per day. Try again tomorrow!", ephemeral=True)
        else:
            await interaction.response.send_message(content=str(error), ephemeral=True)

    # -----------------------------------------------------------------------------------------------------------------#

async def setup(client: commands.Bot) -> None:
    await client.add_cog(QuestGiver(client))
