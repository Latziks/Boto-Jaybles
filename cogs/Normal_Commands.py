import random

import discord
import randfacts
from discord.ext import commands

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
    async def randomclip(self, ctx):
        picked_clip = random.choice(clips)
        picked_randomclip_answer = random.choice(randomclip_anwer)
        await ctx.send(f"{picked_randomclip_answer}\n{picked_clip}")
    
    @commands.command()
    async def what_does_james_think_of_me(self, ctx):
        picked_emotion = random.choice(what_does_james_think_of_me_answer)
        await ctx.send(picked_emotion)

    @commands.command()
    async def funfact(self, ctx):
        fun_fact_get = randfacts.get_fact()
        await ctx.send(fun_fact_get)#This is so easy!
    
async def setup(client):
    await client.add_cog(Normal_Commmands(client)) #Adds the cog in the bot.