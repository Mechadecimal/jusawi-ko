import os, httplib2

from apiclient import discovery
from google.oauth2 import service_account

try:
	scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
	secret_file = os.path.join(os.cwd(), 'jusawi-ko-service-account.json')
	credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scope)
	service = discovery.build('sheets', 'v4', credentials=credentials)

except
def get_character_background():
	""" Gets character name, occupation, age, height, and avatar. """

	<>

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
