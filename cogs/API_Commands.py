import json
import os

import discord
import requests
from discord.ext import commands

from answers import *

#Are you looking for the 2nd command? 

class API_Commands(commands.Cog): 

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def dadjoke(self, ctx):

        DAD_JOKE_KEY = os.getenv("DAD_JOKE_KEY")

        dadjokeurl = "https://daddyjokes.p.rapidapi.com/random"

        headers = {
            "X-RapidAPI-Key": DAD_JOKE_KEY,
            "X-RapidAPI-Host": "daddyjokes.p.rapidapi.com"
        }

        response = requests.request("GET", dadjokeurl, headers=headers)

        await ctx.send(json.loads(response.text)["joke"])

 
async def setup(client):
    await client.add_cog(API_Commands(client)) #Adds the cog in the bot.