import discord
from discord.ext import commands
import aiohttp
import asyncio
import json
import os
from .utils.dataIO import fileIO

class imdbscrap:
	"""A scrapped together version of the original imdb module from Red v1."""

	def __init__(self, bot):
		self.bot = bot
		self.settings = fileIO("data/imdbscrap/settings.json", "load")

	@commands.command(pass_context=False)
	async def imdb(self, *message):
		msg = message#.split()
		if self.settings["MYAPIFILMS_TOKEN"] == "TOKENHERE":
			await self.bot.say("`YOU NONG YOU MESSED UP THE SETTINGS`")
			return False
		if len(msg) > 1:
#				if len(msg[1]) > 1 and len([msg[1]]) < 20:
						try:
#							msg.remove(msg[0])
							msg = "+".join(msg)
#							await self.bot.say("debug: " + msg)
							search = "http://api.myapifilms.com/imdb/title?format=json&title=" + msg + "&token=" + self.settings["MYAPIFILMS_TOKEN"]
							async with aiohttp.get(search) as r:
								result = await r.json()
								title = result['data']['movies'][0]['title']
								year = result['data']['movies'][0]['year']
								rating = result['data']['movies'][0]['rating']
								url = result['data']['movies'][0]['urlIMDB']
								msg = "Title: " + title + " | Released on: " + year + " | IMDB Rating: " + rating + ".\n" + url
								await self.bot.say(msg)
						except:
							await self.bot.say("`Error.`")
#				else:
#					await self.bot.say("`Invalid search.`")
		else:
			await self.bot.say("imdb [text]")

def check_folders():
	if not os.path.exists("data/imdbscrap"):
		print("Creating data/imdbscrap folder...")
		os.makedirs("data/imdbscrap")

def check_files():
	settings = {"MYAPIFILMS_TOKEN": "TOKENHERE"}
	
	f = "data/imdbscrap/settings.json"
	if not fileIO(f, "check"):
		print("Creating imdbscrap.json")
		print("You must obtain an API key as noted in the newly created 'settings.json' file")
		fileIO(f, "save", settings)			
			
def setup(bot):
	check_folders()
	check_files()
	n = imdbscrap(bot)
	bot.add_cog(imdbscrap(bot))