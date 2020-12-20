import discord
import random
import pymongo
from pymongo import MongoClient
import asyncio
from discord.ext import commands
from config import *
import os

client = commands.Bot(command_prefix="!")

client.remove_command("help")
@client.event
async def on_ready():
    channel = client.get_channel(532573322014359552)
    await channel.send("1")
    print("Я включен")
    game = discord.Game(f'Bot by Nice. | {configs["version"]} | {configs["prefix"]}')    
    await client.change_presence(status=discord.Status.online, activity=game)
for i in configs["Cogs"]:
    try:
        client.load_extension(i)
    except Exception as e:
        print(f'{i} cannot be loaded {e}')
    else:
        print(f"{i.replace('cogs.', '')} has been loaded!")

client.run(str(token))
