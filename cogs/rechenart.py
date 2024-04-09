from discord.ext import commands

class Rechnen(commands.Cog):
    def __init__self(self,bot):
        self.bot = bot

    @commands.command(name="rechnen")
    async def rechnen(self, ctx, a, b):
        summe = float(a) + float(b)
        differenz = float(a) - float(b)
        produkt = float(a) * float(b)
        if b != 0:
            quotient = float(a) / float(b)
        else:
            None
        modulo = float(a) % float(b)

        await ctx.channel.send(f'{a} + {b} = {summe} \n'
                               f'{a} - {b} = {differenz} \n'
                               f'{a} * {b} = {produkt} \n'
                               f'{a} / {b} = {quotient} \n'
                               f'{a} mod {b} = {modulo}')


class Rechenart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rechenArt')
    async def rechenArt(self, ctx, a, b, op):
        #op = str(input("Geben sie die Rechenart ein:"))
        if op == '+':
            summe = float(a) + float(b)
            await ctx.channel.send(f'{a} + {b} = {summe} \n ')
        elif op == '-':
            differenz = float(a) - float(b)
            await ctx.channel.send(f'{a} - {b} = {differenz} \n ')
        elif op == '*':
            produkt = float(a) * float(b)
            await ctx.channel.send(f'{a} * {b} = {produkt} \n ')
        elif op == '/':
            if b != 0:
                quotient = float(a) / float(b)
                await ctx.channel.send(f'{a} / {b} = {quotient} \n ')
            else:
                None
        elif op == '%':
            modulo = float(a) % float(b)
            await ctx.channel.send(f'{a} % {b} = {modulo} \n ')
        else:
            None
        '''await ctx.channel.send(f'{a} + {b} = {summe} \n '
                               f'{a} - {b} = {differenz} \n'
                               f'{a} * {b} = {produkt} \n'
                               f'{a} / {b} = {quotient} \n'
                               f'{a} mod {b} = {modulo}')'''