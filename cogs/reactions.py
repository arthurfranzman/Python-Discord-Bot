from discord.ext import commands

class React(commands.Cog):
    def __init__self(self,bot):
        self.bot = bot
    @commands.command(name='react')
    async def reactionchannel(self, ctx):
        lotofreaction = await ctx.send('every reaction youtuber be like')

        await ctx.message.add_reaction('😂')
        await lotofreaction.add_reaction('😴')
        await lotofreaction.add_reaction('🥱')
        await lotofreaction.add_reaction('💤')
        await lotofreaction.add_reaction('🛏️')
        await lotofreaction.add_reaction('😲')