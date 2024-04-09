import requests
import json
import typing
import discord
from discord.ext import commands
from discord import app_commands
from discord import Embed

class Memes(commands.Cog):
    def __init__self(self,bot):
        self.bot = bot

    @app_commands.command(name='meme')
    async def memes(self,interaction: discord.Integration):
        response = requests.get('https://meme-api.com/gimme')
        json_data = json.loads(response.text)
        meme_embed = Embed(
            title="Reddit Meme",)
        meme_embed.set_image(url=json_data.get('url'))
        meme_embed.add_field(name="", value=f"[Link]({json_data.get('url')})", inline=False)
        meme_embed.add_field(name="", value=f"r/{json_data.get('subreddit')}", inline=True)
        meme_embed.add_field(name="", value=f"**{json_data.get('title')}**", inline=False)
        if not json_data.get('nsfw'): await interaction.response.send_message(embed=meme_embed)