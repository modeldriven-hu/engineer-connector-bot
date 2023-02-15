import os

# https://www.geeksforgeeks.org/building-a-discord-bot-in-python/

import discord
from discord.ext.commands import Context
from dotenv import load_dotenv
from discord.ext import commands

def string_cleaner(argument):
    '''This function will remove certain characters from a string'''
    blocked_characters =  [',', '.']
    for character in blocked_characters:
        argument = argument.replace(character, '')
    return argument

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.command(name="ping", help="Pings the bot")  # for debugging purpose
async def ping(ctx: Context):
    username = str(ctx.author).split("#")[0]
    print(f'Pinged by {username}')
    await ctx.send('Pong!')

@bot.command(name="set_location", help="Set the location: !set_location city country")
async def set_location(ctx: Context, city="Helm's Deep", country="Rohan"):
    command = ctx.message.clean_content
    print(ctx.current_argument)
    print(ctx.current_parameter)
    username = str(ctx.author).split("#")[0]
    city = string_cleaner(city)
    country = string_cleaner(country)
    print("Location for user " + ctx.author.name + " set to " + city + ", " + country)
    await ctx.send("Location for user " + ctx.author.name + " set to " + city + ", " + country + " :map::earth_africa::partying_face:" ) 

@bot.command(name="remove_location", help="Remove the location")
async def remove_location(ctx: Context):
    username = str(ctx.author).split("#")[0]
    print("Location removed for " + ctx.author.name)
    await ctx.send("Location removed for " + ctx.author.name + " :ninja:")

@bot.command(name="set_favourite_drink", help="Specify your favourite drink")
async def set_location(ctx: Context, drink="Beer"):
    print(ctx.current_argument)
    print(ctx.current_parameter)
    drink = string_cleaner(drink)
    print("User " + ctx.author.name + " set favourite drink to " + drink)
    await ctx.send("User " + ctx.author.name + " set favourite drink to " + drink + " :beer:" )

bot.run(TOKEN)
