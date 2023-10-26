import os, discord, d20, time
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
	print(f"{time.asctime(time.localtime())} | Received ping request by {ctx.author} from {ctx.guild}")
	await ctx.send(f"Ping: {round(jusawi_bot.latency * 1000, 3)}ms")

@jusawi_bot.command(aliases = ['r'])
async def roll(ctx):
	print(f"{time.asctime(time.localtime())} | Received roll request by {ctx.author} from {ctx.guild}: {ctx.message.content.split(sep = ' ', maxsplit = 1)[1]}.")
	try:
		await ctx.send(f"{str(d20.roll(ctx.message.content.split(sep = ' ', maxsplit = 1)[1]))}")

	except UnexpectedToken as e:
		await ctx.send("Unexpected value, please rewrite!")

with open(os.path.join(os.environ['VIRTUAL_ENV'] + '/discord_token.txt'), 'r') as token_file:
	token = token_file.read()
	jusawi_bot.run(token)
