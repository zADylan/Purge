import discord
import asyncio
import json
import sys
import time
import colorama
import sty
from colorama import Fore


client = discord.Client()

with open('config.json') as handle:
    cipher = json.load(handle)
    token = (cipher["token"])
    if token == "token":
        print ("Please put token in to the config (config.json)")
        time.sleep(5)
        sys.exit()

@client.event
async def on_ready():
    print(f'''
  ♥__♥     ♥__♥
 ♥     ♥ ♥     ♥
 ♥      ♥      ♥
  ♥     /      ♥
   ♥    \     ♥
    ♥   /   ♥
      ♥ \ ♥
        ♥
        ''')
    print(f"Account: {client.user} | Created by ADylan")
    print (f"Command : %%, ##, &&")

@client.event
async def on_message(message):
    if message.content == '%%':
        await message.delete()
        async for message in message.channel.history(limit=10000).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    if message.content == '##':
        await message.delete()
        async for message in message.channel.history(limit=10000).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    if message.content == '&&':
        await message.delete()
        async for message in message.channel.history(limit=10000).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
                    
client.run(token, bot=False)
