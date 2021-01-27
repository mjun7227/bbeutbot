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
            if 44032>chr(i) and chr(i)>55204:
                t=t+i
            else:
                i=j2hcj(h2j(i))
                i="ㅃ"+i[1:]
                t=t+join_jamos(i)
        await message.channel.send(f"{message.author.name}:{t}")

client.run(os.environ['token'])