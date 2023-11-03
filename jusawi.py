# ===== Imports =====
import asyncio, os, discord, d20, time, get_character_sheet, re, json
from discord.ext import commands

# ===== Bot Config =====
prefix = 'j;'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = prefix, intents = intents)

bot.remove_command("help")

# ===== Functions =====
def command_timestamp(cmd, ctx):
	return f"{time.asctime(time.localtime())} | Received `{cmd}` request by {ctx.author} from {ctx.guild}."

def embed(title, desc, color, foot, img, auth, **kwargs):
	embed = discord.Embed(title = title, description = desc, color = color, set_footer = foot, set_thumbnail = img, set_author = auth)
	for key, val in kwargs.items():
		embed.add_field(key, val, False)
	return embed

def get_spreadsheet_id(url):
	return re.findall("(d\/[a-zA-Z0-9-_]+)", url)[0].split('/')[1]

# ===== Asynchronous Functions (Commands) =====
@bot.event
async def on_ready():
	""" Readies the Discord client. """
	print(time.asctime(time.localtime()) + " | Jusawi-ko is online!")
	await bot.change_presence(activity=discord.Game(name="Library of Ruina | j;help"))

@bot.command()
async def help(ctx):
	""" Display this message! """
	print(command_timestamp("help", ctx))
	cmd_name = ["Help", "Ping", "Roll", "Import"]
	cmd_desc = ["Display this message!", "Request a ping!", "Roll a dice!", "Import a character sheet!"]
	cmd_help = {cmd_name[i]: cmd_desc[i] for i in range(len(cmd_name))}
	await ctx.send(embed("Jusawi-ko Help!", "Help Menu", (255, 255, 255), "Jusawi-ko is made by WolfPai!", None, None, cmd_help))

@bot.command()
async def about(ctx):
	""" About Jusawi-ko. """
	print(command_timestamp("about", ctx))
	about = {"About Jusawi-ko": "Jusawi-ko is a Discord bot designed to help with managing Project Moon Tabletop Roleplay Game characters. Currently uses the Community Rules 2.0\n\nOriginally designed for Kawazoi Office, with love :heart:.\n'Jusawi' means 'dice' in Korean, and the '-ko' suffix usually indicates a female child.\nLook at the source code here: https://github.com/Wolf-Pai/jusawi-ko"}
	await ctx.send(embed("About Jusawi-ko!", "About", (255, 255, 255), "Jusawi-ko is made by WolfPai!", None, None, about))

@bot.command()
async def ping(ctx):
	""" Request a ping! """
	print(command_timestamp("ping", ctx))
	if round(bot.latency) < 10:
		await ctx.send(f"Ping: {round(bot.latency * 1000, 3)} ms\nThat's {round(10 / bot.latency)} times faster than a WARP Train!")
	elif round(bot.latency) == 10:
		await ctx.send(f"Ping: {round(bot.latency * 1000)} ms\nThat's... the same speed as a WARP Train!")
	else:
		await ctx.send(f"Ping: {round(bot.latency * 1000, 3)} ms\nThat's very slow... {round(10 / bot.latency)} times slower than a WARP Train.")

@bot.command(aliases = ['r'])
async def roll(ctx):
	""" Roll a dice! """
	print(command_timestamp("roll", ctx))
	try:
		await ctx.send(f"{str(d20.roll(ctx.message.content.split(sep = ' ', maxsplit = 1)[1]))}")
	except Exception as e:
		print(e)

@bot.command(aliases = ['import'])
async def thank_you_cowts(ctx, url):
	""" Import a character sheet! """
	""" Thanks to CowTs for maintaining the Project Moon TTRPG Character Sheet! Jusawi-ko couldn't have been possible without you! """
	print(command_timestamp("import", ctx))
	try:
		with open("venv/playerdata", 'r') as datafile:
			for line in datafile:
				if json.loads(line)["player"] == str(ctx.message.author.name) and list(json.loads(line).keys())[1] == get_spreadsheet_id(url):
					await ctx.send("This character already exists! Use the `update` command to update instead.")
				return
		with open("venv/playerdata", 'a') as datafile:
			data = {"player": ctx.message.author.name, get_spreadsheet_id(url): get_character_sheet.get_character(url)}
			datafile.write(json.dumps(data))
			await ctx.send("Successful `import`!")
	except Exception as e:
		print(e)
		await ctx.send("This isn't a URL...")

@bot.command()
async def update(ctx, charname):
	""" Update a character's sheet! """
	print(command_timestamp("update", ctx))
	try:
		with open("venv/playerdata", 'r') as datafile:
			pass #if json.loads(line)["player"] == str(ctx.message.author.name) and json.loads(line)[list(json.loads(line).keys())[1]] # do check for character name
		with open("venv/playerdata", 'a') as datafile:
			pass #<>
	except Exception as e:
		print(e)

@bot.command(aliases = ['char'])
async def character(ctx, *args):
	""" Display current character! """
	print(command_timestamp("character", ctx))
	try:
		if args and args[0].lower() == "list":
			print("List characters...")
		await ctx.send("Successful `char`!")
	except Exception as e:
		print(e)

@bot.command()
async def sheet(ctx):
	""" Display the current character's sheet! """
	print(command_timestamp("sheet", ctx))
	try:
		await ctx.send("Successful `sheet`!")
	except Exception as e:
		print(e)

@bot.command()
async def removecharacter(ctx):
	""" Removes a character. Be careful! """

# ===== Exception Handling =====
@roll.error
async def roll_error(ctx, error):
	""" Exception handling for `roll` """
	if isinstance(error, commands.CommandInvokeError):
		await ctx.send("Missing a dice!")

@thank_you_cowts.error
async def import_error(ctx, error):
	""" Exception handling for `import` """
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Missing a spreadsheet URL!")

# ===== Start Discord Bot =====
with open(os.path.join(os.environ['VIRTUAL_ENV'] + '/discord_token.txt'), 'r') as token_file:
	token = token_file.read()
	bot.run(token)
