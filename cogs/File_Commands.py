import random

import discord
from discord.ext import commands

from answers import *


class File_Commmands(commands.Cog):
 
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def clone(self, ctx): 
        picked_clone = random.choice(clones)
        await ctx.send(file = discord.File(picked_clone))
        if picked_clone == "JamesAOD.gif":
            await ctx.send("This is AOD_Gaming also known as James' secret brother also, also known as clone number 1\nAOD has actually reunited as brothers one time! He is very, very epic! He streams on twitch and uploads on YouTube! Give him a follow on twitch!\nhttps://www.twitch.tv/aod_gaming_")                  
        if picked_clone == "JamesAndong.gif":
            await ctx.send("This is My Name Is Andong! He is clone number 2 and the most accurate clone! He is identical to James! He makes youtube videos about food!\n Here is his channel: https://www.youtube.com/c/mynameisandong")
        if picked_clone == "JamesActor.gif":
            await ctx.send("This is a strange picture of Jonah Hill! He is an American actor!")
        if picked_clone == "JamesStock.gif":
            await ctx.send("This is a random stock photo of one of James' clones! It is unclear if the man in the stock photo is a clone or actually James!")
        if picked_clone == "JamesNothingHere.gif":
            await ctx.send("This will never happen so you have found the secret command! The secret command is -not_so_secret_now !!!") #Nothing to see here! :)
async def setup(client):
    await client.add_cog(File_Commmands(client))