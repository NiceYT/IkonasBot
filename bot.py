import discord
import asyncio
import random
from discord.ext import commands

import os

prefix = "!"


client = discord.Client()





@client.event
async def on_ready():
    print("Я включен")

            






        
                  

@client.event
async def on_message(message):
    
            
    if message.content == client.user.mention:
        await message.channel.send(f'Мой префикс: `{prefix}`\nПример использования команд: `{prefix}help`')

    if not message.content.startswith(prefix) or message.author.bot: return
    args = message.content.split(' ')
    command = args[0][len(prefix):].lower()
    args = args[1:]
    
    

    

        
    
        
    

    

    

    
    if command == "case":
        case_role = discord.utils.get(message.guild.roles, name= "Кейс")
        if case_role in message.author.roles:
            ctx = message.mentions[0] if (message.mentions) else message.author
            user = message.author
        
        
         

            case_num = (random.randint(101,601))
            if case_num <= 101:
                Win = "10 робуксов"
                win1 = discord.utils.get(message.guild.roles, name="10 робуксов")
                await user.add_roles(win1)
            elif case_num <= 201:
                win2 = discord.utils.get(message.guild.roles, name="Сигна")
                Win = "Сигна от иконаса"
                await user.add_roles(win2)
            elif case_num <= 301:
                win3 = discord.utils.get(message.guild.roles, name="Добавление в друзья")
                Win = "Добавление в друзья к иконасу"
                await user.add_roles(win3)
            elif case_num <= 401:
                win4 = discord.utils.get(message.guild.roles, name="Выбор роли")
                Win = "Выбор роли"
                await user.add_roles(win4)
            elif case_num <= 501:
                channel = client.get_channel(int(597755853625491465))
                Win = "15000 ананасов"
                await channel.send("Тест")
            elif case_num <= 601:
                win5 = discord.utils.get(message.guild.roles, name="Личная комната")
                Win = "Личная голосовая комната"
                await user.add_roles(win5)
            await ctx.send("Вы выиграли:" + str(Win))
            emb = discord.Embed(title= "Число:" + str(case_num), colour= 0x2bbdf3)
            emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
            await message.channel.send(embed= emb)
            await asyncio.sleep(5)
            case1 = discord.utils.get(message.guild.roles, name="Кейс")
            await user.remove_roles(case1)
        else:
            return
        

    
    if command  == "спам":
        if message.author.guild_permissions.manage_messages:
            pass 
        else:
            return await message.channel.send("У вас нету прав!")
        ctx = message.mentions[0] if (message.mentions) else message.author
        
        gg = 1
        while gg == 1:
            await ctx.send("СПАМ")
            
    if command  == "Спам":
        if message.author.guild_permissions.manage_messages:
            gg = 1
            while gg == 1:
                await message.channel.send("СПАМ")
        
        else:
            return await message.channel.send("У вас нету прав!")
        
        
        
        

    
    
       
        
    
        


    






token = os.environ.get("BOT_TOKEN")

client.run(str(token))


