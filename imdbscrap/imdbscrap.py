import discord
from discord.ext import commands
import aiohttp
import asyncio
import json
import os
from .utils.dataIO import fileIO

# just for the record, the cog is called imdb-scrap because it's a scrappy version of the original, not imdb [is] crap, because it's not.

class imdbscrap:
	"""A scrapped together version of the original imdb module from Red v1.
	
	It's functionally the same as V1 - copy your existing API key over if you have it. If you never got one for V1, get an API key from http://www.myapifilms.com//token.do"""

	def __init__(self, bot):
		self.bot = bot
		self.settings = fileIO("data/imdbscrap/settings.json", "load")

	@commands.command(pass_context=False)
	async def imdb(self, *message):
		msg = message
		if self.settings["MYAPIFILMS_TOKEN"] == "TOKENHERE":
			await self.bot.say("`You'll need to put your API key into data/imdbscrap/settings.json`")
			return False
		if len(msg) > 1:
						try:
							msg = "+".join(msg)
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