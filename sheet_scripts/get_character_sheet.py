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
		'BioSheet!F4', # Character Name
		'BioSheet!F5', # Character Occupation
		'BioSheet!E6', # Character Age
		'BioSheet!M6', # Character Height
		'CharSheet!B7', # Character Image
		'CharSheet!AS2', # Player Name
		'CharSheet!U21', # Character Rank
		'CharSheet!AB23', # Character Level
		'CharSheet!U23', # Character EXP
		'CharSheet!R13', # Character Fortitude
		'CharSheet!W13', # Character Prudence
		'CharSheet!AB13', # Character Justice
		'CharSheet!R20', # Character Charm
		'CharSheet!W20', # Character Insight
		'CharSheet!AB20', # CharacterTemperance
		'CharSheet!AO5', # Character Health max
		'CharSheet!AZ5', # Character Stagger res nax
		'CharSheet!AO7', # Character Mentality max
		'CharSheet!AZ7', # Character Light max
		'CharSheet!AJ9', # Character Att
		'CharSheet!AQ9', # Character Def
		'CharSheet!AX9', # Character Evd
		'CharSheet!BM42', # Character Weapon effect slot amount
		'CharSheet!BM43', # Character Outfit effect slot amount
		'CharSheet!BM44', # Character Augment effect slot amount
		'CharSheet!BM45', # Character Skill effect slot amount
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
		'CharSheet!B72', # Outfit Name
		'CharSheet!AJ72', # Outfit Def range
		'CharSheet!AL72', # Outfit Def mod
		'CharSheet!AP72', # Outfit Evd range
		'CharSheet!AR72', # Outfit Evd mod
		'CharSheet!D73', # Outfit Slash hp res
		'CharSheet!H73', # Outfit Slash stagger res
		'CharSheet!D75', # Outfit Pierce hp res
		'CharSheet!H75', # Outfit Pierce stagger res
		'CharSheet!D77', # Outfit Blunt hp res
		'CharSheet!H77', # Outfit Blunt stagger res
		'CharSheet!L73', # Outfit Effect 1 Name
		'CharSheet!L74', # Outfit Effect 1 Cost
		'CharSheet!S73', # Outfit Effect 2 Name
		'CharSheet!S74', # Outfit Effect 2 Cost
		'CharSheet!L75', # Outfit Effect 3 Name
		'CharSheet!L76', # Outfit Effect 3 Cost
		'CharSheet!S75', # Outfit Effect 4 Name
		'CharSheet!S76', # Outfit Effect 4 Cost
		'CharSheet!L77', # Outfit Effect 5 Name
		'CharSheet!L78', # Outfit Effect 5 Cost
		'CharSheet!S77', # Outfit Effect 6 Name
		'CharSheet!S78', # Outfit Effect 6 Cost
		'CharSheet!L79', # Outfit Effect 7 Name
		'CharSheet!L80', # Outfit Effect 7 Cost
		'CharSheet!S79', # Outfit Effect 8 Name
		'CharSheet!S80', # Outfit Effect 8 Cost
		'CharSheet!L81', # Outfit Effect 9 Name
		'CharSheet!L82', # Outfit Effect 9 Cost
		'CharSheet!S81', # Outfit Effect 10 Name
		'CharSheet!S82', # Outfit Effect 10 Cost
		'CharSheet!BI72', # Outfit Legal
		'CharSheet!B100', # Augment Name
		'CharSheet!Y100', # Augment Type
		'CharSheet!AF101', # Augment Effect 1 Name
		'CharSheet!AF102', # Augment Effect 1 Cost
		'CharSheet!AM101', # Augment Effect 2 Name
		'CharSheet!AM102', # Augment Effect 2 Cost
		'CharSheet!AF103', # Augment Effect 3 Name
		'CharSheet!AF104', # Augment Effect 3 Cost
		'CharSheet!AM103', # Augment Effect 4 Name
		'CharSheet!AM104', # Augment Effect 4 Cost
		'CharSheet!AF105', # Augment Effect 5 Name
		'CharSheet!AF106', # Augment Effect 5 Cost
		'CharSheet!AM105', # Augment Effect 6 Name
		'CharSheet!AM106', # Augment Effect 6 Cost
		'CharSheet!AF107', # Augment Effect 7 Name
		'CharSheet!AF108', # Augment Effect 7 Cost
		'CharSheet!AM107', # Augment Effect 8 Name
		'CharSheet!AM108', # Augment Effect 8 Cost
		'CharSheet!AF109', # Augment Effect 9 Name
		'CharSheet!AF110', # Augment Effect 9 Cost
		'CharSheet!AM109', # Augment Effect 10 Name
		'CharSheet!AM110', # Augment Effect 10 Cost
		'CharSheet!BA100', # Augment Legal
		'CharSheet!C80', # Skill 1 Name
		'CharSheet!X80', # Skill 1 Type
		'CharSheet!M80', # Skill 1 Dice range
		'CharSheet!O80', # Skill 1 Dice mod
		'CharSheet!S80', # Skill 1 Light cost
		'CharSheet!C82', # Skill 1 Effect 1 Name
		'CharSheet!C83', # Skill 1 Effect 1 Cost
		'CharSheet!J82', # Skill 1 Effect 2 Name
		'CharSheet!J83', # Skill 1 Effect 2 Cost
		'CharSheet!C84', # Skill 1 Effect 3 Name
		'CharSheet!C85', # Skill 1 Effect 3 Cost
		'CharSheet!J84', # Skill 1 Effect 4 Name
		'CharSheet!J85', # Skill 1 Effect 4 Cost
		'CharSheet!C86', # Skill 1 Effect 5 Name
		'CharSheet!C87', # Skill 1 Effect 5 Cost
		'CharSheet!J86', # Skill 1 Effect 6 Name
		'CharSheet!J87', # Skill 1 Effect 6 Cost
		'CharSheet!C88', # Skill 1 Effect 7 Name
		'CharSheet!C89', # Skill 1 Effect 7 Cost
		'CharSheet!J88', # Skill 1 Effect 8 Name
		'CharSheet!J89', # Skill 1 Effect 8 Cost
		'CharSheet!C90', # Skill 1 Effect 9 Name
		'CharSheet!C91', # Skill 1 Effect 9 Cost
		'CharSheet!J90', # Skill 1 Effect 10 Name
		'CharSheet!J91', # Skill 1 Effect 10 Cost
		'CharSheet!', # Skill 1 Legal
		'CharSheet!', # Skill 2 Name
		'CharSheet!', # Skill 2 Type
		'CharSheet!', # Skill 2 Dice range
		'CharSheet!', # Skill 2 Dice mod
		'CharSheet', # Skill 2 Light cost
		'CharSheet!', # Skill 2 Effect 1 Name
		'CharSheet!', # Skill 2 Effect 1 Cost
		'CharSheet!', # Skill 2 Effect 2 Name
		'CharSheet!', # Skill 2 Effect 2 Cost
		'CharSheet!', # Skill 2 Effect 3 Name
		'CharSheet!', # Skill 2 Effect 3 Cost
		'CharSheet!', # Skill 2 Effect 4 Name
		'CharSheet!', # Skill 2 Effect 4 Cost
		'CharSheet!', # Skill 2 Effect 5 Name
		'CharSheet!', # Skill 2 Effect 5 Cost
		'CharSheet!', # Skill 2 Effect 6 Name
		'CharSheet!', # Skill 2 Effect 6 Cost
		'CharSheet!', # Skill 2 Effect 7 Name
		'CharSheet!', # Skill 2 Effect 7 Cost
		'CharSheet!', # Skill 2 Effect 8 Name
		'CharSheet!', # Skill 2 Effect 8 Cost
		'CharSheet!', # Skill 2 Effect 9 Name
		'CharSheet!', # Skill 2 Effect 9 Cost
		'CharSheet!', # Skill 2 Effect 10 Name
		'CharSheet!', # Skill 2 Effect 10 Cost
		'CharSheet!', # Skill 2 Legal
		'CharSheet!', # Skill 3 Name
		'CharSheet!', # Skill 3 Type
		'CharSheet!', # Skill 3 Dice range
		'CharSheet!', # Skill 3 Dice mod
		'CharSheet!', # Skill 3 Light cost
		'CharSheet!', # Skill 3 Effect 1 Name
		'CharSheet!', # Skill 3 Effect 1 Cost
		'CharSheet!', # Skill 3 Effect 2 Name
		'CharSheet!', # Skill 3 Effect 2 Cost
		'CharSheet!', # Skill 3 Effect 3 Name
		'CharSheet!', # Skill 3 Effect 3 Cost
		'CharSheet!', # Skill 3 Effect 4 Name
		'CharSheet!', # Skill 3 Effect 4 Cost
		'CharSheet!', # Skill 3 Effect 5 Name
		'CharSheet!', # Skill 3 Effect 5 Cost
		'CharSheet!', # Skill 3 Effect 6 Name
		'CharSheet!', # Skill 3 Effect 6 Cost
		'CharSheet!', # Skill 3 Effect 7 Name
		'CharSheet!', # Skill 3 Effect 7 Cost
		'CharSheet!', # Skill 3 Effect 8 Name
		'CharSheet!', # Skill 3 Effect 8 Cost
		'CharSheet!', # Skill 3 Effect 9 Name
		'CharSheet!', # Skill 3 Effect 9 Cost
		'CharSheet!', # Skill 3 Effect 10 Name
		'CharSheet!', # Skill 3 Effect 10 Cost
		'CharSheet!', # Skill 3 Legal
		'CharSheet!', # Skill 4 Name
		'CharSheet!', # Skill 4 Type
		'CharSheet!', # Skill 4 Dice range
		'CharSheet!', # Skill 4 Dice mod
		'CharSheet!', # Skill 4 Light cost
		'CharSheet!', # Skill 4 Effect 1 Name
		'CharSheet!', # Skill 4 Effect 1 Cost
		'CharSheet!', # Skill 4 Effect 2 Name
		'CharSheet!', # Skill 4 Effect 2 Cost
		'CharSheet!', # Skill 4 Effect 3 Name
		'CharSheet!', # Skill 4 Effect 3 Cost
		'CharSheet!', # Skill 4 Effect 4 Name
		'CharSheet!', # Skill 4 Effect 4 Cost
		'CharSheet!', # Skill 4 Effect 5 Name
		'CharSheet!', # Skill 4 Effect 5 Cost
		'CharSheet!', # Skill 4 Effect 6 Name
		'CharSheet!', # Skill 4 Effect 6 Cost
		'CharSheet!', # Skill 4 Effect 7 Name
		'CharSheet!', # Skill 4 Effect 7 Cost
		'CharSheet!', # Skill 4 Effect 8 Name
		'CharSheet!', # Skill 4 Effect 8 Cost
		'CharSheet!', # Skill 4 Effect 9 Name
		'CharSheet!', # Skill 4 Effect 9 Cost
		'CharSheet!', # Skill 4 Effect 10 Name
		'CharSheet!', # Skill 4 Effect 10 Cost
		'CharSheet!', # Skill 4 Legal
		'CharSheet!', # Skill 5 Name
		'CharSheet!', # Skill 5 Type
		'CharSheet!', # Skill 5 Dice range
		'CharSheet!', # Skill 5 Dice mod
		'CharSheet!', # Skill 5 Light cost
		'CharSheet!', # Skill 5 Effect 1 Name
		'CharSheet!', # Skill 5 Effect 1 Cost
		'CharSheet!', # Skill 5 Effect 2 Name
		'CharSheet!', # Skill 5 Effect 2 Cost
		'CharSheet!', # Skill 5 Effect 3 Name
		'CharSheet!', # Skill 5 Effect 3 Cost
		'CharSheet!', # Skill 5 Effect 4 Name
		'CharSheet!', # Skill 5 Effect 4 Cost
		'CharSheet!', # Skill 5 Effect 5 Name
		'CharSheet!', # Skill 5 Effect 5 Cost
		'CharSheet!', # Skill 5 Effect 6 Name
		'CharSheet!', # Skill 5 Effect 6 Cost
		'CharSheet!', # Skill 5 Effect 7 Name
		'CharSheet!', # Skill 5 Effect 7 Cost
		'CharSheet!', # Skill 5 Effect 8 Name
		'CharSheet!', # Skill 5 Effect 8 Cost
		'CharSheet!', # Skill 5 Effect 9 Name
		'CharSheet!', # Skill 5 Effect 9 Cost
		'CharSheet!', # Skill 5 Effect 10 Name
		'CharSheet!', # Skill 5 Effect 10 Cost
		'CharSheet!', # Skill 5 Legal
		'CharSheet!', # Skill 6 Name
		'CharSheet!', # Skill 6 Type
		'CharSheet!', # Skill 6 Dice range
		'CharSheet!', # Skill 6 Dice mod
		'CharSheet!', # Skill 6 Light cost
		'CharSheet!', # Skill 6 Effect 1 Name
		'CharSheet!', # Skill 6 Effect 1 Cost
		'CharSheet!', # Skill 6 Effect 2 Name
		'CharSheet!', # Skill 6 Effect 2 Cost
		'CharSheet!', # Skill 6 Effect 3 Name
		'CharSheet!', # Skill 6 Effect 3 Cost
		'CharSheet!', # Skill 6 Effect 4 Name
		'CharSheet!', # Skill 6 Effect 4 Cost
		'CharSheet!', # Skill 6 Effect 5 Name
		'CharSheet!', # Skill 6 Effect 5 Cost
		'CharSheet!', # Skill 6 Effect 6 Name
		'CharSheet!', # Skill 6 Effect 6 Cost
		'CharSheet!', # Skill 6 Effect 7 Name
		'CharSheet!', # Skill 6 Effect 7 Cost
		'CharSheet!', # Skill 6 Effect 8 Name
		'CharSheet!', # Skill 6 Effect 8 Cost
		'CharSheet!', # Skill 6 Effect 9 Name
		'CharSheet!', # Skill 6 Effect 9 Cost
		'CharSheet!', # Skill 5 Effect 10 Name
		'CharSheet!', # Skill 6 Effect 10 Cost
		'CharSheet!', # Skill 6 Legal
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
