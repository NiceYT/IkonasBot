import pymongo
from pymongo import MongoClient
import discord
from discord.ext import commands
import random

from datetime import datetime
import pytz

import os
from config import clr
db_pass = os.environ.get("DB_pass")
db_pass = str(db_pass)


class blockCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_any_role(645265129893658624)
    async def block(self, ctx, member: discord.Member):   
        id = member.id
        if member in ctx.guild.members:   

            block_system = MongoClient(db_pass)
            db = block_system["BlockSystem"]
            collection = db["Block"] 
            results = collection.find_one({"id": id})
            if results == None:

                collection.insert_one({"id": id, "status": "blocked"})
                emb = discord.Embed(title=f"Вы заблокировали пользователя ", description = f"Участник: {member.mention}", color= random.choice(clr))
                await ctx.send(embed=emb)

                await member.send(f"Вы были заблокированы администратором {ctx.message.author}")
            elif results["id"] == id:
                emb = discord.Embed(title="Ошибка!", description="Этот участник уже был заблокирован!",color= random.choice(clr))
                await ctx.send(embed=emb)  
            else:
                emb = discord.Embed(title="Ошибка!", description="Данного участника нет на сервере!",color= random.choice(clr))
                await ctx.send(embed=emb)
            
                
    @commands.command()
    @commands.has_any_role(645265129893658624)
    async def unblock(self, ctx, member: discord.Member):
        id = member.id

        block_system = MongoClient(db_pass)
        db = block_system["BlockSystem"]
        collection = db["Block"] 

        results = collection.find_one({"id": id})
        if results == None:
            embed = discord.Embed(title="Ошибка!",description=f"Участник {member.mention} не заблокирован.",color= random.choice(clr))
            await ctx.send(embed=embed)

        else:
            collection.delete_one({"id": id})        

            emb = discord.Embed(title=f"Вы разблокировали пользователя", description = f"Упоминание участника: {member.mention}", color= random.choice(clr))
            await ctx.send(embed=emb)
                                
            await member.send(f"Вы были разблокированы администратором {ctx.message.author}")
                    
    @commands.command()
    @commands.has_any_role(645265129893658624)
    async def blocked(self,ctx):
        block_system = MongoClient(db_pass)
        db = block_system["BlockSystem"]
        collection = db["Block"]
        blocked = []
        results = collection.find({"status":"blocked"})
        for i in results:
            i = i["id"]
            blocked_users = ctx.guild.get_member(int(i))
            blocked.append(f"{i} - {blocked_users.mention}")
                    
        emb = discord.Embed(title= "Список заблокированных людей: ", description=("\n".join([str(i) for i in blocked])),  color= random.choice(clr))
        await ctx.send(embed=emb)

    @commands.command()
    @commands.has_any_role(645265129893658624)
    async def answer(self,ctx, member: discord.Member, *, textAnswer):
        await member.send(embed=discord.Embed(title=f"Вы получили ответ от {ctx.message.author}. ", description=textAnswer, color= random.choice(clr)).set_footer(text=f"С уважением, {ctx.message.author}",icon_url=f"{ctx.message.author.avatar_url}"))
        await ctx.send(embed=discord.Embed(title="Успех!", description=f"Вы успешно отправили сообщение участнику {member}.", color=random.choice(clr)))
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild == None:
            if message.author == self.bot.user:
                return
            else:
                block_system = MongoClient(db_pass)
                db = block_system["BlockSystem"]
                collection = db["Block"] 
                results = collection.find_one({"id": message.author.id})
                if results == None:
                    tz = pytz.timezone('Europe/Moscow')
                    time_now = str(datetime.now(tz)).split(' ')[1][:8]
                    channel = self.bot.get_channel(532573322014359552) 
                    emb = discord.Embed(title = str(message.author), description = message.content, color= random.choice(clr))
                    emb.set_footer(icon_url = str(message.author.avatar_url),text= str(message.author.id) + " | " +str(time_now))
                    await channel.send(embed=emb)
                elif str(message.author.id) == str(results["id"]):
                    await message.author.send("Вы в черном списке этого сервера!")
def setup(bot):
    bot.add_cog(blockCog(bot))
