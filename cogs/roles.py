import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
from config import clr, db_pass
import asyncio
import random

class roleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=["ad", "ar"])
    async def addrole(self, ctx, member: discord.Member, time: int, role2: discord.Role, role1: discord.Role = None):
        if ctx.message.author.id == 503981176806178816 or ctx.message.author.id == 361179719800061963 or ctx.message.author.id == 264081734264422400:
            if time < 60:
                if role1 != None:
                        time = time * 60
                        timer = 0
                        role_system = MongoClient(db_pass)
                        db = role_system["RoleSystem"]
                        collection = db["Timer"] 
                        collection.insert_one({"timer": timer, "time": time, "member": member.id, "role2": role2.id, "role1": role1.id, "role": True, "guild": ctx.guild.id})
                        succes_embed = discord.Embed(title="Успешно!", description=f"Вы ввели время({time} секунд), через которое будет выдана роль.", color=random.choice(clr))
                        await ctx.send(embed=succes_embed)
                        while timer != time:
                            await asyncio.sleep(1)
                            timer += 1
                            collection.find_one_and_update({"time": time}, {"$set":{"timer": timer}})
                            if timer == time:
                                collection.find_one_and_delete({"time": time})
                                await member.add_roles(role2)
                                await ctx.send(f"Роль была выдана {member.mention}.")
                                await member.remove_roles(role1)
                if role1 == None:
                        time = time * 60
                        timer = 0
                        role_system = MongoClient(db_pass)
                        db = role_system["RoleSystem"]
                        collection = db["Timer"] 
                        collection.insert_one({"timer": timer, "time": time, "member": member.id, "role2": role2.id, "role1": "empty", "role": True, "guild": ctx.guild.id})
                        succes_embed = discord.Embed(title="Успешно!", description=f"Вы ввели время({time} секунд), через которое будет выдана роль.", color=random.choice(clr))
                        await ctx.send(embed=succes_embed)
                        while timer != time:
                            await asyncio.sleep(1)
                            timer += 1
                            collection.find_one_and_update({"time": time}, {"$set":{"timer": timer}})
                            if timer == time:
                                collection.find_one_and_delete({"time": time})
                                for role in member.roles[1:]:
                                    try:
                                        await member.remove_roles(role)
                                    except discord.errors.Forbidden:
                                        pass
                                await member.add_roles(role2)
                                await ctx.send(f"Роль была выдана {member.mention}.")              
            elif time > 60:
                error_embed = discord.Embed(title="Ошибка!", description=f"Вы ввели время({time} минут), которое больше чем максимальное.", color=random.choice(clr))
                await ctx.send(embed=error_embed)
def setup(bot):
    bot.add_cog(roleCog(bot))
