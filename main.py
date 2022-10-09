import discord
import asyncio
import os
from apikeys import BOTTOKEN 
from discord.ext import commands

intents = discord.Intents.all() #Intents are so we can use so so many different commands and events in discord. It gives us acess to these events
intents.members = True
client = commands.Bot(command_prefix = "-", intents=intents) 

@client.event                                           
async def on_ready():                                   
   print("Hello! I am ready.\n------------------")
   #When the bot is ready to function print that it is ready

#Next will be the set up of cogs

async def load():
    for filename in os.listdir("./cogs"): #For every file direction that ends with /cogs --->
        if filename.endswith(".py"):      # And if the file ends with .py
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main(): #This will load the load function!
    await load()
    await client.start(BOTTOKEN)

asyncio.run(main()) #Do the main function!