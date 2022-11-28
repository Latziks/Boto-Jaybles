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
        embed.add_field(name = "-dadjoke", value = "Boto Jaybles tells you a VERY 'funny' dad joke!", inline = False)
        embed.add_field(name = "-randomclip", value = "Boto Jaybles sends you a random JamesLee85 Twitch clip!", inline = False)
        embed.add_field(name = "-what_does_james_think_of_me", value = "Boto Jaybles tells you what James Lee really thinks about you!", inline = False)
        embed.add_field(name = "-funfact", value = "Boto Jaybles sends you an actually fun fact! This has not been influenced by Latziks!", inline = False)
        embed.add_field(name = "-clone", value = "Boto Jaybles sends one of the 5 clones of James Lee! If you want to see all of the James' clones you can just do -clone1; -clone2; -clone3; -clone4; -clone5", inline = False)
        embed.add_field(name = "-secrets", value = "This will tell you everything about the secret commands!", inline = False)
        embed.add_field(name = "-github", value = "Boto Jaybles sends you his GitHub link!", inline = False)
        embed.add_field(name = "-merch", value = "Boto Jaybles sends you a random picture of JamesLee85 merch! If you want to see all James Lee merch pictures you can just do -merch1; -merch2; -merch3; -merch4; -merch5; -merch6; -merch7; -merch8; -merch9; -merch10", inline = False)
        embed.add_field(name = "-spam", value = "No questions asked!", inline = False)
        embed.add_field(name = "-thug", value = "In honour of the removed thug command, Boto Jaybles sends you a picture of 'thuged' James!", inline = False)
        embed.add_field(name = "-silence", value = "Boto Jaybles silences/stops the conversation you are having!", inline = False)
        embed.add_field(name = "-yesorno", value = "Boto Jaybles decides your faith!", inline = False)
        await ctx.send(embed = embed)
    
    @commands.command()
    async def github(self, ctx):
        picked_github_answer = random.choice(github_answer)
        await ctx.send(picked_github_answer)
        await ctx.send("https://github.com/Latziks/Boto-Jaybles")

    @commands.command()
    async def secrets(self, ctx):
        await ctx.send("So you want to know the 3 secret commands! I'll give you some clues! So one of the command is actually hidden in the source code! You'll have to use -github to see my source code! (NO LATZIKS' IS NOT THAT STUPID AND DID NOT ADD ALL 3 SECRET COMMANDS ON GITHUB), then there is -lottery! It's a 1 in 10000 chance to get a secret message! Then there is a completely secret command! Good luck!\n\nUPDATE: These 3 commands have been found by Grenter and Berry!\n\nThe secret commands were:\n\n-lottery (The secret answer was 'So you my friend have done it! You have gambled for a long time and got here! You are a legend! So what is this about? Well, I just wanted to say that JamesLee is epic and thank you for the quality content! You are very underrated! And you viewers are better! { The one who won } you are the part of the gang! Remember that! Congrats!')\n\n-not_so_secret_now\n\n-subway\n\nThere are now 5 new secret commands! Each command will give a hint to the next command in order. I'm sorry but this will be a long journey!\n\nThe hint for the first command is...look at Boto Jaybles at the right sidebar...just look at it and see what he's trying to tell you!")
       
async def setup(client):
    await client.add_cog(Info_Commmands(client))