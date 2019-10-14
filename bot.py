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
normal_list = (discord.Color.red(),
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
spooky_list = (0xFFA500,
               0xFF8C00,
               0xFF4500,
               0xFF6347,
               0xFF7F50,
               0xFFA07A,
               0xFFFF00,
               0xFFD700,
               0xFFDAB9,
               0x8B4513,
               0xA52A2A,
               0xA0522D,
               0xD2691E,
               0xB8860B)
clr = spooky_list


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
    emb = discord.Embed(title=f"Вы заблокировали пользователя ", description = f"Айди человека: <@{id}>", color= random.choice(clr))
    await ctx.send(embed=emb)
    await member.send(f"Вы были заблокированы на 24 часа администратором {ctx.message.author}")
@client.command()
@commands.has_any_role(532444048166748170, 532444461985300481)
async def unblock(ctx, member: discord.Member):
    id = member.id
    cursor.execute(f"DELETE FROM idbase WHERE id = {id}")
    conn.commit()
    emb = discord.Embed(title=f"Вы Разблокировали пользователя", description = f"Айди человека: <@{id}>", color= random.choice(clr))
    await ctx.send(embed=emb)
    await member.send(f"Вы были разблокированы администратором {ctx.message.author}")

@client.command()
@commands.has_any_role(532444048166748170, 532444461985300481)
async def blocked(ctx):
    cursor.execute('SELECT * FROM idbase')
    row = cursor.fetchone()
    while row is not None:
        emb = discord.Embed(title= "Список заблокированных людей: ", description="\n".join([str(i) for i in row]),  color= random.choice(clr))
        await ctx.send(embed=emb)
        row = cursor.fetchone()
@client.command()
@commands.has_any_role(532444048166748170, 532444461985300481)
async def answer(ctx, member: discord.Member, *, textAnswer):
    await member.send(embed=discord.Embed(title=f"Вы получили ответ от {ctx.message.author}. ", description=textAnswer, color= random.choice(clr)).set_footer(text=f"С уважением, {ctx.message.author}",icon_url=f"{ctx.message.author.avatar_url}"))
    await ctx.send(embed=discord.Embed(title="Успех!", description=f"Вы успешно отправили сообщение участнику {member}.", color=random.choice(clr)))          
@commands.has_any_role(532444048166748170, 532444461985300481)
@client.command()
async def start(ctx, maxUsers: int, game: str, *, time: str):
        await ctx.message.delete()
        users = 0
        message = await ctx.send(embed=discord.Embed(title=f"Набор на игру {game} был открыт", description="Нажми на реакцию ниже, чтобы участвовать.", color= random.choice(clr)).add_field(name="Максимальное число участников:",value=f"{maxUsers}", inline=False).add_field(name="Время провидения:", value=f"{time}", inline=False))
        await message.add_reaction("✔")
        while True:
            try:
                r, u = await client.wait_for('reaction_add', check=lambda r,u: r.message.id == message.id)
            except asyncio.TimeoutError as e:
                return 
            else:
                if u != client.user: 
                    if str(r) == '✔':
                        if users != maxUsers:
                            await ctx.send("Добавлен участник:" + str(u))
                            users+=1
                            await message.edit(embed=discord.Embed(title=f"Набор на игру {game} был открыт", description="Нажми на реакцию ниже, чтобы участвовать.", color= random.choice(clr)).add_field(name="Максимальное число участников:",value=f"{maxUsers}", inline=False).add_field(name="Время провидения:", value=f"{time}", inline=False).add_field(name="Текущее кол-во участников:", value=f"{users}"))
                            await asyncio.sleep(2)
                        elif users == maxUsers:
                            #await message.remove_reaction("✔", u)
                            await message.edit(embed=discord.Embed(title="Набор закрыт по причине: превышение участников.", color= random.choice(clr)))
                        try:
                            r, u = await client.wait_for('reaction_remove', check=lambda r,u: r.message.id == message.id)
                        except asyncio.TimeoutError as e:
                            return
                        else:
                            if u != client.user: 
                                if str(r) == '✔':
                                    await ctx.send("Из игры ушел участник:" + str(u))
                                    users-=1
                                    await message.edit(embed=discord.Embed(title=f"Набор на игру {game} был открыт", description="Нажми на реакцию ниже, чтобы участвовать.", color= random.choice(clr)).add_field(name="Максимальное число участников:",value=f"{maxUsers}", inline=False).add_field(name="Время провидения:", value=f"{time}", inline=False).add_field(name="Текущее кол-во участников:", value=f"{users}"))
                                    await asyncio.sleep(2)
                else:     
                    pass
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
                emb = discord.Embed(title = str(message.author), description = message.content, color= random.choice(clr))
                emb.set_footer(icon_url = str(message.author.avatar_url),text= str(message.author.id) + " | " +str(time_now)) 

                await channel.send(embed=emb) 
        
        
    
    

    

        
    
        
    

    

    

    
    if command == "case":
        case_role = discord.utils.get(message.guild.roles, name= "Кейс")
        if case_role in message.author.roles:
            user = message.author
            case_num = (random.randint(0,1000))
            channel3 = client.get_channel(int(605289537287094272))
            
            if case_num <= 50:
                proc = "5%"
                win2 = discord.utils.get(message.guild.roles, name="Сигна")
                if win2 in message.author.roles:
                    await message.channel.send("Вам выпала повторная роль! Введите команду заново!")
                    return
                else:
                    Win = "Сигна от иконаса"
                    emb = discord.Embed(title= "Шанс:" + proc, color= random.choice(clr))
                    emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                    await message.channel.send(embed= emb)
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win2)
            elif case_num <= 150:
                proc = "10%"
                win1 = discord.utils.get(message.guild.roles, name="10 робуксов")
                if win1 in message.author.roles:
                    Win = "10 робуксов"
                    embe= discord.Embed(title="Шанс:" + proc, colour= random.choice(clr))
                    embe.add_field(name="Вы выиграли повторный приз: " + str(Win), value = "Молодец!")
                    await message.channel.send(embed=embe)
                    emb = discord.Embed(title= "Повторный выиграш 10 робуксов", colour =random.choice(clr) )
                    emb.add_field(name= "Участнику {} выпал повторный приз 10 робуксов".format(message.author), value= f"Иконас выдай робуксы {message.author}")
                    await channel3.send(embed= emb)
                else:
                    Win = "10 робуксов"
                    embe= discord.Embed(title="Шанс:" + proc, color= random.choice(clr))
                    embe.add_field(name="Вы выиграли приз: " + str(Win), value = "Молодец!")
                    await message.channel.send(embed=embe)
                    emb = discord.Embed(title= "10 робуксов", color= random.choice(clr))
                    emb.add_field(name= f"{message.author} выиграл:" + str(Win), value= f"Иконас выдай робуксы {message.author}")
                    await channel3.send(embed= emb)
                    await user.add_roles(win1)

            elif case_num <= 250:
                proc = "10%"
                win3 = discord.utils.get(message.guild.roles, name="Добавление в друзья")
                if win3 in message.author.roles:
                    await message.channel.send("Вам выпала повторная роль! Введите команду заново!")
                    return
                else:
                    Win = "Добавление в друзья к иконасу"
                    emb = discord.Embed(title= "Шанс:" + proc, colour= random.choice(clr))
                    emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                    await message.channel.send(embed= emb)
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win3)
            elif case_num <= 500:
                proc = "20%"
                win5 = discord.utils.get(message.guild.roles, name="Личная комната")
                if win5 in message.author.roles:
                    await message.channel.send("Вам выпала повторная роль! Введите команду заново!")
                    return
                else:
                    Win = "Личная голосовая комната"
                    emb = discord.Embed(title= "Шанс:" + proc, color= random.choice(clr))
                    emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                    await message.channel.send(embed= emb)
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win5)
            elif case_num <= 700:
                proc = "25%"
                win4 = discord.utils.get(message.guild.roles, name="Выбор роли")
                if win4 in message.author.roles:
                    await message.channel.send("Вам выпала повторная роль! Введите команду заново!")
                    return
                else:
                    Win = "Выбор роли"
                    emb = discord.Embed(title= "Шанс:" + proc, color= random.choice(clr))
                    emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                    await message.channel.send(embed= emb)
                    await channel3.send(f"{message.author} выиграл:" + str(Win))
                    await user.add_roles(win4)
            elif case_num <= 1000:
                proc = "30%"
                channel2 = client.get_channel(int(532573322014359552))
                Win = "20000 ананасов"
                emb = discord.Embed(title= "Шанс:" + proc, color= random.choice(clr))
                emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                await message.channel.send(embed= emb)
                await channel2.send(f"=add-money {message.author.id} 20000")
            
            await asyncio.sleep(5)
            case1 = discord.utils.get(message.guild.roles, name="Кейс")
            await user.remove_roles(case1)
        else:
            return
    await client.process_commands(message)
     
                

token = os.environ.get("BOT_TOKEN")
client.run(str(token))
