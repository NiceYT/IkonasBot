import discord
import asyncio
import random 
import datetime 
from discord.ext import commands
import os


prefix = "."


client = discord.Client()





@client.event
async def on_ready():
    print("Я включен")

            




        
                  

@client.event
async def on_message(message):
    args = message.content.split(' ')
    command = args[0][len(prefix):].lower()
    args = args[1:]
    if message.guild == None:
        timeRU = datetime.now() 
        channel = client.get_channel(532573322014359552) 
        emb = discord.Embed(title = message.author.name, description = message.content + str(TimeRU), color= 0xff0404)
        await channel.send(embed=emb)
        
        
    
    

    

        
    
        
    

    

    

    
    if command == "case":
        case_role = discord.utils.get(message.guild.roles, name= "Кейс")
        if case_role in message.author.roles:
            user = message.author
            case_num = (random.randint(1,601))
            channel3 = client.get_channel(int(605289537287094272))
            

            if case_num <= 101:
                channel1 = client.get_channel(int(605289537287094272))
                win1 = discord.utils.get(message.guild.roles, name="10 робуксов")
                if win1 in message.author.roles:
                    await message.channel.send("Вам выпал повторный приз 10 робуксов! Поздравляю!")
                    emb = discord.Embed(title= "Повторный выиграш 10 робуксов", colour = 0xff0404 )
                    emb.add_field(name= "Участнику {} выпал повторный приз 10 робуксов".format(message.author), value= f"Иконас выдай робуксы {message.author}")
                    await channel1.send(embed= emb)
                else:
                    Win = "10 робуксов"
                    emb = discord.Embed(title= "10 робуксов", colour = 0xff0404)
                    emb.add_field(name= f"{message.author} выиграл:" + str(Win), value= f"Иконас выдай робуксы {message.author}")
                    await channel3.send(embed= emb)
                    await user.add_roles(win1)
            elif case_num <= 201:
                win2 = discord.utils.get(message.guild.roles, name="Сигна")
                if win2 in message.author.roles:
                    await message.channel.send("Вам выпала повторная роль! Введите команду заново!")
                    return
                else:
                    Win = "Сигна от иконаса"
                    emb = discord.Embed(title= "Число:" + str(case_num), colour= 0x2bbdf3)
                    emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                    await message.channel.send(embed= emb)
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win2)
            elif case_num <= 301:
                win3 = discord.utils.get(message.guild.roles, name="Добавление в друзья")
                if win3 in message.author.roles:
                    await message.channel.send("Вам выпала повторная роль! Введите команду заново!")
                    return
                else:
                    Win = "Добавление в друзья к иконасу"
                    emb = discord.Embed(title= "Число:" + str(case_num), colour= 0x2bbdf3)
                    emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                    await message.channel.send(embed= emb)
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win3)
            elif case_num <= 401:
                win4 = discord.utils.get(message.guild.roles, name="Выбор роли")
                if win4 in message.author.roles:
                    await message.channel.send("Вам выпала повторная роль! Введите команду заново!")
                    return
                else:
                    Win = "Выбор роли"
                    emb = discord.Embed(title= "Число:" + str(case_num), colour= 0x2bbdf3)
                    emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                    await message.channel.send(embed= emb)
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win4)
            elif case_num <= 501:
                channel2 = client.get_channel(int(532573322014359552))
                Win = "15000 ананасов"
                emb = discord.Embed(title= "Число:" + str(case_num), colour= 0x2bbdf3)
                emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                await message.channel.send(embed= emb)
                await channel2.send(f"=add-money @{message.author} 15000")
            elif case_num <= 601:
                win5 = discord.utils.get(message.guild.roles, name="Личная комната")
                if win5 in message.author.roles:
                    await message.channel.send("Вам выпала повторная роль! Введите команду заново!")
                    return
                else:
                    Win = "Личная голосовая комната"
                    emb = discord.Embed(title= "Число:" + str(case_num), colour= 0x2bbdf3)
                    emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                    await message.channel.send(embed= emb)
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win5)
            await asyncio.sleep(5)
            case1 = discord.utils.get(message.guild.roles, name="Кейс")
            await user.remove_roles(case1)
        else:
            return
                

token = os.environ.get("BOT_TOKEN")
client.run(str(token))
