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
New_Year = (0xFF0000,
            0xFFFF00,
            0x0000FF,
            0xFFFFFF,
            0x000080,
            0x87CEEB,
            0x00FF00,
            0xFA8072,
            0xFFC0CB,
            0xFFDAB9,
            0x00FFFF,
            0xFF00FF,
            0x6A5ACD,
            0x7B68EE,
            0xE0FFFF,
            0x00FF7F,
            0xC0C0C0)
good = "Дед мороз"
bad = "Гринч"
clr = New_Year
celebration = True

@client.event
async def on_ready():
    print("Я включен")
client.remove_command("help")
cogs = ['cogs.event']
for i in cogs:
    try:
        client.load_extension(i)
    except Exception as e:
        print(f'{i} cannot be loaded {e}')
    else:
        print(f"{i.replace('cogs.', '')} has been loaded!")



    
conn = sqlite3.connect("datebase.sqlite")
cursor = conn.cursor()
    
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS idbase (id text)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS code_base (code text)''')
except:
    pass
"""@client.command()
@commands.has_any_role(645265129893658624)
async def clear_roles(ctx, role_id: int):
    counter = 0
    await ctx.send(embed=discord.Embed (title=f"Очистка роли {role_to_clear.name}у участников началась!", description=f"Вызвано: {ctx.author}",color= random.choice(clr))) 
    role_to_clear = discord.utils.get(ctx.guild.roles, id=role_id)
    for m in ctx.guild.members:
        await m.add_roles(role_to_clear)
        counter = counter + 1
        await asyncio.sleep(0.10)
    await ctx.send(embed = discord.Embed (Title = f"Очистка роли {role_to_clear.name} у {counter} участников закончилась!", description=f"Вызвано: {ctx.author}",color= random.choice(clr)))"""

              
              
@client.command()
async def c_poll(ctx):
    members_role = discord.utils.get(ctx.guild.roles, id=532458373535236099)
    channel = ctx.channel
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
    count = 0
    count2 = 0
    users = []
    users_win_row = []
    users_lose_row = []
    user_choose = None
    nagrada = random.randint(50, 150)
    lose = random.randint(-125, -25)
    for m in ctx.guild.members:
        if m.bot: continue
        users.append(str(m))
    while count != 6:
        i = random.choice(users)
        if i in users_win_row:
            pass
        else:
            user_choose = i
            count = count + 1
            users_win_row.append(str(user_choose))
            await asyncio.sleep(0.15)
    while count2 != 2:
        user_row = random.choice(users_win_row)
        count2 = count2 + 1
        users_lose_row.append(user_row)
        users_win_row.remove(user_row)
    users_win = ("\n".join([(i) for i in users_win_row]))
    users_lose = ("\n".join([(i) for i in users_lose_row]))
    await ctx.send(embed= discord.Embed(title="**Удача!**", description=f"{good} дал подарки ({nagrada} ананасов) участникам:\n {users_win}",color= random.choice(clr)).add_field(name="**Неудача!**", value=f"{bad} украл подарки ({lose} ананасов) у участников:\n {users_lose}"))


                   
    
@client.command()
@commands.has_any_role(645265129893658624)
async def block(ctx, member: discord.Member):
    id = member.id
    cursor.execute(f"INSERT INTO  idbase (id) VALUES ({id})")
    conn.commit()
    emb = discord.Embed(title=f"Вы заблокировали пользователя ", description = f"Айди человека: <@{id}>", color= random.choice(clr))
    await ctx.send(embed=emb)
    await member.send(f"Вы были заблокированы на 24 часа администратором {ctx.message.author}")
@client.command()
@commands.has_any_role(645265129893658624)
async def unblock(ctx, member: discord.Member):
    id = member.id
    cursor.execute(f"DELETE FROM idbase WHERE id = {id}")
    conn.commit()
    emb = discord.Embed(title=f"Вы Разблокировали пользователя", description = f"Айди человека: <@{id}>", color= random.choice(clr))
    await ctx.send(embed=emb)
    await member.send(f"Вы были разблокированы администратором {ctx.message.author}")
#Настройка отправки кода             
channels = [645275470086275142,645275741524852736,645275781387386880]

conn = sqlite3.connect("datebase.sqlite")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS kod(code text)''')

codes = ['gwQIep2','XdOtIEm','x7W160Q','o9xvIW1','vk8kIwb','X2OVRfR','MhclQDo','AcrmW3F',
        'ZFC2y0F','Pbem6mI','BYvtx1c','V0AdnBu','1SMX5ML','XAslRT7','uIz9NO8','DLvKA1b',
        'DbkX6xQ','JjGrACm','V88W8HI','k4CzHHz','N7gNFmQ','6oc3M2S','O7100EU','zDAMZRX']
#Отправка кода
@client.command()
@commands.has_any_role(645265129893658624)
async def send_code(ctx):
    cursor.execute("DROP table kod")
    conn.commit()
    cursor.execute('''CREATE TABLE IF NOT EXISTS kod(code text)''')
    conn.commit()

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
    await channel.send(embed=embed)
#Ввод кода
@client.command()
async def enter_code(ctx, redeem_code: str == None):
    try:
        cursor.execute('SELECT * FROM kod')
        row = cursor.fetchone()
        db_code = " ".join([str(i) for i in row])
        if redeem_code == db_code.replace(" ", ""):
            await ctx.send(embed=discord.Embed(title="Поздравляю!", description="Вы ввели правильный код!", color= random.choice(clr)).set_footer(icon_url = str(ctx.author.avatar_url),text=str(ctx.author)))

            cursor.execute("DROP TABLE kod")
            conn.commit()
            cursor.execute('''CREATE TABLE IF NOT EXISTS kod(code text)''')
            conn.commit()

        else:
            await ctx.send(embed=discord.Embed(title="Неудача!", description="Вы ввели неправильный код!", color= random.choice(clr)).set_footer(icon_url = str(ctx.author.avatar_url),text=str(ctx.author)))
    except Exception as e:
        pass
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
@commands.has_any_role(645265129893658624)
async def answer(ctx, member: discord.Member, *, textAnswer):
    await member.send(embed=discord.Embed(title=f"Вы получили ответ от {ctx.message.author}. ", description=textAnswer, color= random.choice(clr)).set_footer(text=f"С уважением, {ctx.message.author}",icon_url=f"{ctx.message.author.avatar_url}"))
    await ctx.send(embed=discord.Embed(title="Успех!", description=f"Вы успешно отправили сообщение участнику {member}.", color=random.choice(clr)))          

@client.event
async def on_message(message):
    await client.process_commands(message)
    args = message.content.split(' ')
    command = args[0][len(prefix):].lower()
    args = args[1:]
        
    if message.channel.id == 647853551804088341:
        if message.lower.startswith("#Идея"):
              idea = "#Идея"
              await message.delete()
              embed = discord.Embed(
                  title=f"Идея от {message.author}",
                  description =f"{message.replace(idea.lower, '')}",
                  color=random.choice(clr)
              )
              emb_message = await ctx.send(embed=embed)
              await emb_message.add_reaction("✔", "❌")
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
        if message.channel.id == 605710082042363934 or 532573322014359552:
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
                        emb.set_footer(text=message.author)
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
                        embe.set_footer(text=message.author)
                        await message.channel.send(embed=embe)
                        emb = discord.Embed(title= "Повторный выиграш 10 робуксов", colour =random.choice(clr) )
                        emb.add_field(name= "Участнику {} выпал повторный приз 10 робуксов".format(message.author), value= f"Иконас выдай робуксы {message.author}")
                        await channel3.send(embed= emb)
                    else:
                        Win = "10 робуксов"
                        embe= discord.Embed(title="Шанс:" + proc, color= random.choice(clr))
                        embe.add_field(name="Вы выиграли приз: " + str(Win), value = "Молодец!")
                        embe.set_footer(text=message.author)
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
                        emb.set_footer(text=message.author)
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
                        emb.set_footer(text=message.author)
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
                        emb.set_footer(text=message.author)
                        await message.channel.send(embed= emb)
                        await channel3.send(f"{message.author} выиграл:" + str(Win))
                        await user.add_roles(win4)
                elif case_num <= 1000:
                    proc = "30%"
                    channel2 = client.get_channel(int(532573322014359552))
                    Win = "20000 ананасов"
                    emb = discord.Embed(title= "Шанс:" + proc, color= random.choice(clr))
                    emb.add_field(name="Вы выиграли: " + str(Win), value = "Молодец!")
                    emb.set_footer(text=message.author)
                    await message.channel.send(embed= emb)
                    await channel2.send(f"=add-money {message.author.id} 20000")

                await asyncio.sleep(5)
                case1 = discord.utils.get(message.guild.roles, name="Кейс")
                await user.remove_roles(case1)
            else:
                return
        
     
                

token = os.environ.get("BOT_TOKEN")
client.run(str(token))
