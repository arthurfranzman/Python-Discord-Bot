import typing
import discord
from discord.ext import commands
from discord import app_commands
from discord import Embed

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="slash")
    async def slash(self,interaction: discord.Integration, unsichtbar: typing.Optional[str] = "a"):
        await interaction.response.send_message("Slash funktioniert", ephemeral=True)

    @app_commands.command(name='slash_mit_optionalen_variablen')
    @app_commands.describe(unsichtbar='Dies ist die Beschreibung der unsichtbar Variable')
    async def slash_mit_optionalen_variablen(self,interaction: discord.Integration, unsichtbar: typing.Optional[str] = "a"):
        if unsichtbar == 'y' or unsichtbar == 'yes' or unsichtbar == 'j' or unsichtbar == 'ja':
            await interaction.response.send_message('Unsichtbare Ausgabe', ephemeral=True)
        else:
            await interaction.response.send_message("Sichtbare Ausgahe", ephemeral=False)

    @app_commands.command(name='slash_mit_auswahlmoeglichkeiten')
    @app_commands.describe(auswahl='Dies ist die Beschreibung der auswahl Variable')
    async def slash_mit_auswahlmöglichkeit(self, interaction: discord.Integration, auswahl: typing.Literal[ 1, 2, 3]):
        await interaction.response.send_message(f"Variablen können auch übergeben werden:\n{auswahl}")

    @app_commands.command(name='get_color')
    @app_commands.describe(farben='Rollenänderung')
    async def get_color(self, interaction: discord.Integration, farben: typing.Literal["rot", "gelb", "blau", "grün"]):
        guild = interaction.guild
        if farben == "rot":
            color = discord.Color.red()
        elif farben == "gelb":
            color = discord.Color.gold()
        elif farben == "blau":
            color = discord.Color.blue()
        elif farben == "grün":
            color = discord.Color.green()
        else:
            return

        role = discord.utils.get(guild.roles, name=farben)
        await interaction.user.add_roles(role)
        farben_auswahl = Embed(
            title="Rollenänderung",
            description=f"Du hast die Rolle <@&{role.id}> erhalten.",
            color=color)
        await interaction.response.send_message(embed=farben_auswahl)