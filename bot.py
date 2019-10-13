import discord
import asyncio
import random
import pytz
import sqlite3
from datetime import datetime 
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '.')
prefix = "."
color_list = (discord.Color.red(),
                discord.Color.dark_red(),
                discord.Color.blue(),
                discord.Color.dark_blue(),
                discord.Color.teal(),
                discord.Color.dark_teal(),
                discord.Color.green(),
                discord.Color.dark_green(),
                discord.Color.purple(),
                discord.Color.dark_purple(),
                discord.Color.magenta(),
                discord.Color.dark_magenta(),
                discord.Color.gold(),
                discord.Color.dark_gold(),
                discord.Color.orange(),
                discord.Color.dark_orange()
                )




@client.event
async def on_ready():
    print("Я включен")
    


    
conn = sqlite3.connect("datebase.sqlite")
cursor = conn.cursor()
    
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS idbase (id text)''')
except:
    pass
    


@client.command()
@commands.has_any_role(532444048166748170, 532444461985300481)
async def block(ctx, member: discord.Member):
    id = member.id
    cursor.execute(f"INSERT INTO  idbase (id) VALUES ({id})")
    conn.commit()
    emb = discord.Embed(title=f"Вы заблокировали пользователя ", description = f"Айди человека: <@{id}>", color= random.choice(color_list))
    await ctx.send(embed=emb)
    await member.send(f"Вы были заблокированы на 24 часа администратором {ctx.message.author}")
@client.command()
@commands.has_any_role(532444048166748170, 532444461985300481)
async def unblock(ctx, member: discord.Member):
    id = member.id
    cursor.execute(f"DELETE FROM idbase WHERE id = {id}")
    conn.commit()
    emb = discord.Embed(title=f"Вы Разблокировали пользователя", description = f"Айди человека: <@{id}>", color= random.choice(color_list))
    await ctx.send(embed=emb)
    await member.send(f"Вы были разблокированы администратором {ctx.message.author}")

@client.command()
@commands.has_any_role(532444048166748170, 532444461985300481)
async def blocked(ctx):
    cursor.execute('SELECT * FROM idbase')
    row = cursor.fetchone()
    while row is not None:
        emb = discord.Embed(title= "Список заблокированных людей: ", description="\n".join([str(i) for i in row]),  color= random.choice(color_list))
        await ctx.send(embed=emb)
        row = cursor.fetchone()
@client.command()
@commands.has_any_role(532444048166748170, 532444461985300481)
async def answer(ctx, member: discord.Member, *, textAnswer):
    await member.send(embed=discord.Embed(title=f"Вы получили ответ от {ctx.message.author} ", description=textAnswer, color= random.choice(color_list)).set_footer(text=f"С уважением, {ctx.message.author}",icon_url=f"{ctx.message.author.avatar_url}"))
               

@client.event
async def on_message(message):
     
    args = message.content.split(' ')
    command = args[0][len(prefix):].lower()
    args = args[1:]
        
        
    if message.guild == None:
        if message.author == client.user:
            return
        else:
            cursor.execute('SELECT * FROM idbase')
            row = cursor.fetchone() 
            if str(message.author.id) in str(row):
                blocked = message.author
                await blocked.send("Вы в черном списке этого сервера!")
            else:
                tz = pytz.timezone('Europe/Moscow')
                time_now = str(datetime.now(tz)).split(' ')[1][:8]
                channel = client.get_channel(532573322014359552) 
                emb = discord.Embed(title = str(message.author), description = message.content, color= random.choice(color_list))
                emb.set_footer(icon_url = str(message.author.avatar_url),text= str(message.author.id) + " | " +str(time_now)) 

                await channel.send(embed=emb) 
        
        
    
    

    

        
    
        
    

    

    

    
    if command == "case":
        case_role = discord.utils.get(message.guild.roles, name= "Кейс")
        if case_role in message.author.roles:
            user = message.author
            case_num = (random.randint(1,601))
            channel3 = client.get_channel(int(605289537287094272))
            

            if case_num <= 101:
                
                win1 = discord.utils.get(message.guild.roles, name="10 робуксов")
                if win1 in message.author.roles:
                    Win = "10 робуксов"
                    embe= discord.Embed(title="Число:" + str(case_num), colour= random.choice(color_list))
                    embe.add_field(name="Вы выиграли повторный приз: " + str(Win), value = "Молодец!")
                    await message.channel.send(embed=embe)
                    emb = discord.Embed(title= "Повторный выиграш 10 робуксов", colour =random.choice(color_list) )
                    emb.add_field(name= "Участнику {} выпал повторный приз 10 робуксов".format(message.author), value= f"Иконас выдай робуксы {message.author}")
                    await channel3.send(embed= emb)
                else:
                    Win = "10 робуксов"
                    embe= discord.Embed(title="Число:" + str(case_num), color= random.choice(color_list))
                    embe.add_field(name="Вы выиграли приз: " + str(Win), value = "Молодец!")
                    await message.channel.send(embed=embe)
                    emb = discord.Embed(title= "10 робуксов", color= random.choice(color_list))
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
                    emb = discord.Embed(title= "Число:" + str(case_num), color= random.choice(color_list))
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
                    emb = discord.Embed(title= "Число:" + str(case_num), colour= random.choice(color_list))
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
                    emb = discord.Embed(title= "Число:" + str(case_num), color= random.choice(color_list))
                    emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                    await message.channel.send(embed= emb)
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win4)
            elif case_num <= 501:
                channel2 = client.get_channel(int(532573322014359552))
                Win = "15000 ананасов"
                emb = discord.Embed(title= "Число:" + str(case_num), color= random.choice(color_list))
                emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                await message.channel.send(embed= emb)
                await channel2.send(f"=add-money {message.author.id} 15000")
            elif case_num <= 601:
                win5 = discord.utils.get(message.guild.roles, name="Личная комната")
                if win5 in message.author.roles:
                    await message.channel.send("Вам выпала повторная роль! Введите команду заново!")
                    return
                else:
                    Win = "Личная голосовая комната"
                    emb = discord.Embed(title= "Число:" + str(case_num), color= random.choice(color_list))
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
