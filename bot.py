import discord
import asyncio
import random
from discord.ext import commands
import os


prefix = "."


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
            user = message.author
            channel3 = client.get_channel(int(605289537287094272)
           
        
        
         

            case_num = (random.randint(1,601))
            if case_num <= 101:
                channel1 = client.get_channel(int(605289537287094272))
                win1 = discord.utils.get(message.guild.roles, name="10 робуксов")
                if win1 in message.author.roles:
                    await channel1.send("Участнику {} выпал повторный приз 10 робуксов".format(message.author))
                    return
                else:
                    Win = "10 робуксов"
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win1)
            elif case_num <= 201:
                win2 = discord.utils.get(message.guild.roles, name="Сигна")
                if win2 in message.author.roles:
                    await message.channel.send("Вам выпала повторная роль! Введите команду заново!")
                    return
                else:
                    Win = "Сигна от иконаса"
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win2)
            elif case_num <= 301:
                win3 = discord.utils.get(message.guild.roles, name="Добавление в друзья")
                if win3 in message.author.roles:
                    await message.channel.send("Вам выпала повторная роль! Введите команду заново!")
                    return
                else:
                    Win = "Добавление в друзья к иконасу"
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win3)
            elif case_num <= 401:
                win4 = discord.utils.get(message.guild.roles, name="Выбор роли")
                if win4 in message.author.roles:
                    await message.channel.send("Вам выпала повторная роль! Введите команду заново!")
                    return
                else:
                    Win = "Выбор роли"
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win4)
            elif case_num <= 501:
                channel2 = client.get_channel(int(532573322014359552))
                Win = "15000 ананасов"
                await channel2.send("=add-money {} 15000".format(message.author))
            elif case_num <= 601:
                win5 = discord.utils.get(message.guild.roles, name="Личная комната")
                if win5 in message.author.roles:
                    await message.channel.send("Вам выпала повторная роль! Введите команду заново!")
                    return
                else:
                    Win = "Личная голосовая комната"
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win5)
            emb = discord.Embed(title= "Число:" + str(case_num), colour= 0x2bbdf3)
            emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
            await message.channel.send(embed= emb)
            await asyncio.sleep(5)
            case1 = discord.utils.get(message.guild.roles, name="Кейс")
            await user.remove_roles(case1)
        else:
            return
                

token = os.environ.get("BOT_TOKEN")
client.run(str(token))
