import pymongo
from pymongo import MongoClient


import discord
from discord.ext import commands
from discord.ext.commands import errors
import asyncio
import random
from config import *

import pytz
from datetime import datetime 

import os

# db_pass = os.environ.get("DB_pass")
# db_pass = str(db_pass)
db_pass = "mongodb+srv://Nice:FFOBc0dAF8bnvAVc@ikonasbot.o8vxi.mongodb.net/IkonasFamily?retryWrites=true&w=majority"

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Я включен")
    i = 0
    while i == 0:
        game = discord.Game(f"В статусе разработки. | {version} | {prefix}")    
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(30)
        game = discord.Game(f"Восстановление активности сервера...| {version} | {prefix}")    
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(60)
        game = discord.Game(f"Бот для IKONAS FAMILY. | {version} | {prefix}")    
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(60)
        
client.remove_command("help")

cogs = ['cogs.block']
for i in cogs:
    try:
        client.load_extension(i)
    except Exception as e:
        print(f'{i} cannot be loaded {e}')
    else:
        print(f"{i.replace('cogs.', '')} has been loaded!")

  
    
"""@client.command()
async def case(ctx):
        if ctx.channel.id == 605710082042363934 or 532573322014359552:
            user = ctx.message.author
            case_role = discord.utils.get(ctx.guild.roles, name= "Кейс")
            if case_role in user.roles:
                case_num = (random.randint(0,1000))
                channel3 = client.get_channel(int(605289537287094272))
                if case_num <= 50:
                    proc = "5%"
                    win2 = discord.utils.get(ctx.guild.roles, name="Сигна")
                    if win2 in user.roles:
                        await ctx.channel.send("Вам выпала повторная роль! Введите команду заново!")
                        return
                    else:
                        Win = "Сигна от иконаса"
                        emb = discord.Embed(title= "Шанс:" + proc, color= random.choice(clr))
                        emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                        emb.set_footer(text=ctx.author)
                        await ctx.channel.send(embed= emb)
                        await channel3.send(f"{ctx.author} выиграл:" + str(Win))
                        await user.add_roles(win2)
                elif case_num <= 150:
                    proc = "10%"
                    win1 = discord.utils.get(ctx.guild.roles, name="10 робуксов")
                    if win1 in ctx.author.roles:
                        Win = "10 робуксов"
                        embe= discord.Embed(title="Шанс:" + proc, colour= random.choice(clr))
                        embe.add_field(name="Вы выиграли повторный приз: " + str(Win), value = "Молодец!")
                        embe.set_footer(text=ctx.author)
                        await ctx.channel.send(embed=embe)
                        emb = discord.Embed(title= "Повторный выиграш 10 робуксов", colour =random.choice(clr) )
                        emb.add_field(name= "Участнику {} выпал повторный приз 10 робуксов".format(ctx.author), value= f"Иконас выдай робуксы {ctx.author}")
                        await channel3.send(embed= emb)
                    else:
                        Win = "10 робуксов"
                        embe= discord.Embed(title="Шанс:" + proc, color= random.choice(clr))
                        embe.add_field(name="Вы выиграли приз: " + str(Win), value = "Молодец!")
                        embe.set_footer(text=ctx.author)
                        await ctx.channel.send(embed=embe)
                        emb = discord.Embed(title= "10 робуксов", color= random.choice(clr))
                        emb.add_field(name= f"{ctx.author} выиграл:" + str(Win), value= f"Иконас выдай робуксы {ctx.author}")
                        await channel3.send(embed= emb)
                        await user.add_roles(win1)
                elif case_num <= 250:
                    proc = "10%"
                    win3 = discord.utils.get(ctx.guild.roles, name="Добавление в друзья")
                    if win3 in ctx.author.roles:
                        await ctx.channel.send("Вам выпала повторная роль! Введите команду заново!")
                        return
                    else:
                        Win = "Добавление в друзья к иконасу"
                        emb = discord.Embed(title= "Шанс:" + proc, colour= random.choice(clr))
                        emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                        emb.set_footer(text=ctx.author)
                        await ctx.channel.send(embed= emb)
                        await channel3.send(f"{ctx.author} выиграл:" + str(Win))
                        await user.add_roles(win3)
                elif case_num <= 500:
                    proc = "20%"
                    win5 = discord.utils.get(ctx.guild.roles, name="Личная комната")
                    if win5 in ctx.author.roles:
                        await ctx.channel.send("Вам выпала повторная роль! Введите команду заново!")
                        return
                    else:
                        Win = "Личная голосовая комната"
                        emb = discord.Embed(title= "Шанс:" + proc, color= random.choice(clr))
                        emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                        emb.set_footer(text=ctx.author)
                        await ctx.channel.send(embed= emb)
                        await channel3.send(f"{ctx.author} выиграл:" + str(Win))
                        await user.add_roles(win5)
                elif case_num <= 700:
                    proc = "25%"
                    win4 = discord.utils.get(ctx.guild.roles, name="Выбор роли")
                    if win4 in ctx.author.roles:
                        await ctx.channel.send("Вам выпала повторная роль! Введите команду заново!")
                        return
                    else:
                        Win = "Выбор роли"
                        emb = discord.Embed(title= "Шанс:" + proc, color= random.choice(clr))
                        emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                        emb.set_footer(text=ctx.author)
                        await ctx.channel.send(embed= emb)
                        await channel3.send(f"{ctx.author} выиграл:" + str(Win))
                        await user.add_roles(win4)
                elif case_num <= 1000:
                    proc = "30%"
                    channel2 = client.get_channel(int(532573322014359552))
                    Win = "20000 ананасов"
                    emb = discord.Embed(title= "Шанс:" + proc, color= random.choice(clr))
                    emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                    emb.set_footer(text=ctx.author)
                    await ctx.channel.send(embed= emb)
                    await channel2.send(f"=add-money {ctx.author.id} 20000")
                await asyncio.sleep(5)
                case1 = discord.utils.get(ctx.guild.roles, name="Кейс")
                await user.remove_roles(case1)
            else:
                return
"""
              
@client.command()
@commands.has_any_role(642383351239409664) 
async def c_poll(ctx):
    channel = ctx.channel
    if channel.id == 724336893545808003:
      members_role = discord.utils.get(ctx.guild.roles, id=532458373535236099)
      await channel.set_permissions(members_role, read_messages=False)
      await ctx.message.delete()
      poll_role = discord.utils.get(ctx.guild.roles, id=643506538673209344)

      embed = discord.Embed(colour = 0xff1b1b)
      def check(msg):
          return msg.author == ctx.author

      msg = await ctx.send("Какой должна быть тема опроса?")
      theme = await client.wait_for("message", check=check)
      await theme.delete()

      await msg.edit(content="Какими должны быть варианты ответа?")
      answers = await client.wait_for("message", check=check)
      await answers.delete()

      embed.add_field(name="**"+ theme.content+ "**", value=answers.content)

      await ctx.channel.send(poll_role.mention,embed=embed)
      await msg.delete()
      await channel.set_permissions(members_role, read_messages=True)

              

@client.command()
@commands.has_any_role(645265129893658624)
async def magic(ctx):
    win_count = 0
    lose_count = 0
    users = []
    win_row = []
    lose_row = []
    user_choose = None
    winners = []
    losers = []
    reward = random.randint(50, 150)
    lose = random.randint(-125, -25)
    for m in ctx.guild.members:

        if m.status == discord.Status.idle or m.status == discord.Status.offline: continue
        if m.bot: continue
        users.append(str(m.id))
    while win_count != 6:
        i = random.choice(users)
        if i in win_row:
            pass
        else:
            user_choose = i
            win_count = win_count + 1
            win_row.append(str(user_choose))
            await asyncio.sleep(0.15)
    while lose_count != 2:
        user_row = random.choice(win_row)
        lose_count = lose_count + 1
        lose_row.append(user_row)
        win_row.remove(user_row)
    for i in win_row:
        user_row = ctx.guild.get_member(int(i))
        winners.append(f"{i} - {user_row.mention}")
    for i in lose_row:
        user_row = ctx.guild.get_member(int(i))
        losers.append(f"{i} - {user_row.mention}")
    users_win = ("\n".join([(i) for i in winners]))
    users_lose = ("\n".join([(i) for i in losers]))
    await ctx.send(embed= discord.Embed(title="**Удача!**", description=f"{good} дал подарки ({reward} ананасов) участникам:\n {users_win}",color= random.choice(clr)).add_field(name="**Неудача!**", value=f"{bad} украл подарки ({lose} ананасов) у участников:\n {users_lose}"))
                   
    
        
              
#Настройка отправки кода    
'''
channels = [645275470086275142,645275741524852736,645275781387386880]
conn = sqlite3.connect("datebase.sqlite")
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS kod(code text, message int, channel)')
codes = ['gwQIep2','XdOtIEm','x7W160Q','o9xvIW1','vk8kIwb','X2OVRfR','MhclQDo','AcrmW3F',
        'ZFC2y0F','Pbem6mI','BYvtx1c','V0AdnBu','1SMX5ML','XAslRT7','uIz9NO8','DLvKA1b',
        'DbkX6xQ','JjGrACm','V88W8HI','k4CzHHz','N7gNFmQ','6oc3M2S','O7100EU','zDAMZRX']
#Отправка кода
@client.command()
@commands.has_any_role(645265129893658624)
async def send_code(ctx):
    secret = random.choice(codes)
    secret_list=[]
    secret_list.append(secret)
    cursor.execute(f"INSERT INTO kod(code) VALUES(?)", secret_list)
    conn.commit()
    pineapples = random.randint(250,1500) if celebration == True else random.randint(-100, 1250)
    hard = random.randint(1, 15)
    channel = client.get_channel(int(random.choice(channels)))
    embed = discord.Embed(
        title=f'{"Элитный код:" if hard==3 else "Код:"} **{secret}**',
        description=f"Этот код дает: {pineapples} монет. \n*Чтобы его ввести напишите в канал для ботов: .enter_code [код]*",
        color=random.choice(clr),
        delete_after=600
    )
    channel_list = []
    channel_list.append(channel.id)
    cursor.execute(f"INSERT INTO kod(channel) VALUES(?)", channel_list)
    conn.commit()    
              
    embed_message = await channel.send(embed=embed)
              
    message_list=[]
    message_list.append(embed_message.id)
    cursor.execute(f"INSERT INTO kod(message) VALUES(?)", message_list)
    conn.commit()
#Ввод кода
@client.command()
async def enter_code(ctx, redeem_code: str):
   
        cursor.execute("SELECT channel FROM kod")
        channel = cursor.fetchone()
        channel = "".join([str(i) for i in channel])
        cursor.execute("SELECT message FROM kod")
        message_code = cursor.fetchone()
        message_code= "".join([str(i) for i in message_code])
        message_delete = await client.get_channel(channel).fetch_message(message_code)
              
        cursor.execute('SELECT code FROM kod')
        row = cursor.fetchone()
        db_code = " ".join([str(i) for i in row])
        if redeem_code == db_code.replace(" ", ""):
            await ctx.send(embed=discord.Embed(title="Поздравляю!", description="Вы ввели правильный код!", color= random.choice(clr)).set_footer(icon_url = str(ctx.author.avatar_url),text=str(ctx.author)))
            cursor.execute("DROP TABLE kod")
            conn.commit()
            cursor.execute('CREATE TABLE IF NOT EXISTS kod(code text, message int, channel)')
            conn.commit()
            await message_delete.delete()
            channel = client.get_channel(532573322014359552)
            await channel.send(f"Участник {ctx.author} ввел правильный код {message_delete.content}!")
        elif not redeem_code: await ctx.send(embed=discord.Embed(title="Неудача!", description="Вы ввели неправильный код!", color= random.choice(clr)).set_footer(icon_url = str(ctx.author.avatar_url),text=str(ctx.author)))
        else:
            await ctx.send(embed=discord.Embed(title="Неудача!", description="Вы ввели неправильный код!", color= random.choice(clr)).set_footer(icon_url = str(ctx.author.avatar_url),text=str(ctx.author)))
'''


@client.event
async def on_message(message):
    try:
        if message.guild.id == 531006906630930432:
            if message.channel.id == 724336560987701289:
                msg_low = message.content.lower()
                if msg_low.startswith("#отзыв"):
                    feedback = "#отзыв"
                    await message.delete()
                    embed = discord.Embed(
                        title=f"Отзыв от {message.author}",
                        description =f"{msg_low.replace(feedback, '')}",
                        color=random.choice(clr)
                    )
                    emb_msg = await message.channel.send(embed=embed)
                    await emb_msg.add_reaction("❤")
        await client.process_commands(message)
    except:
        pass
token = os.environ.get("BOT_TOKEN")
client.run(str(token))
