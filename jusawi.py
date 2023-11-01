# Imports
import os, discord, d20, time, get_character_sheet
from discord.ext import commands

# Discord On-Boot
jusawi_prefix = 'j;'
jusawi_intents = discord.Intents.default()
jusawi_intents.message_content = True
jusawi_bot = commands.Bot(command_prefix = jusawi_prefix, intents = jusawi_intents)

jusawi_bot.remove_command("help")

# Functions
def timestamp():
	return f"{time.asctime(time.localtime())} | "

# Asynchronous Functions
@jusawi_bot.event
async def on_ready():
	""" Readies the Discord client. """
	print(timestamp() + "Jusawi-ko is online!")
	await jusawi_bot.change_presence(activity=discord.Game(name="Library of Ruina | j;help"))

@jusawi_bot.command()
async def help(ctx):
	""" Displays this message! """
	print(timestamp() + f"Received help request by {ctx.author} from {ctx.guild}.")
	helptext = "Jusawi Help!\n\n**help**: Displays this message!\n**ping**: Request a ping!\n**roll**: Roll a dice!\n**import**: Import a character sheet!"
	await ctx.send(helptext)

@jusawi_bot.command()
async def ping(ctx):
	""" Request a ping! """
	print(timestamp() + f"Received ping request by {ctx.author} from {ctx.guild}.")
	await ctx.send(f"Ping: {round(jusawi_bot.latency * 1000, 3)}ms")

@jusawi_bot.command(aliases = ['r'])
async def roll(ctx):
	""" Roll a dice! """
	print(timestamp() + f"Received roll request by {ctx.author} from {ctx.guild}: {ctx.message.content.split(sep = ' ', maxsplit = 1)[1]}.")
	await ctx.send(f"{str(d20.roll(ctx.message.content.split(sep = ' ', maxsplit = 1)[1]))}")

@jusawi_bot.command(aliases = ['import'])
async def thanks_to_cowts(ctx, url):
	""" Import a character sheet! """
	print(timestamp() + f"Received import request by {ctx.author} from {ctx.guild}.")
	get_character_sheet.get_character_list(url)
	await ctx.send("Success!")

@thanks_to_cowts.error
async def info_error(ctx, error):
	""" Exception handling for the import command. """
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Missing a URL!")

# Start Discord Bot
with open(os.path.join(os.environ['VIRTUAL_ENV'] + '/discord_token.txt'), 'r') as token_file:
	token = token_file.read()
	jusawi_bot.run(token)
