import os, random, io, aiohttp, datetime, pytz

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = '!')


# Ready Annoucement
@client.event
async def on_ready():
        print('KermodeBot is ready for action!')

# Help Command
@client.command()
async def intro(ctx):
        await ctx.send('Current commands are:\n\n!pingu - checks bot ping\n' \
'!time - tells the local time\n' \
'!joke - tells a hilarious (terrible) joke\n' \
'!yeet - kicks a member from the server (mods only)\n' \
'!clear - clears n-1 of the most recent messages from the channel (mods only)\n' \
)

# On Message
@client.event
async def on_message(message):
        # React to Michael
        if message.author.name == 'God has forsaken us':
                emoji = client.get.emoji(636410883387686912)
                await message.add_reaction(emoji)
        await client.process_commands(message)

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

#Time Check
# getting utc timezone
utc = pytz.utc

# getting timezone by name
pst = pytz.timezone('US/Pacific')

@client.command()
async def time(ctx):
        await ctx.send(f'The current time in Squamish is {datetime.datetime.now(tz=pst).time()}')

# Clear Messages - default clear just the previous message
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
        await ctx.channel.purge(limit=amount)

#Kick - Kick completely from server
@client.command()
@commands.has_permissions(kick_members=True)
async def yeet(ctx, member : discord.Member):
        await member.kick()

# Actual Run
client.run('NjMzNzE0Mzk4ODgzNzQxNzI5.Xa4BPQ.PkDew1nsY7Xh-WD8_Fe36pE3Lg4')


                                                     
