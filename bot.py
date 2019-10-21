import os, random, io, aiohttp, datetime

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')


# Ready Annoucement
@client.event
async def on_ready():
        print('KermodeBot is ready for action!')

# Help Command
@client.command()
async def intro(ctx):
        await ctx.send('Current commands are:\n\n!pingu - checks bot ping\n!' \
'!dingding - tells Ding Ding that he is wrong/lying\n' \
'!time - tells the local time\n' \
'!joke - tells a hilarious (terrible) joke' \
)

# On Message
@client.event
async def on_message(message):
        # React to Michael
        if message.author.name == 'God has forsaken us':
                emoji = '😠'
                await message.add_reaction(emoji)

# Tell a joke
@client.command()
async def joke(ctx):
        jokes = ['How does Janna shield her allies?\nWith ease!', \
        "Why did Twisted Fate get deported?\nHe doesn't have a green card!", \
        "Why does Taliyah love bread?\n Because she's a sand witch!", \
        "What's Vayne's favorite website? Tumblr!"]
        await ctx.send(f'{random.choice(jokes)}')

# Check Ping
@client.command()
async def pingu(ctx):
        await ctx.send(f'Noot Noot! {round(client.latency * 1000)}ms')

# Rebuke
@client.command(aliases = ['ding'])
async def dingding(ctx):
        wrongs = ["That's a filthy lie!", "You take that back!", "I can't believe you've done this.", "Need a fire extinguisher for those pants?", "You're so wron$

        await ctx.send(f'{random.choice(wrongs)}')

#Time Check
@client.command()
async def time(ctx):
        await ctx.send(f'The current time in Squamish is {datetime.datetime.now().time()}')

#Kick
@client.command()
async def yeet(ctx, member : discord.Member):
        if message.author.name == 'JFIRECAT':
                await member.kick()
        else:
                return

# Actual Run
client.run('NjMzNzE0Mzk4ODgzNzQxNzI5.Xa3fcQ.O6DmjRDwRtfVc7VZJKLMs2GuJPw')

