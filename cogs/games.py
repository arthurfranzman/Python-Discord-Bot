from discord.ext import commands
import random
from discord import Embed
import discord
import time

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='muenzwurf')
    async def muenzwurf(self, ctx, wahl:str):
        ergebnis = random.randrange(0,2)
        if wahl == 'Kopf' and ergebnis == 0:
            await ctx.send(f'Du hast Kopf gesetzt und mit Kopf 🪙 gewonnen!')
        elif wahl == 'Zahl' and ergebnis == 1:
            await ctx.send(f'Du hast Zahl gesetzt und mit Zahl 💯 gewonnen!')
        elif wahl == 'Kopf' and ergebnis == 1:
            await ctx.send(f'Du hast Kopf gesetzt und mit Zahl 💯 verloren!')
        elif wahl == 'Zahl' and ergebnis == 0:
            await ctx.send(f'Du hast Zahl gesetzt und mit Kopf 🪙 verloren!')
        else:
            await ctx.send(f'Du hast eine falsche Eingabe gemacht! Die Syntax ist wie folgt: "$muenzwurf Zahl" oder "$muenzwurf Kopf"!')


    ''' @muenzwurf.error
        async def muenzwurf_error(ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send('Fehler. Es fehlen erforderliche Argumente. Die Syntax ist wie folgt: "$muenzwurf Zahl" oder "$muenzwurf Kopf"!')
    '''


    @commands.command (name ='rps')
    async def scheresteinpapier(self, ctx, wahl:str):
        # Ein Embed erstellen
        server = ctx.guild
        scheresteinpapier = Embed(
            title="Münzwurf",
            description="Es wird eine Münze geworfen...",
            color=discord.Color.yellow(), # Farbe des Embeds
        )
        ergebnis = random.randrange(0, 3)
        result = 0
        if wahl == 'Schere' and ergebnis == 0:
            result = (f'Du hast Schere gesetzt und mit Schere ✂️ gewonnen!')
        elif wahl == 'Stein' and ergebnis == 1:
            result = (f'Du hast Stein gesetzt und mit Stein 🗿 gewonnen!')
        elif wahl == 'Kopf' and ergebnis == 2:
            result = (f'Du hast Papier gesetzt und mit Papier 📃 gewonnen!')
        else:
            await ctx.channel.send(
                f'Du hast eine falsche Eingabe gemacht! Die Syntax ist wie folgt: "$rps Schere", "$rps Stein" oder "$rps Papier"!')
        # Felder hinzufügen
        scheresteinpapier.add_field(name="Das Ergebnis:", value= "Einen Moment...", inline = True)
        # Footer hinzufügen
        #serverinfo.set_footer(text="Fußzeile des Embeds")
        # Bild hinzufügen
        scheresteinpapier.set_thumbnail(url=server.icon)
        # Autor hinzufügen
        #serverinfo.set_author(name="Autor des Embeds", icon_url=ctx.author.display_avatar)
        # Timestamp hinzufügen
        scheresteinpapier.timestamp = discord.utils.utcnow()
        # Ein Embed in einer Nachricht senden
        message = await ctx.channel.send(embed=scheresteinpapier)
        time.sleep(3)
        scheresteinpapier.set_field_at(index=0, name ='Das Ergebnis:', value=result)
        await message.edit(embed=scheresteinpapier)