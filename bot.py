import discord 
import asyncio
from jamo import j2hcj, h2j
from uni import join_jamos
import os

client= discord.Client()

@client.event
async def on_ready():
    print("응")

@client.event

async def on_message(message):
    if message.content.startswith("ㅃ"):
        t=""
        ctx=message.content
        for i in ctx[1:]:
            i=j2hcj(h2j(i))
            i="ㅃ"+i[1:]
            t=t+join_jamos(i)
        await message.channel.send(f"{message.author.name}:{t}")

#client.run(os.environ['token'])
client.run("NzU0Njc0ODIyODU1OTE3NjM5.X14Lsg.MN2WcIJg7Sox_4R0o6uHnXYtLEE")