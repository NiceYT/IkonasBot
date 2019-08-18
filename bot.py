import discord
import asyncio
import random
import pytz
from datetime import datetime 
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '.')
prefix = "."






@client.event
async def on_ready():
    print("Я включен")
    

blacklist = []
    



@client.command()
@commands.has_any_role(532444048166748170, 532444461985300481)
async def block(ctx, id):
    blacklist.append(int(id))
    emb = discord.Embed(title=f"Вы заблокировали пользователя ", description = f"Айди человека: {id}", color= 0xee4426)
    await ctx.send(embed=emb)
@client.command()
@commands.has_any_role(532444048166748170, 532444461985300481)
async def unblock(ctx, id):
    blacklist.remove(int(id))
    emb = discord.Embed(title=f"Вы Разблокировали пользователя", description = f"Айди человека: {id}", color= 0xee4426)
    await ctx.send(embed=emb)

@client.command()
@commands.has_any_role(532444048166748170, 532444461985300481)
async def blocked(ctx):
    emb = discord.Embed(title="Список заблокированных людей", description = f"{blacklist}",  color= 0xee4426)
    await ctx.send(embed=emb)
               

@client.event
async def on_message(message):
     
    args = message.content.split(' ')
    command = args[0][len(prefix):].lower()
    args = args[1:]
        
        
    if message.guild == None:
        if message.author == bot.user:
            return
        else:
            if message.author.id in blacklist:
                blocked = message.author
                await blocked.send("Вы в черном списке этого сервера!")
            else:
                tz = pytz.timezone('Europe/Moscow')
                time_now = str(datetime.now(tz)).split(' ')[1][:8]
                channel = client.get_channel(532573322014359552) 
                emb = discord.Embed(title = str(message.author), description = message.content, color=0xff0404)
                emb.set_footer(icon_url = str(message.author.avatar_url),text= str(message.author.id) + " | " +str(time_now)) 

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
    await client.process_commands(message)
     
                

token = os.environ.get("BOT_TOKEN")
client.run(str(token))
