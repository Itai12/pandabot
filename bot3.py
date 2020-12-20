import discord
from discord.ext import commands
import asyncio
import urllib3, json
from datetime import datetime
client = commands.Bot(command_prefix = '!')
client.remove_command("help")
global x
x=True
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name='mention me'))
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
	global x
	if message.author.id == client.user.id:
		return
	if message.content.startswith("<@!787710618038698034>") or message.content.startswith("<@787710618038698034>"):
		if message.content.startswith("<@!787710618038698034> help") or message.content.startswith("<@787710618038698034> help"):
			await message.channel.send("""{0} to have a cute redpanda image <:RedPanda:783742265931071519>
{0} nb to have some redpanda images ( max 20 )
Ex : ``{0} 2`` generates 2 redpanda images""".format(client.user.mention))
			return
		if message.content.startswith("<@!787710618038698034> stop") or message.content.startswith("<@787710618038698034> stop"):
			await message.channel.send("**Successfully stopped**")
			x = False
			return
		if message.content.startswith("<@!787710618038698034>"):
			inte=message.content[23:]
		else:
			inte=message.content[22:]
		try:
			x=int(inte)
			if x > 20:
				await message.channel.send("**Too Many images !** (max : 20)")
			else:
				for _ in range(x):
					if x == False:
						x=True
						break
					http = urllib3.PoolManager()
					url = "https://some-random-api.ml/img/red_panda"
					r = http.request('GET', url)
					data=json.loads(r.data.decode('utf-8'))
					await message.channel.send(data['link'])
		except Exception:
			http = urllib3.PoolManager()
			url = "https://some-random-api.ml/img/red_panda"
			r = http.request('GET', url)
			data=json.loads(r.data.decode('utf-8'))
			await message.channel.send(data['link'])
	await client.process_commands(message)
client.run('token')
