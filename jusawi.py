import os, discord, d20, time, get_character_sheet
from discord.ext import commands

jusawi_prefix = 'j;'
jusawi_intents = discord.Intents.default()
jusawi_intents.message_content = True
jusawi_bot = commands.Bot(command_prefix = jusawi_prefix, intents = jusawi_intents)

@jusawi_bot.event
async def on_ready():
	print(f"{time.asctime(time.localtime())} | Jusawi-ko is online!")
	await jusawi_bot.change_presence(activity=discord.Game(name="Library of Ruina | j;"))

@jusawi_bot.command()
async def ping(ctx):
	print(f"{time.asctime(time.localtime())} | Received ping request by {ctx.author} from {ctx.guild}.")
	await ctx.send(f"Ping: {round(jusawi_bot.latency * 1000, 3)}ms")

@jusawi_bot.command(aliases = ['r'])
async def roll(ctx):
	print(f"{time.asctime(time.localtime())} | Received roll request by {ctx.author} from {ctx.guild}: {ctx.message.content.split(sep = ' ', maxsplit = 1)[1]}.")
	try:
		await ctx.send(f"{str(d20.roll(ctx.message.content.split(sep = ' ', maxsplit = 1)[1]))}")

	except Exception as e:
		await ctx.send("Unexpected value, please rewrite!")

@jusawi_bot.command(aliases = ['import'])
async def thanks_to_cowt(ctx, url):
	print(f"{time.asctime(time.localtime())} | Received import request by {ctx.author} from {ctx.guild}.")
	try:
		get_character_sheet.get_character_list(url)
		await ctx.send("Success!")

	except Exception as e:
		await ctx.send("Error while importing..." + str(e))

with open(os.path.join(os.environ['VIRTUAL_ENV'] + '/discord_token.txt'), 'r') as token_file:
	token = token_file.read()
	jusawi_bot.run(token)
