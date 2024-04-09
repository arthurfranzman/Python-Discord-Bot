import discord
from discord.ext import commands
import asyncio
from discord import Embed

class SquareFunction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='square_function')
    async def square_function(self,ctx):
        num = 0
        user_num = 0
        which_num = Embed(
            title="Zahl für die Quadratfunktion",
            description="Welche Zahl soll quadriert werden?")
        message = await ctx.send(embed=which_num)
        while True:
            try:
                msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=10)
                user_num = int(msg.content)
            except asyncio.TimeoutError:
                error_embed = discord.Embed(title="Berechnung aufgrund von Zeitüberschreitung abgebrochen")
                await message.edit(embed=error_embed)
                return
            except ValueError:
                error_embed2 = discord.Embed(title="Falsche Eingabe, bitte Ganzzahlige positive Zahlen eingeben.")
                await message.edit(embed=error_embed2)
                continue

        res = user_num ** 2
        print(user_num)
        print(res)

        squarembed = Embed(
            title="Quadratfunktion",
            description="Das Quadrat einer gegebenen Zahl wird ausgegeben.",
            color=discord.Color.yellow())
        squarembed.add_field(name=msg.content + " quadriert ergibt:", value= res, inline = True)
        squarembed.set_thumbnail(url="https://www.studyhelp.de/online-lernen/wp-content/uploads/2016/02/bil_quadratisch.png")
        message2 = await ctx.send(embed=squarembed)