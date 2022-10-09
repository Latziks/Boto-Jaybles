import discord
import random
import requests
import json
import os
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from answers import *

#Sadly in cogs --->
#@client.commands() = @commands.command() and
#@client.event = @commands.cog.listener()

class Normal_Commmands(commands.Cog): #The class always has to be called like the file name!
 
    def __init__(self, client): #The __init__ method lets the class initialize the object's attributes. Initialize means to set a value!
        self.client = client
    
    @commands.command()
    async def hello(self, ctx): #In every function that is in a cog there needs to be a self!
        picked_hello_answer = random.choice(hello_answer)
        await ctx.send(f"{picked_hello_answer} {ctx.message.author}"[:-5] + "!")
    
    
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

    @commands.command()
    async def randomclip(self, ctx):
        clips = open("clips.txt").readlines()

        picked_clip = random.choice(clips)
        picked_randomclip_answer = random.choice(randomclip_anwer)
        await ctx.send(f"{picked_randomclip_answer}\n{picked_clip}")

    @commands.command()
    @has_permissions(kick_members=True)
    async def addclip(self, ctx, url: str):
        clips = open("clips.txt").readlines()

        if url in clips:
            picked_addclips_already_in_answer = random.choice(addclips_already_in_answer)
            await ctx.send(picked_addclips_already_in_answer)
            print(clips)
        else: 
            if not url.startswith("https://clips.twitch.tv/"):
                picked_addclips_not_twitch_answer = random.choice(addclips_not_twitch_answer)
                await ctx.send(picked_addclips_not_twitch_answer)
                print(clips)
            else:
                picked_addclips_added_clip = random.choice(addclips_added_clip)
                file = open("clips.txt", "a")
                file.write(f"\n{url}")
                file.close()
                await ctx.send(picked_addclips_added_clip)
                print(clips)
    
    @addclip.error
    async def addclip_error(self, ctx, error): 
        if isinstance(error, MissingPermissions):
            picked_addclips_no_permissions = random.choice(addclips_no_permissions)
            await ctx.send(picked_addclips_no_permissions)

async def setup(client):
    await client.add_cog(Normal_Commmands(client)) #Adds the cog in the bot.