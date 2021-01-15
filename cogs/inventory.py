import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import random
from config import clr, db_pass
class InventoryCog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command(aliases=["inv"])
    async def inventory(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.message.author.send("")
        elif member != None and ctx.message.author.id == 361179719800061963 or member != None and ctx.message.author.id == 264081734264422400:
            pass
def setup(bot):
    bot.add_cog(InventoryCog(bot))