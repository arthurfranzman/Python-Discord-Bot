import discord
from discord.ext import commands
from discord import app_commands

class Aliases(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='add')
    async def add(self, interaction: discord.Integration, a: float, b: float):
        summe = a + b
        await interaction.response.send_message(f'{a} + {b} = {summe}')