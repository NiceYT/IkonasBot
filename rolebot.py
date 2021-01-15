import discord
import random
import pymongo
from pymongo import MongoClient
import asyncio
from discord.ext import commands
from config import token, configs, db_pass
import os

client = commands.Bot(command_prefix="!")

client.remove_command("help")
@client.event
async def on_ready():
    print("Я ебал рот, поэтому включился")
    game = discord.Game(f'Bot by Nice. | {configs["version"]} | {configs["prefix"]}')    
    await client.change_presence(status=discord.Status.online, activity=game)

for i in configs["Cogs"]:
    try:
        client.load_extension(i)
    except Exception as e:
        print(f'{i} cannot be loaded {e}')
    else:
        print(f"{i.replace('cogs.', '')} has been loaded!")
@client.event
async def on_message(message):
        try:
            if message.guild.id == 791649735727251487 or message.guild.id == 751786385781817423:
                await client.process_commands(message)
                stats_system = MongoClient(db_pass)
                db = stats_system["StatsSystem"]
                collection = db["Rolls"]
                results = collection.find_one({"Working": True})
                results = results["Status"]
                if results == True:
                    pass
                elif results == False:
                    if message.content.startswith("!d"):
                        return
                    else: 
                        pass
        except AttributeError:
            pass
            

client.run(str(token))
