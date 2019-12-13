import discord
from discord.ext import commands
import time
import asyncio
import random
import sqlite3
try:
    conn = sqlite3.connect("database.sqlite")

                             
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS react (message_id text, maxUsers int, users int, timestart text, game text)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS members_list (members text)''')
except:
    pass


class UtilsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active = True

    @commands.has_any_role(645265129893658624)
    @commands.command()
    async def start(self, ctx, maxUsers: int, game: str, *, time: str):
        await ctx.send(embed=discord.Embed(title="**Все возможные игры**", description="Игры:").add_field(name="Гонки:", value="1; Ивенты: 1: x2 очки, минус 1-3 поинта у рандомного человека.", inline=False).add_field(name="Idk:", value="2"))
        cursor.execute('SELECT message_id FROM react')
        message = cursor.fetchone()
        cursor.fetchone()
        if message == None:
            await ctx.message.delete()
            users = 0
            await ctx.send(embed=discord.Embed(title="**Внимание!**", description="При использовании **__любых__** багов вы будете лишены доступа в этот канал").set_footer(text=f"С уважением, {ctx.message.author}",icon_url=f"{ctx.message.author.avatar_url}"))
            message = await ctx.send(embed=discord.Embed(title=f"Набор на игру {game} был открыт", description="Нажми на реакцию ниже, чтобы участвовать.").add_field(name="Максимальное число участников:",value=f"{maxUsers}", inline=False).add_field(name="Время проведения:", value=f"{time}", inline=False))
            cursor.execute(f"INSERT INTO react (message_id, maxUsers, users, timestart, game) VALUES ({message.id}, {maxUsers}, {users}, {time},{game})")
            conn.commit()
            await message.add_reaction("✔")
        else:
            await ctx.message.delete()
            users = 0
            await ctx.send(embed=discord.Embed(title="**Внимание!**", description="При использовании **__любых__** багов вы будете лишены доступа в этот канал").set_footer(text=f"С уважением, {ctx.message.author}",icon_url=f"{ctx.message.author.avatar_url}"))
            message = await ctx.send(embed=discord.Embed(title=f"Набор на игру {game} был открыт", description="Нажми на реакцию ниже, чтобы участвовать.").add_field(name="Максимальное число участников:",value=f"{maxUsers}", inline=False).add_field(name="Время проведения:", value=f"{time}", inline=False))
            cursor.execute(f"UPDATE react SET message_id = {message.id}, maxUsers = {maxUsers}, users = {users}, timestart = {time}, game = {game}")
            conn.commit()
            await message.add_reaction("✔")
            
    @commands.has_any_role(645265129893658624)
    @commands.command()
    async def finish(self, ctx):
        await ctx.message.delete()
        #await ctx.channel.purge(limit=100)   
        cursor.execute("UPDATE react SET message_id = NULL, maxUsers = NULL, users = NULL, timestart = NULL, game = NULL")
        cursor.execute("UPDATE members_list SET members = NULL")
        conn.commit()
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
            #
            cursor.execute('SELECT message_id FROM react')
            message = cursor.fetchone()
            cursor.fetchone()
            cursor.execute('SELECT maxUsers FROM react')
            maxUsers = cursor.fetchone()
            maxUsers = "".join([str(i) for i in maxUsers])
            maxUsers = int(maxUsers)
            cursor.fetchone()
            cursor.execute('SELECT users FROM react')
            users = cursor.fetchone()
            users = "".join([str(i) for i in users])
            users = int(users)
            cursor.fetchone()
            cursor.execute('SELECT timestart FROM react')
            timestart = cursor.fetchone()
            timestart = "".join([str(i) for i in timestart])
            cursor.fetchone()
            cursor.execute('SELECT game FROM react')
            game = cursor.fetchone()
            game = "".join([str(i) for i in game])
            cursor.fetchone()
            users = int(users)
            #
            if message != None:
                guild = self.bot.get_guild(payload.guild_id)
                user = guild.get_member(payload.user_id)
                if user != self.bot.user:
                    if str(payload.message_id) == "".join([str(i) for i in message]):
                        if str(payload.emoji) == "✔":
                            if users != maxUsers:
                                await self.bot.get_channel(payload.channel_id).send("Добавлен участник:" + str(user))
                                message_edit = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
                                users+=1 
                                member = user.name
                                cursor.execute(f"UPDATE react SET users = {users}")
                                cursor.execute(f"INSERT INTO  members_list(members) VALUES ('{member}')")
                                conn.commit()
                                cursor.execute('SELECT * FROM members_list')
                                members = cursor.fetchall()
                                member_list = []
                                for i in [x[0] for x in members]:
                                    member_list.append(i)
                                members = ("\n".join([str(i) for i in member_list]))
                                await message_edit.edit(embed=discord.Embed(title=f"Набор на игру {game} был открыт", description="Нажми на реакцию ниже, чтобы участвовать.").add_field(name="Максимальное число участников:",value=f"{maxUsers}", inline=False).add_field(name="Время проведения:", value=f"{timestart}", inline=False).add_field(name="Текущее кол-во участников:", value=f"{users}").add_field(name="Участники: ", value=members, inline=False))                                 
                                await asyncio.sleep(2)
                                cursor.fetchone()
                            elif users >= maxUsers:
                                cursor.fetchone()
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):
        try:
            cursor.execute('SELECT message_id FROM react')
            message = cursor.fetchone()
            cursor.fetchone()
            cursor.execute('SELECT maxUsers FROM react')
            maxUsers = cursor.fetchone()
            maxUsers = "".join([str(i) for i in maxUsers])
            maxUsers = int(maxUsers)
            cursor.fetchone()
            cursor.execute('SELECT users FROM react')
            users = cursor.fetchone()
            users = "".join([str(i) for i in users])
            users = int(users)
            cursor.fetchone()
            cursor.execute('SELECT timestart FROM react')
            timestart = cursor.fetchone()
            timestart = "".join([str(i) for i in timestart])
            cursor.fetchone()
            cursor.execute('SELECT game FROM react')
            game = cursor.fetchone()
            game = "".join([str(i) for i in game])
            cursor.fetchone()
            users = int(users)
            if message != None:
                guild = self.bot.get_guild(payload.guild_id)
                user = guild.get_member(payload.user_id)
                if user != self.bot.user:
                    if str(payload.message_id) == "".join([str(i) for i in message]):
                        if str(payload.emoji) == "✔":
                            if users != maxUsers:
                                await self.bot.get_channel(payload.channel_id).send("Из игры ушел участник: " + str(user))
                                message_edit = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
                                users-=1 
                                member = user.name
                                cursor.execute(f"UPDATE react SET users = {users}")
                                cursor.execute(f"DELETE FROM members_list WHERE members = '{member}'")
                                conn.commit()
                                cursor.execute('SELECT * FROM members_list')
                                members = cursor.fetchall()
                                members_test = members
                                members_test =("\n".join([str(i) for i in members_test]))
                                member_list = []
                                for i in [x[0] for x in members]:
                                    member_list.append(i)
                                members = ("\n".join([str(i) for i in member_list]))
                                if members_test:
                                    await message_edit.edit(embed=discord.Embed(title=f"Набор на игру {game} был открыт", description="Нажми на реакцию ниже, чтобы участвовать.").add_field(name="Максимальное число участников:",value=f"{maxUsers}", inline=False).add_field(name="Время проведения:", value=f"{timestart}", inline=False).add_field(name="Текущее кол-во участников:", value=f"{users}").add_field(name="Участники: ", value=members, inline=False))   
                                    await asyncio.sleep(2)                                    
                                    cursor.fetchone()
                                else:
                                    await message_edit.edit(embed=discord.Embed(title=f"Набор на игру {game} был открыт", description="Нажми на реакцию ниже, чтобы участвовать.").add_field(name="Максимальное число участников:",value=f"{maxUsers}", inline=False).add_field(name="Время проведения:", value=f"{timestart}", inline=False).add_field(name="Текущее кол-во участников:", value=f"{users}"))
                                    await asyncio.sleep(2)
                                    cursor.fetchone()
        except Exception as e:
            print(e)  
    @commands.has_any_role(645265129893658624)
    @commands.command()
    async def game_i(self, ctx, *, game_sel: int = None):
        if game_sel == None:
            await ctx.message.delete()
            return
        elif game_sel == 1: #Числовая Гонка
            await ctx.send(embed= discord.Embed(title="Гонка", description="В этой игре выиграет тот, кто наберет первым 100 очков. Очки могут и убавляться и прибавляться. Игроки получают очки с помощью рандомайзера Бота. Обычно в игру играют 5 человек."))
        elif game_sel == 2: #
            pass
    @commands.has_any_role(645265129893658624)
    @commands.command()
    async def game_start(self, ctx, game: int, *, event: int):
        if game == 1 & event == 0:
            await ctx.send("Числовая гонка без ивента началась!")
        if game == 1 & event == 1: #Числовая гонки
            await ctx.send("Числовая гонка с ивентом **x2 очки** началась!")
        if game == 1 & event == 2: #Числовая гонки
            await ctx.send("Числовая гонка с ивентом **минус 1-3 поинта** у рандомного человека началась!")
    @commands.command()
    async def game_role(self, ctx):
        if ctx.channel.id != 644030582237560834:
            return
        elif ctx.channel.id == 644030582237560834:
            plus_or_minus = (random.randint(1, 20))
            if plus_or_minus == 13:
                lost = (random.randint(1, 3))
                await ctx.send(embed=discord.Embed(title="Неудача!", description=f"Игрок {ctx.author.name} потерял {lost} очков."))
            else:
                up = (random.randint(1,6))
                await ctx.send(embed=discord.Embed(title="Удача!", description=f"Игрок {ctx.author.name} получил {up} очков."))

    '''@commands.command()
    async def masttest(self, ctx):
        hard = 3
        if hard == 3:
            pass'''
        


                
        
        


def setup(bot):
    bot.add_cog(UtilsCog(bot))
