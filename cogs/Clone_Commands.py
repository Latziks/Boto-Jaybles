import discord
from discord.ext import commands

from answers import *


class Clone_Commmands(commands.Cog):
 
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def clone1(self, ctx): 
        await ctx.send(file = discord.File("JamesAOD.gif"))
    @commands.command()

    async def clone2(self, ctx): 
        await ctx.send(file = discord.File("JamesAndong.gif"))
    @commands.command()

    async def clone3(self, ctx): 
        await ctx.send(file = discord.File("JamesActor.gif"))

    @commands.command()
    async def clone4(self, ctx): 
        await ctx.send(file = discord.File("JamesStock.gif"))
    
    @commands.command()
    async def clone5(self, ctx): 
        await ctx.send(file = discord.File("JamesYTClone.gif"))

async def setup(client):
    await client.add_cog(Clone_Commmands(client))