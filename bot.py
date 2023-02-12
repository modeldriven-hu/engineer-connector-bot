import os

# https://www.geeksforgeeks.org/building-a-discord-bot-in-python/

import discord
from discord.ext.commands import Context
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.command(name="set_location", help="Set the location")
async def set_location(ctx: Context):
    print(ctx.current_argument)
    print(ctx.current_parameter)
    city = 'Budapest'
    country = 'Hungary'
    await ctx.send("Location for user " + ctx.author.name + " set to " + city + "," + country)

@bot.command(name="remove_location", help="Remove the location")
async def remove_location(ctx: Context):
    await ctx.send("Location removed for " + ctx.author.name)

bot.run(TOKEN)
