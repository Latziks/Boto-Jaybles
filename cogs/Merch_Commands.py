import discord
from discord.ext import commands

from answers import *


class Merch_Commmands(commands.Cog):
 
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def merch1(self, ctx): 
        await ctx.send(file = discord.File("merch1.jpg"))
    
    @commands.command()
    async def merch2(self, ctx): 
        await ctx.send(file = discord.File("merch2.JPG"))

    @commands.command()
    async def merch3(self, ctx): 
        await ctx.send(file = discord.File("merch3.JPG"))

    @commands.command()
    async def merch4(self, ctx): 
        await ctx.send(file = discord.File("merch4.JPG"))
    
    @commands.command()
    async def merch5(self, ctx): 
        await ctx.send(file = discord.File("merch5.JPG"))

    @commands.command()
    async def merch6(self, ctx): 
        await ctx.send(file = discord.File("merch6.JPG"))
    
    @commands.command()
    async def merch7(self, ctx): 
        await ctx.send(file = discord.File("merch7.JPG"))

    @commands.command()
    async def merch8(self, ctx): 
        await ctx.send(file = discord.File("merch8.JPG"))
    
    @commands.command()
    async def merch9(self, ctx): 
        await ctx.send(file = discord.File("merch9.JPG"))

    @commands.command()
    async def merch10(self, ctx): 
        await ctx.send(file = discord.File("merch10.JPG"))
    
async def setup(client):
    await client.add_cog(Merch_Commmands(client))