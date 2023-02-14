import os

# https://www.geeksforgeeks.org/building-a-discord-bot-in-python/

import discord
from discord.ext.commands import Context
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.command(name="ping", help="Pings the bot")  # for debugging purpose
async def ping(ctx: Context):
    username = str(ctx.author).split("#")[0]
    print(f'Pinged by {username}')
    await ctx.send('Pong!')

@bot.command(name="set_location", help="Set the location")
async def set_location(ctx: Context, city="Helm's Deep", country="Rohan"):
    command = ctx.message.clean_content
    print(ctx.current_argument)
    print(ctx.current_parameter)
    username = str(ctx.author).split("#")[0]
    city = city.replace(',', '').replace('.', '')
    country = country.replace(',', '').replace('.', '')
    print("Location for user " + ctx.author.name + " set to " + city + ", " + country)
    await ctx.send("Location for user " + ctx.author.name + " set to " + city + ", " + country)

@bot.command(name="remove_location", help="Remove the location")
async def remove_location(ctx: Context):
    username = str(ctx.author).split("#")[0]
    print("Location removed for " + ctx.author.name)
    await ctx.send("Location removed for " + ctx.author.name)

bot.run(TOKEN)
