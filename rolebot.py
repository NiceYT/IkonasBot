import discord
import random
import pymongo
from pymongo import MongoClient
import asyncio
from discord.ext import commands
from config import *
import os
db_pass = os.environ.get("DB_pass")
db_pass = str(db_pass)

client = commands.Bot(command_prefix="-")

client.remove_command("help")
@client.event
async def on_ready():
    channel = client.get_channel(532573322014359552)
    await channel.send("1")
    print("Я включен")
    game = discord.Game(f"Bot by Nice. | {version} | {prefix2}")    
    await client.change_presence(status=discord.Status.online, activity=game)
@client.command()
async def addrole(ctx, member: discord.Member, time: int, role1: discord.Role, role2: discord.Role):
    if ctx.message.author.id == 759670745440976916 or ctx.message.author.id == 361179719800061963:
        if time < 60:
            time = time * 60
            timer = 0
            role_system = MongoClient(db_pass)
            db = role_system["RoleSystem"]
            collection = db["Timer"] 
            collection.insert_one({"timer": timer, "time": time, "member": member.id, "role1": role1.id, "role2": role2.id, "role": True, "guild": ctx.guild.id})
            while timer != time:
                await asyncio.sleep(1)
                timer += 1
                collection.find_one_and_update({"time": time}, {"$set":{"timer": timer}})
                if timer == time:
                    collection.find_one_and_delete({"time": time})
                    await member.add_roles(role1)
                    await member.remove_roles(role2)
                    await ctx.send("Успешно!")
        elif time > 60:
            error_embed = discord.Embed(title="Ошибка!", description=f"Вы ввели время({time}), которое больше чем максимальное.", color=random.choice(normal_list))
            await ctx.send(embed=error_embed)

@client.event
async def on_message(msg):
    if msg.author.id == 601472872346550287:
        if msg.content == "1":
            role_system = MongoClient(db_pass)
            db = role_system["RoleSystem"]
            collection = db["Timer"]
            results = collection.find_one({"role": True})
            timer = int(results["timer"])
            time = int(results["time"])
            member = int(results["member"])
            role1 = int(results["role1"])
            role2 = int(results["role2"])
            guild = int(results["guild"])
            member = client.get_guild(guild).get_member(member)
            role1 = client.get_guild(guild).get_role(role1)
            role2 = client.get_guild(guild).get_role(role2)
            while timer != time:
                await asyncio.sleep(1)
                timer += 1
                collection.find_one_and_update({"time": time}, {"$set":{"timer": timer}})
                if timer == time:
                    collection.find_one_and_delete({"time": time})
                    await member.add_roles(role1)
                    await member.remove_roles(role2)
                    await msg.channel.send("Успешно!")
    await client.process_commands(msg)
token = os.environ.get("token")
client.run(str(token))
