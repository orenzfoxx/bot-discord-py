#mantappp jiwaaa pake python versi 3.5 - 3.6

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("The Bot is online and connected")
    await client.change_presence(game=discord.Game(name="Tahap Pengembang"))
		

@client.event
async def on_message(message):
	if message.content.upper().startswith('!PING'):
	    userID = message.author.id
	    await client.send_message(message.channel, "<@%s> !Pong" % (userID))

	if message.content.upper().startswith('!MEMEK'):
	    userID = message.author.id
	    await client.send_message(message.channel, "<@%s> !enak euy:v" % (userID))

	if message.content.upper().startswith('!SAY'):
	    args = message.content.split(" ")
	    await client.send_message(message_channel, "%s" % (" ".join(args[1:])))
	else:
	    await client.send_message(message.channel, "You do not have Permission")

	if message.content.upper().startswith('!AMIADMIN'):
	    if "id role lu" in [role.id for role in message.author.roles]:
		await client.send_message(message.channel, "You are an admin")
	    else:
		await client.send_message(message.channel, "You are not an admin")


client.run("tarok token lo disini")
