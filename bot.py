#Autarch by Mododon

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = Bot(description = "Autarch made by Mododon", command_prefix=";", pm_help = False)

#bot = commands.Bot(command_prefix=';')
#client = Bot(description = "Autarch made by Mododon")

@bot.event
async def on_ready():
    print ("Here master")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def come(ctx):
    await bot.say("I am at your service master")
    print ("I work")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

#@bot.command(pass_context=True)
#async def kick(ctx, user: discord.Member):
#    await bot.say("Get out".format(user.name))
#    await bot.kick(user)

@bot.command(pass_context=True)
async def sex(ctx):
    await bot.say("For you :smiley: :heart: :heart:")

@bot.command(pass_context=True)
async def brutallyrape (ctx, user: discord.Member):
    await bot.say("I have fucking raped {}".format(user.name))

@bot.command(pass_context=True)
async def sexing(ctx, user: discord.Member):
    await bot.say("I have fucked {}".format(user.name))

@bot.command(pass_context=True)
async def uptime(ctx):
    await bot.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not bot.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1

@bot.command(pass_context=True)
async def vinex(ctx):
    await bot.say("I am your sensei! Fight me")
    print ("Fight")

@bot.command(pass_context=True)
async def dev(ctx):
    await bot.say("Devoloping is going well, just need to do some scripts for some games")
    print ("It works")

    


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
    


bot.run("NDAyNTAxMjY2ODc1NjEzMjA2.DYMjMg.Ku5h4h2vu055XlWrPBQcYcfvV0U")
