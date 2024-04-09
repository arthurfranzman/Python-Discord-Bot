import discord
from discord.ext import commands
from discord import app_commands

class RoleManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='clear_roles', description='Entfernt alle Rollen vom aufrufenden Benutzer.')
    async def clear_roles(self, interaction: discord.Interaction):
        # Stellen Sie sicher, dass der Bot die Berechtigung zum Entfernen von Rollen hat
        if interaction.user.guild_permissions.manage_roles:
            member = interaction.guild.get_member(interaction.user.id)
            roles = member.roles
            # Entferne alle Rollen außer der @everyone Rolle, die standardmäßig nicht entfernt werden kann
            roles_to_remove = [role for role in roles if role.name != '@everyone']
            await member.remove_roles(*roles_to_remove, reason="Alle Rollen auf Anfrage des Benutzers entfernt.")
            await interaction.response.send_message(f"Alle Rollen wurden entfernt.", ephemeral=True)
        else:
            await interaction.response.send_message("Du hast keine Berechtigung, Rollen zu verwalten.", ephemeral=True)