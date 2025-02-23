import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import asyncio
import datetime

# Load environment variables
load_dotenv()

# Bot configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID', 0))
STAFF_ROLE_ID = int(os.getenv('STAFF_ROLE_ID', 0))
TICKET_CATEGORY_ID = int(os.getenv('TICKET_CATEGORY_ID', 0))

# Initialize bot with intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Ticket button view
class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Create Ticket", style=discord.ButtonStyle.primary, custom_id="create_ticket")
    async def create_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Check if user already has a ticket
        guild = interaction.guild
        existing_ticket = discord.utils.get(guild.channels, 
                                         name=f"ticket-{interaction.user.name.lower()}")
        
        if existing_ticket:
            await interaction.response.send_message(
                "You already have an open ticket!", ephemeral=True)
            return

        # Create ticket channel
        category = interaction.guild.get_channel(TICKET_CATEGORY_ID)
        
        # Set permissions
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            guild.get_role(STAFF_ROLE_ID): discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }

        # Create the channel
        channel = await guild.create_text_channel(
            name=f"ticket-{interaction.user.name}",
            category=category,
            overwrites=overwrites
        )

        # Send initial message in ticket channel
        embed = discord.Embed(
            title="Ticket Created",
            description=f"Welcome {interaction.user.mention}! Please describe your issue and wait for staff to respond.",
            color=discord.Color.green(),
            timestamp=datetime.datetime.utcnow()
        )
        
        close_button = TicketCloseView()
        await channel.send(embed=embed, view=close_button)
        
        await interaction.response.send_message(
            f"Ticket created! Check {channel.mention}", ephemeral=True)

class TicketCloseView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Close Ticket", style=discord.ButtonStyle.danger, custom_id="close_ticket")
    async def close_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.get_role(STAFF_ROLE_ID):
            await interaction.response.send_message(
                "Only staff members can close tickets!", ephemeral=True)
            return

        await interaction.response.send_message("Closing ticket in 5 seconds...")
        await asyncio.sleep(5)
        await interaction.channel.delete()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    """Sets up the ticket system"""
    embed = discord.Embed(
        title="🎫 Ticket System",
        description="Click the button below to create a ticket",
        color=discord.Color.blue()
    )
    
    await ctx.send(embed=embed, view=TicketView())

# Run the bot
if __name__ == "__main__":
    bot.run(DISCORD_TOKEN) 