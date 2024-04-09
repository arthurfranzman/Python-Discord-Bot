from discord.ext import commands

class Ping(commands.Cog):
    def __init__self(self,bot):
        self.bot = bot
    @commands.command(name='ping', aliases=['PING'])
    async def ping(self, ctx):
        await ctx.channel.send('pong')