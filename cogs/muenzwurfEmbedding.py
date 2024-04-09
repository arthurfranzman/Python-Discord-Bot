from discord.ext import commands
import random
from discord import Embed
import discord
import time

class MuenzWurf(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='muenzwurf-embed')
    async def muenz_embedding(self, ctx, wahl):
        # Ein Embed erstellen
        server = ctx.guild
        muenz_embedding = Embed(
            title="Münzwurf",
            description="Es wird eine Münze geworfen...",
            color=discord.Color.yellow(),  # Farbe des Embeds
        )
        ergebnis = random.randrange(0, 2)
        if wahl == 'Kopf' and ergebnis == 0:
            res = (f'Du hast Kopf gesetzt und mit Kopf 🪙 gewonnen!')
        elif wahl == 'Zahl' and ergebnis == 1:
            res = (f'Du hast Zahl gesetzt und mit Zahl 💯 gewonnen!')
        elif wahl == 'Kopf' and ergebnis == 1:
            res = (f'Du hast Kopf gesetzt und mit Zahl 💯 verloren!')
        elif wahl == 'Zahl' and ergebnis == 0:
            res = (f'Du hast Zahl gesetzt und mit Kopf 🪙 verloren!')
        else:
            await ctx.send(
                f'Du hast eine falsche Eingabe gemacht! Die Syntax ist wie folgt: "$muenzwurf Zahl" oder "$muenzwurf Kopf"!')
        # Felder hinzufügen
        muenz_embedding.add_field(name="Das Ergebnis:", value="Einen Moment...", inline=True)
        # Footer hinzufügen
        # serverinfo.set_footer(text="Fußzeile des Embeds")
        # Bild hinzufügen
        muenz_embedding.set_thumbnail(url=server.icon)
        # Autor hinzufügen
        # serverinfo.set_author(name="Autor des Embeds", icon_url=ctx.author.display_avatar)
        # Timestamp hinzufügen
        muenz_embedding.timestamp = discord.utils.utcnow()
        # Ein Embed in einer Nachricht senden
        message = await ctx.send(embed=muenz_embedding)
        time.sleep(1)
        muenz_embedding.set_field_at(index=0, name='Das Ergebnis:', value=res)
        await message.edit(embed=muenz_embedding)