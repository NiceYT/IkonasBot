import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import random
from config import *
class ProfilesCog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    
    @commands.command()
    async def create(self,ctx, member: discord.Member, name, type, colour, attention, speed, accuracy):
        if ctx.message.author.id == 264081734264422400 or ctx.message.author.id == 361179719800061963:
            stats_system = MongoClient(db_pass)
            db = stats_system["StatsSystem"]
            collection = db["Profiles"]
            results = collection.find_one({"member": member.id})
            if results == None:
                collection.insert_one({"member": member.id, "name": name, "type": type, "colour": colour, "attention": attention, "speed": speed, "accuracy": accuracy})
                succes_embed = discord.Embed(title="Успешно!", description=f"Профиль участника {member} был создан.", color=random.choice(clr))
                await ctx.send(embed=succes_embed)
            else:
                if int(results["member"]) == member.id:
                    pass
                else:
                    collection.insert_one({"member": member.id, "name": name, "type": type, "colour": colour, "attention": attention, "speed": speed, "accuracy": accuracy})
                    succes_embed = discord.Embed(title="Успешно!", description=f"Профиль участника {member} был создан.", color=random.choice(clr))
                    await ctx.send(embed=succes_embed)
    @commands.command()
    async def delete(self,ctx, member: discord.Member):
        if ctx.message.author.id == 264081734264422400 or ctx.message.author.id == 361179719800061963:
            stats_system = MongoClient(db_pass)
            db = stats_system["StatsSystem"]
            collection = db["Profiles"]
            collection.find_one_and_delete({"member": member.id})
            embed = discord.Embed(title="Успешно!", description=f"Профиль {member.mention} удален.", colour=random.choice(clr))
            await ctx.send(embed=embed)
    @commands.command()
    async def profile(self,ctx, member: discord.Member = None):
        if member == None:
            stats_system = MongoClient(db_pass)
            db = stats_system["StatsSystem"]
            collection = db["Profiles"]
            results = collection.find_one({"member": ctx.message.author.id})
            if results != None:
                name = results["name"]
                type = results["type"]
                colour = results["colour"]
                attention = results["attention"]
                speed = results["speed"]
                accuracy = results["accuracy"]
                embed = discord.Embed(title="Ваш профиль.", description="Информация о вас ниже.", colour=random.choice(clr))
                embed.add_field(name="Имя персонажа", value=name, inline=False)
                embed.add_field(name="Класс", value=type, inline=False)
                embed.add_field(name="Цвет огня", value=colour, inline=False)
                embed.add_field(name="Внимательность", value=attention, inline=False)
                embed.add_field(name="Скорость", value=speed, inline=False)
                embed.add_field(name="Точность", value=accuracy, inline=False)
                await ctx.message.author.send(embed=embed)
            else: 
                embed = discord.Embed(title="Ошибка!", description="У вас нет профиля.",colour=random.choice(clr))
                await ctx.message.author.send(embed=embed)
        if member != None and ctx.message.author.id == 264081734264422400 or member != None and ctx.message.author.id == 361179719800061963:
            stats_system = MongoClient(db_pass)
            db = stats_system["StatsSystem"]
            collection = db["Profiles"]
            results = collection.find_one({"member": member.id})
            if results != None:
                name = results["name"]
                type = results["type"]
                colour = results["colour"]
                attention = results["attention"]
                speed = results["speed"]
                accuracy = results["accuracy"]
                embed = discord.Embed(title=f"Профиль {member}.", description=f"Информация о игроке ниже.", colour=random.choice(clr))
                embed.add_field(name="Имя персонажа", value=name, inline=False)
                embed.add_field(name="Класс", value=type, inline=False)
                embed.add_field(name="Цвет огня", value=colour, inline=False)
                embed.add_field(name="Внимательность", value=attention, inline=False)
                embed.add_field(name="Скорость", value=speed, inline=False)
                embed.add_field(name="Точность", value=accuracy, inline=False)
                await ctx.message.author.send(embed=embed)
            else: 
                embed = discord.Embed(title="Ошибка!", description=f"У пользователя {member.mention} нет профиля.",colour=random.choice(clr))
                await ctx.message.author.send(embed=embed)
    @commands.command()
    async def stop(self,ctx):
        if ctx.message.author.id == 264081734264422400 or ctx.message.author.id == 361179719800061963:
            stats_system = MongoClient(db_pass)
            db = stats_system["StatsSystem"]
            collection = db["Rolls"]
            results = collection.find_one({"Working": True})
            results = results["Status"]
            if results == True:
                results = collection.find_one_and_update({"Working": True}, {"$set":{"Status": False}})
                embed = discord.Embed(title="Успешно!", description="Роллы больше не работают.", colour=random.choice(clr))
                await ctx.send(embed=embed)
            if results == False:
                results = collection.find_one_and_update({"Working": True}, {"$set": {"Status": True}})
                embed = discord.Embed(title="Успешно!", description="Роллы снова работают.", colour=random.choice(clr))
                await ctx.send(embed=embed)
    @commands.command()
    async def d(self,ctx, max: int = None, add: int = 0):
        if max != None:
            if add != 0:
                number = random.randint(1, max)
                embed = discord.Embed(title="Выпало число:", description=number+add, colour=random.choice(clr))
                await ctx.send(ctx.message.author.mention, embed=embed)
            elif add == 0:
                number = random.randint(1, max)
                embed = discord.Embed(title="Выпало число:", description=number+add, colour=random.choice(clr))
                await ctx.send(ctx.message.author.mention, embed=embed)            
        elif max == None:
            number = random.randint(1, 100)
            embed = discord.Embed(title="Выпало число:", description=number, colour=random.choice(clr))
            await ctx.send(ctx.message.author.mention, embed=embed)
    @commands.command()
    async def d1(self,ctx):
        stats_system = MongoClient(db_pass)
        db = stats_system["StatsSystem"]
        collection = db["Profiles"]
        results = collection.find_one({"member": ctx.message.author.id})
        if results != None:
            random_number= random.randint(1, 100)
            attention = int(results["attention"]) - 10
            attention = attention + random_number
            embed = discord.Embed(title="Выпало число:", description=attention, colour=random.choice(clr))
            await ctx.send(ctx.message.author.mention, embed=embed)
        else:
            embed = discord.Embed(title="Ошибка!", description="У вас нет профиля.",colour=random.choice(clr))
            await ctx.message.author.send(embed=embed)
    @commands.command()
    async def d2(self,ctx):
        stats_system = MongoClient(db_pass)
        db = stats_system["StatsSystem"]
        collection = db["Profiles"]
        results = collection.find_one({"member": ctx.message.author.id})
        if results != None:
            random_number= random.randint(1, 100)
            speed = int(results["speed"]) - 10
            speed = speed + random_number
            embed = discord.Embed(title="Выпало число:", description=speed, colour=random.choice(clr))
            await ctx.send(ctx.message.author.mention, embed=embed)
        else:
            embed = discord.Embed(title="Ошибка!", description="У вас нет профиля.",colour=random.choice(clr))
            await ctx.message.author.send(embed=embed)
    @commands.command()
    async def d3(self,ctx):
        stats_system = MongoClient(db_pass)
        db = stats_system["StatsSystem"]
        collection = db["Profiles"]
        results = collection.find_one({"member": ctx.message.author.id})
        if results != None:
            random_number= random.randint(1, 100)
            accuracy = int(results["accuracy"]) - 10
            accuracy = accuracy + random_number
            embed = discord.Embed(title="Выпало число:", description=accuracy, colour=random.choice(clr))
            await ctx.send(ctx.message.author.mention, embed=embed)
        else:
            embed = discord.Embed(title="Ошибка!", description="У вас нет профиля.",colour=random.choice(clr))
            await ctx.message.author.send(embed=embed)
def setup(bot):
    bot.add_cog(ProfilesCog(bot))
