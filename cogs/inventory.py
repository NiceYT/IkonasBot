import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
import random
from config import clr, db_pass
class InventoryCog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command(aliases=["inv"])
    async def inventory(self, ctx, member: discord.Member = None):
        if member == None:
            stats_system = MongoClient(db_pass)
            db = stats_system["StatsSystem"]
            collection = db["Profiles"]
            results = collection.find_one({"member": ctx.message.author.id})
            if results != None:
                item1 = results["item1"]
                item2 = results["item2"]
                item3 = results["item3"]
                item4 = results["item4"]
                item5 = results["item5"]
                if item1 == "None":
                    item1 = "Отсутствует"
                if item2 == "None":
                    item2 = "Отсутствует"
                if item3 == "None":
                    item3 = "Отсутствует"
                if item4 == "None":
                    item4 = "Отсутствует"
                if item5 == "None":
                    item5 = "Отсутствует"
                embed = discord.Embed(title="Ваш инвентарь.", description="Ваши предметы показаны ниже.", colour=random.choice(clr))
                embed.add_field(name="Первый предмет", value=f"*{item1}*", inline=False)
                embed.add_field(name="Второй предмет", value=f"*{item2}*", inline=False)
                embed.add_field(name="Третий предмет", value=f"*{item3}*", inline=False)
                embed.add_field(name="Четвертый предмет", value=f"*{item4}*", inline=False)
                embed.add_field(name="Пятый предмет", value=f"*{item5}*", inline=False)
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
                item1 = results["item1"]
                item2 = results["item2"]
                item3 = results["item3"]
                item4 = results["item4"]
                item5 = results["item5"]
                if item1 == "None":
                    item1 = "Отсутствует"
                if item2 == "None":
                    item2 = "Отсутствует"
                if item3 == "None":
                    item3 = "Отсутствует"
                if item4 == "None":
                    item4 = "Отсутствует"
                if item5 == "None":
                    item5 = "Отсутствует"
                embed = discord.Embed(title="Ваш инвентарь.", description="Ваши предметы показаны ниже.", colour=random.choice(clr))
                embed.add_field(name="Первый предмет", value=f"*{item1}*", inline=False)
                embed.add_field(name="Второй предмет", value=f"*{item2}*", inline=False)
                embed.add_field(name="Третий предмет", value=f"*{item3}*", inline=False)
                embed.add_field(name="Четвертый предмет", value=f"*{item4}*", inline=False)
                embed.add_field(name="Пятый предмет", value=f"*{item5}*", inline=False)
                await ctx.message.author.send(embed=embed)
            else: 
                embed = discord.Embed(title="Ошибка!", description=f"У пользователя {member.mention} нет профиля.",colour=random.choice(clr))
                await ctx.message.author.send(embed=embed)
    @commands.command(aliases=["ai"])
    async def additem(self, ctx, member: discord.Member, slot, attention: int, speed: int, accuracy: int, *, item):
        if ctx.author.id == 264081734264422400 or ctx.author.id == 361179719800061963:
            stats_system = MongoClient(db_pass)
            db = stats_system["StatsSystem"]
            collection = db["Profiles"]
            results = collection.find_one({"member": member.id})
            if results != None:
                m_attention = int(results["attention"])
                m_speed = int(results["speed"])
                m_accuracy =int(results["accuracy"])
                m_attention = m_attention + attention
                m_speed = m_speed + speed
                m_accuracy = m_accuracy + accuracy
                m_attention = str(m_attention)
                m_speed = str(m_speed)
                m_accuracy = str(m_accuracy)
                collection.find_one_and_update({"member": member.id},{"$set":{"attention": m_attention, "speed": m_speed, "accuracy": m_accuracy, f"item{slot}":item}})
                embed = discord.Embed(title="Успешно!", description=f'Участнику {member.mention} был выдан предмет "{item}" с характеристиками: {attention}(Внимание), {speed}(Скорость), {accuracy}(Точность).', colour=random.choice(clr))
                await ctx.message.channel.send(embed=embed)
            else: 
                embed = discord.Embed(title="Ошибка!", description=f"У участника {member.mention} нет профиля.",colour=random.choice(clr))
                await ctx.message.channel.send(embed=embed)
def setup(bot):
    bot.add_cog(InventoryCog(bot))
