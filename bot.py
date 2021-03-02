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
            if 44032>ord(i) or ord(i)>55204:
                t=t+i
            else:
                i=j2hcj(h2j(i))
                i="ㅃ"+i[1:]
                t=t+join_jamos(i)
        await message.channel.send(f"{message.author.name}:{t}")
    if message.content.startswith("!호에"):
        a=message.content
        result="호"
        for i in a[3:]:
            s=bin(ord(i))[2:]
            s=s.replace("1","ㅇ")
            s=s.replace("0","ㅔ")
            result+=(s)
        result=join_jamos(result)
        await message.channel.send(f"{message.author.name}:{re}")

client.run(os.environ['token'])