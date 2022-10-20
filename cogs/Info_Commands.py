import random

import discord
from discord.ext import commands

from answers import *


class Info_Commmands(commands.Cog):
 
    def __init__(self, client):
        self.client = client
    
    @commands.command(name = "help")
    async def help(self, ctx): 
        embed = discord.Embed(colour = discord.Colour.purple())
        embed.set_author(name = "Commands")
        embed.add_field(name = "-hello", value = "Boto Jaybles says hello to you!", inline = False)
        embed.add_field(name = "-dadjoke", value = "Boto Jaybles tells you a VERY 'funny' dad joke to you!", inline = False)
        embed.add_field(name = "-randomclip", value = "Boto Jaybles tells you what James Lee really thinks about you!", inline = False)
        embed.add_field(name = "-what_does_james_think_of_me", value = "Boto Jaybles sends you an actually fun fact! This has not been influenced by Latziks!", inline = False)
        embed.add_field(name = "-funfact", value = "Boto Jaybles sends you an actually fun fact! This has not been influenced by Latziks!", inline = False)
        embed.add_field(name = "-clone", value = "Boto Jaybles sends one of the 4 clones of James! If you want to see all of the James clones you are going to send this command multiple times OR just do -clone1; -clone2; -clone3; -clone4", inline = False)
        embed.add_field(name = "-secrets", value = "This will tell you everything about 3 secret commands!", inline = False)
        embed.add_field(name = "-github", value = "Boto Jaybles sends you his GitHub link!", inline = False)
        await ctx.send(embed = embed)
    
    @commands.command()
    async def github(self, ctx):
        picked_github_answer = random.choice(github_answer)
        await ctx.send(picked_github_answer)
        await ctx.send("https://github.com/Latziks/Boto-Jaybles")

    @commands.command()
    async def secrets(self, ctx):
        await ctx.send("So you want to know the 3 secret commands! I'll give you some clues! So one of the commands is actually hidden in the source code! You'll have to use -github to see my source code! (NO LATZIKS' IS NOT THAT STUPID AND DID NOT ADD ALL 3 SECRET COMMANDS ON GITHUB), then there is -lottery! It's a 1 in 10000 chance to get a secret message! Then there is a completely secret message! Good luck!")
       
async def setup(client):
    await client.add_cog(Info_Commmands(client))