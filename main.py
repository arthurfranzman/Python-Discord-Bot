import time
import discord
from discord.ext import commands
from discord import Embed
from discord import app_commands
import os
import tracemalloc
from cogs.games import Games
from cogs.muenzwurfEmbedding import MuenzWurf
from cogs.squareFunc import SquareFunction
from cogs.rechenart import Rechenart
from cogs.rechenart import Rechnen
from cogs.reactions import React
from cogs.ping import Ping
from cogs.add import Aliases
from cogs.slash import Slash
from cogs.role_management import RoleManagement
from cogs.meme_api import Memes
from cogs.stocktracker import Stocks
tracemalloc.start()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    await bot.add_cog(Games(bot))
    await bot.add_cog(MuenzWurf(bot))
    await bot.add_cog(SquareFunction(bot))
    await bot.add_cog(Rechenart(bot))
    await bot.add_cog(React(bot))
    await bot.add_cog(Rechnen(bot))
    await bot.add_cog(Ping(bot))
    await bot.add_cog(Aliases(bot))
    await bot.add_cog(RoleManagement(bot))
    await bot.add_cog(Slash(bot))
    await bot.add_cog(Memes(bot))
    await bot.add_cog(Stocks(bot))
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} Commands')
    except Exception as e:
        print(e)
    print(f'Eingeloggt als {bot.user}')


@bot.tree.context_menu(name="Show join date")
async def get_joined_date(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f"Member joined: {discord.utils.format_dt(member.joined_at)} ", ephemeral=True)

@bot.tree.context_menu(name="Nutzerinfo")
async def userinfo(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f"Beigetreten, ID und Name{discord.utils.format_dt(member.joined_at),(member.id)}", ephemeral=True)
    userinfo_embed = Embed(
        title="Nutzerinformationen",
        description="Nutzer-ID und -Name",
        color=discord.Color.yellow(),  # Farbe des Embeds
    )
    userinfo_embed.add_field(name="Das Ergebnis:", value="Einen Moment...", inline=True)
bot.run('some discord bot token') # Hier wäre dann das Discord-Bot-Token...



# Idee für Projekt nächste Woche: (finanzen.net oder Yahoo Finance) oder andere Aktien-Plattform-API bei Discord einbetten und in Embed anzeigen lassen
# Frage: Robolab, keine Experience
