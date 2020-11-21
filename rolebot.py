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

client = commands.Bot(command_prefix="!")

client.remove_command("help")
@client.event
async def on_ready():
    channel = client.get_channel(532573322014359552)
    await channel.send("1")
    print("Я включен")
    game = discord.Game(f"Bot by Nice. | {version} | {prefix2}")    
    await client.change_presence(status=discord.Status.online, activity=game)
@client.command()
async def addrole(ctx, member: discord.Member, time: int, role2: discord.Role, role1: discord.Role = None):
    if ctx.message.author.id == 503981176806178816 or ctx.message.author.id == 361179719800061963 or ctx.message.author.id == 264081734264422400:
        if time < 60:
            if role1 != None:
                time = time * 60
                timer = 0
                role_system = MongoClient(db_pass)
                db = role_system["RoleSystem"]
                collection = db["Timer"] 
                collection.insert_one({"timer": timer, "time": time, "member": member.id, "role2": role2.id, "role1": role1.id, "role": True, "guild": ctx.guild.id})
                succes_embed = discord.Embed(title="Успешно!", description=f"Вы ввели время({time} секунд), через которое будет выдана роль..", color=random.choice(normal_list))
                await ctx.send(embed=succes_embed)
                while timer != time:
                    await asyncio.sleep(1)
                    timer += 1
                    collection.find_one_and_update({"time": time}, {"$set":{"timer": timer}})
                    if timer == time:
                        collection.find_one_and_delete({"time": time})
                        await member.add_roles(role2)
                        await member.remove_roles(role1)
                        await ctx.send(f"Роль была выдана, {ctx.message.author.mention}")
            if role1 == None:
                time = time * 60
                timer = 0
                role_system = MongoClient(db_pass)
                db = role_system["RoleSystem"]
                collection = db["Timer"] 
                collection.insert_one({"timer": timer, "time": time, "member": member.id, "role2": role2.id, "role1": "empty", "role": True, "guild": ctx.guild.id})
                succes_embed = discord.Embed(title="Успешно!", description=f"Вы ввели время({time} секунд), через которое будет выдана роль..", color=random.choice(normal_list))
                await ctx.send(embed=succes_embed)
                while timer != time:
                    await asyncio.sleep(1)
                    timer += 1
                    collection.find_one_and_update({"time": time}, {"$set":{"timer": timer}})
                    if timer == time:
                        collection.find_one_and_delete({"time": time})
                        await member.add_roles(role2)
                        for role in member.roles[1:]:
                            await member.remove_roles(role)
                        await ctx.send(f"Роль была выдана, {ctx.message.author.mention}")
        elif time > 60:
            error_embed = discord.Embed(title="Ошибка!", description=f"Вы ввели время({time} минут), которое больше чем максимальное.", color=random.choice(normal_list))
            await ctx.send(embed=error_embed)
@client.command()
async def create(ctx, member: discord.Member, name, type, colour, attention, speed, accuracy):
    if ctx.message.author.id == 264081734264422400 or ctx.message.author.id == 361179719800061963:
        stats_system = MongoClient(db_pass)
        db = stats_system["StatsSystem"]
        collection = db["Profiles"]
        collection.insert_one({"member": member, "name": name, "type": type, "colour": colour, "attention": attention, "speed": speed, "accuracy": accuracy})
        succes_embed = discord.Embed(title="Успешно!", description=f"Профиль участника {member} был создан.", color=random.choice(normal_list))
        await ctx.send(succes_embed)
        






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
            role1 = results["role1"]
            role2 = int(results["role2"])
            guild = int(results["guild"])
            if role1 == "empty":
                member = client.get_guild(guild).get_member(member)
                role2 = client.get_guild(guild).get_role(role2)
                while timer != time:
                    await asyncio.sleep(1)
                    timer += 1
                    collection.find_one_and_update({"time": time}, {"$set":{"timer": timer}})
                    if timer == time:
                        collection.find_one_and_delete({"time": time})
                        await member.add_roles(role2)
                        for role in member.roles[1:]:
                            await member.remove_roles(role)
                        await msg.channel.send("Роль была выдана.")
            else:
                try:
                    member = client.get_guild(guild).get_member(member)
                    role1 = client.get_guild(guild).get_role(role1)
                    role2 = client.get_guild(guild).get_role(role2)
                    while timer != time:
                        await asyncio.sleep(1)
                        timer += 1
                        collection.find_one_and_update({"time": time}, {"$set":{"timer": timer}})
                        if timer == time:
                            collection.find_one_and_delete({"time": time})
                            await member.add_roles(role2)
                            await member.remove_roles(role1)
                            await msg.channel.send("Роль была выдана.")
                except:
                    pass
    await client.process_commands(msg)
token = os.environ.get("token")
client.run(str(token))
