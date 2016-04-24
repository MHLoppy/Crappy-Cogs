import discord
from discord.ext import commands
import random

class Same:
	"""Sometimes says same when a user says same."""

	def __init__(self, bot):
		self.bot = bot

	async def scrutinize_messages(self, message):

		channel = message.channel

		if (message.content == "same" and message.author.id != self.bot.user.id):
			kek = random.randint(1, 20)
			if kek == 1:
				await self.bot.send_message(channel, "same")
			if kek == 2:
				await self.bot.send_message(channel, "same")
			if kek == 3:
				await self.bot.send_message(channel, "same")
			if kek == 4:
				await self.bot.send_message(channel, "same")
			if kek == 5:
				await self.bot.send_message(channel, "`same`")
			if kek == 6:
				await self.bot.send_message(channel, "SAME")
			if kek == 7:
				await self.bot.send_message(channel, "`SAME`")
			if kek == 8:
				await self.bot.send_message(channel, "same!")
			if kek == 9:
				await self.bot.send_message(channel, "`SAME!`")
			if kek == 10:
				await self.bot.send_message(channel, "http://i.imgur.com/ha1HJd7.gif")

def setup(bot):
	n = Same(bot)
	bot.add_listener(n.scrutinize_messages, "on_message")
	bot.add_cog(Same(bot))
