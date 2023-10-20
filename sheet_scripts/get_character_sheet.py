import os, httplib2

from apiclient import discovery
from google.oauth2 import service_account

try:
	scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
	secret_file = os.path.join('../env/jusawi-ko-service-account.json')
	credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scope)
	service = discovery.build('sheets', 'v4', credentials=credentials)

except OSError as e:
	print(e)

RANGES = [
		'BioSheet!F4', # Name
		'BioSheet!F5', # Occupation
		'BioSheet!E6', # Age
		'BioSheet!M6', # Height
		'CharSheet!B7', # Character image
		'CharSheet!AS2', # Player name
		'CharSheet!U21', # Rank
		'CharSheet!AB23', # Level
		'CharSheet!U23', # EXP
		'CharSheet!R13', # Fortitude
		'CharSheet!W13', # Prudence
		'CharSheet!AB13', # Justice
		'CharSheet!R20', # Charm
		'CharSheet!W20', # Insight
		'CharSheet!AB20', # Temperance
		'CharSheet!AO5', # Health max
		'CharSheet!AZ5', # Stagger res nax
		'CharSheet!AO7', # Mentality max
		'CharSheet!AZ7', # Light max
		'CharSheet!AJ9', # Att
		'CharSheet!AQ9', # Def
		'CharSheet!AX9', # Evd
		'CharSheet!BM42', # Weapon effect slot amount
		'CharSheet!BM43', # Outfit effect slot amount
		'CharSheet!BM44', # Augment effect slot amount
		'CharSheet!BM45', # Skill effect slot amount
		'CharSheet!B47', # Weapon 1 Name
		'CharSheet!O47', # Weapon 1 Melee true
		'CharSheet!O48', # Weapon 1 Range true
		'CharSheet!S47', # Weapon 1 Dice range
		'CharSheet!U47', # Weapon 1 Dice mod
		'CharSheet!W47', # Weapon 1 Form property
		'CharSheet!W48', # Weapon 1 Hand property
		'CharSheet!D49', # Weapon 1 Slash true
		'CharSheet!D51', # Weapon 1 Pierce true
		'CharSheet!D53', # Weapon 1 Blunt true
		'CharSheet!F49', # Weapon 1 Effect 1 Name
		'CharSheet!F50', # Weapon 1 Effect 1 Cost
		'CharSheet!M49', # Weapon 1 Effect 2 Name
		'CharSheet!M50', # Weapon 1 Effect 2 Cost
		'CharSheet!F51', # Weapon 1 Effect 3 Name
		'CharSheet!F52', # Weapon 1 Effect 3 Cost
		'CharSheet!M51', # Weapon 1 Effect 4 Name
		'CharSheet!M52', # Weapon 1 Effect 4 Cost
		'CharSheet!F53', # Weapon 1 Effect 5 Name
		'CharSheet!F54', # Weapon 1 Effect 5 Cost
		'CharSheet!M53', # Weapon 1 Effect 6 Name
		'CharSheet!M54', # Weapon 1 Effect 6 Cost
		'CharSheet!F55', # Weapon 1 Effect 7 Name
		'CharSheet!F56', # Weapon 1 Effect 7 Cost
		'CharSheet!M55', # Weapon 1 Effect 8 Name
		'CharSheet!M56', # Weapon 1 Effect 8 Cost
		'CharSheet!F57', # Weapon 1 Effect 9 Name
		'CharSheet!F58', # Weapon 1 Effect 9 Cost
		'CharSheet!M57', # Weapon 1 Effect 10 Name
		'CharSheet!M58', # Weapon 1 Effect 10 Cost
		'CharSheet!AG48', # Weapon 1 Legal
		'CharSheet!AI47', # Weapon 2 Name
		'CharSheet!AV47', # Weapon 2 Melee true
		'CharSheet!AV48', # Weapon 2 Range true
		'CharSheet!AZ47', # Weapon 2 Dice range
		'CharSheet!BB47', # Weapon 2 Dice mod
		'CharSheet!BD47', # Weapon 2 Form property
		'CharSheet!BD48', # Weapon 2 Hand property
		'CharSheet!AK49', # Weapon 2 Slash true
		'CharSheet!AK51', # Weapon 2 Pierce true
		'CharSheet!AK53', # Weapon 2 Blunt true
		'CharSheet!AM49', # Weapon 2 Effect 1 Name
		'CharSheet!AM50', # Weapon 2 Effect 1 Cost
		'CharSheet!AT49', # Weapon 2 Effect 2 Name
		'CharSheet!AT50', # Weapon 2 Effect 2 Cost
		'CharSheet!AM51', # Weapon 2 Effect 3 Name
		'CharSheet!AM52', # Weapon 2 Effect 3 Cost
		'CharSheet!AT51', # Weapon 2 Effect 4 Name
		'CharSheet!AT52', # Weapon 2 Effect 4 Cost
		'CharSheet!AM53', # Weapon 2 Effect 5 Name
		'CharSheet!AM54', # Weapon 2 Effect 5 Cost
		'CharSheet!AT53', # Weapon 2 Effect 6 Name
		'CharSheet!AT54', # Weapon 2 Effect 6 Cost
		'CharSheet!AM55', # Weapon 2 Effect 7 Name
		'CharSheet!AM56', # Weapon 2 Effect 7 Cost
		'CharSheet!AT55', # Weapon 2 Effect 8 Name
		'CharSheet!AT56', # Weapon 2 Effect 8 Cost
		'CharSheet!AM57', # Weapon 2 Effect 9 Name
		'CharSheet!AM58', # Weapon 2 Effect 9 Cost
		'CharSheet!AT57', # Weapon 2 Effect 10 Name
		'CharSheet!AT58', # Weapon 2 Effect 10 Cost
		'CharSheet!BN48', # Weapon 2 Legal
		'CharSheet!B59', # Weapon 3 Name
		'CharSheet!O59', # Weapon 3 Melee true
		'CharSheet!O60', # Weapon 3 Range true
		'CharSheet!S59', # Weapon 3 Dice range
		'CharSheet!U59', # Weapon 3 Dice mod
		'CharSheet!W59', # Weapon 3 Form property
		'CharSheet!W60', # Weapon 3 Hand property
		'CharSheet!D61', # Weapon 3 Slash true
		'CharSheet!D63', # Weapon 3 Pierce true
		'CharSheet!D65', # Weapon 3 Blunt true
		'CharSheet!F61', # Weapon 3 Effect 1 Name
		'CharSheet!F62', # Weapon 3 Effect 1 Cost
		'CharSheet!M61', # Weapon 3 Effect 2 Name
		'CharSheet!M62', # Weapon 3 Effect 2 Cost
		'CharSheet!F63', # Weapon 3 Effect 3 Name
		'CharSheet!F64', # Weapon 3 Effect 3 Cost
		'CharSheet!M63', # Weapon 3 Effect 4 Name
		'CharSheet!M64', # Weapon 3 Effect 4 Cost
		'CharSheet!F65', # Weapon 3 Effect 5 Name
		'CharSheet!F66', # Weapon 3 Effect 5 Cost
		'CharSheet!M65', # Weapon 3 Effect 6 Name
		'CharSheet!M66', # Weapon 3 Effect 6 Cost
		'CharSheet!F67', # Weapon 3 Effect 7 Name
		'CharSheet!F68', # Weapon 3 Effect 7 Cost
		'CharSheet!M67', # Weapon 3 Effect 8 Name
		'CharSheet!M68', # Weapon 3 Effect 8 Cost
		'CharSheet!F69', # Weapon 3 Effect 9 Name
		'CharSheet!F70', # Weapon 3 Effect 9 Cost
		'CharSheet!M69', # Weapon 3 Effect 10 Name
		'CharSheet!M70', # Weapon 3 Effect 10 Cost
		'CharSheet!AG60', # Weapon 3 Legal
		'CharSheet!AI59', # Weapon 4 Name
		'CharSheet!AV59', # Weapon 4 Melee true
		'CharSheet!AV60', # Weapon 4 Range true
		'CharSheet!AZ59', # Weapon 4 Dice range
		'CharSheet!BB59', # Weapon 4 Dice mod
		'CharSheet!BD59', # Weapon 4 Form property
		'CharSheet!BD60', # Weapon 4 Hand property
		'CharSheet!AK61', # Weapon 4 Slash true
		'CharSheet!AK63', # Weapon 4 Pierce true
		'CharSheet!AK65', # Weapon 4 Blunt true
		'CharSheet!AM61', # Weapon 4 Effect 1 Name
		'CharSheet!AM62', # Weapon 4 Effect 1 Cost
		'CharSheet!AT61', # Weapon 4 Effect 2 Name
		'CharSheet!AT62', # Weapon 4 Effect 2 Cost
		'CharSheet!AM63', # Weapon 4 Effect 3 Name
		'CharSheet!AM64', # Weapon 4 Effect 3 Cost
		'CharSheet!AT63', # Weapon 4 Effect 4 Name
		'CharSheet!AT64', # Weapon 4 Effect 4 Cost
		'CharSheet!AM65', # Weapon 4 Effect 5 Name
		'CharSheet!AM66', # Weapon 4 Effect 5 Cost
		'CharSheet!AT65', # Weapon 4 Effect 6 Name
		'CharSheet!AT66', # Weapon 4 Effect 6 Cost
		'CharSheet!AM67', # Weapon 4 Effect 7 Name
		'CharSheet!AM68', # Weapon 4 Effect 7 Cost
		'CharSheet!AT67', # Weapon 4 Effect 8 Name
		'CharSheet!AT68', # Weapon 4 Effect 8 Cost
		'CharSheet!AM69', # Weapon 4 Effect 9 Name
		'CharSheet!AM70', # Weapon 4 Effect 9 Cost
		'CharSheet!AT69', # Weapon 4 Effect 10 Name
		'CharSheet!AT70', # Weapon 4 Effect 10 Cost
		'CharSheet!BN60', # Weapon 4 Legal
		'CharSheet!', # Outfit Name
		'CharSheet!', # Outfit Def range
		'CharSheet!', # Outfit Def mod
		'CharSheet!', # Outfit Evd range
		'CharSheet!', # Outfit Evd mod
		'CharSheet!', # Outfit Slash hp res
		'CharSheet!', # Outfit Slash stagger res
		'CharSheet!', # Outfit Pierce hp res
		'CharSheet!', # Outfit Pierce stagger res
		'CharSheet!', # Outfit Blunt hp res
		'CharSheet!', # Outfit Blunt stagger res
		'CharSheet!', # Outfit Effect 1 Name
		'CharSheet!', # Outfit Effect 1 Cost
		'CharSheet!', # Outfit Effect 2 Name
		'CharSheet!', # Outfit Effect 2 Cost
		'CharSheet!', # Outfit Effect 3 Name
		'CharSheet!', # Outfit Effect 3 Cost
		'CharSheet!', # Outfit Effect 4 Name
		'CharSheet!', # Outfit Effect 4 Cost
		'CharSheet!', # Outfit Effect 5 Name
		'CharSheet!', # Outfit Effect 5 Cost
		'CharSheet!', # Outfit Effect 6 Name
		'CharSheet!', # Outfit Effect 6 Cost
		'CharSheet!', # Outfit Effect 7 Name
		'CharSheet!', # Outfit Effect 7 Cost
		'CharSheet!', # Outfit Effect 8 Name
		'CharSheet!', # Outfit Effect 8 Cost
		'CharSheet!', # Outfit Effect 9 Name
		'CharSheet!', # Outfit Effect 9 Cost
		'CharSheet!', # Outfit Effect 10 Name
		'CharSheet!', # Outfit Effect 10 Cost
		'CharSheet!', # Outfit Legal
	]

def get_character_background():
	""" Gets character name, occupation, age, height, and avatar. """

	service.spreadsheets().value().batchGet()

def get_rank_and_level():
	""" Gets character rank, level, and exp. """

	<>

def get_character_stats():
	""" Gets character Fortitude, Prudence, Justice, Charm, Insight, and Temperance.
	Also, gets Att, Def, and Evd modifiers. """

	<>

def get_character_resources():
	""" Gets character health, stagger resistance, mentality, and light. """

	<>

def get_character_weapon():
	""" Gets character weapon details.
	Includes melee/range, dice, modifiers, size, type, damage type, and effects. """

	<>

def get_character_outfit():
	""" Gets character outfit details.
	Includes Def dice, Evd dice, damage resistances, stagger resistances, and effects. """

	<>

def get_character_tool():
	""" Gets character tool details.
	Includes portability, reusability, and effects. """

	<>

def get_character_augmentation():
	""" Gets character augmentation details.
	Includes type and effects. Does not include functional part support. """

	# TODO: Get functional part support.
	# Possibly as a multi-choice list that references the "Functional Part Repository"?

	<>

def get_character_skills():
	""" Gets character skill details.
	Includes type, dice, light cost, and effects. """

	<>
