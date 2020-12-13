import discord
from discord.ext import commands
import asyncio
import urllib3, json
from datetime import datetime
client = commands.Bot(command_prefix = '!')
client.remove_command("help")
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name='mention me'))
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
	if message.content.startswith("<@!787710618038698034>"):
		inte=message.content[23:]
		try:
			x=int(inte)
			for i in range(x):
				http = urllib3.PoolManager()
				url = "https://some-random-api.ml/img/red_panda"
				r = http.request('GET', url)
				data=json.loads(r.data.decode('utf-8'))
				await message.channel.send(str(data)[10:])
		except Exception as e:
			http = urllib3.PoolManager()
			url = "https://some-random-api.ml/img/red_panda"
			r = http.request('GET', url)
			data=json.loads(r.data.decode('utf-8'))
			await message.channel.send(str(data)[10:])
	await client.process_commands(message)
client.run('Nzg3NzEwNjE4MDM4Njk4MDM0.X9Y6rg.0IN3V7vwKK_s3ssZo9unfJUsxS4')
