import asyncio
import os
import time
from asyncio import sleep
from itertools import cycle

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()

BOTTOKEN = os.getenv("BOTTOKEN")

intents = discord.Intents.all() #Intents are so we can use so so many different commands and events in discord. It gives us acess to these events
intents.members = True
client = commands.Bot(command_prefix = "-", intents=intents, help_command=None) 
status = cycle(["Coded by: Latziks :)", "Hey! I see you!", "Use the -help command!", "JAMES BOT IS HERE", "Use the -help command to see all of the commands!", "JamesLee Twitch -> https://www.twitch.tv/jameslee85", "JamesLee YouTube -> https://www.youtube.com/channel/UCw3QUEX--77dy9T0_AVVFgg", " The 1st secret command is...", "-CommandFirst"])

@client.event                                           
async def on_ready():
    change_status.start()                           
    print("Hello! I am ready.\n------------------")

#When the bot is ready to function print that it is ready

@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))

#Next will be the set up of cogs

async def load():
    for filename in os.listdir("./cogs"): #For every file direction that ends with /cogs --->
        if filename.endswith(".py"):      # And if the file ends with .py
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main(): #This will load the load function!
    await load()
    await client.start(BOTTOKEN)

asyncio.run(main())