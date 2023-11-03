import os, httplib2, re

from apiclient import discovery
from google.oauth2 import service_account

def get_character(url):
	try:
		scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
		secret_file = os.environ['VIRTUAL_ENV'] + os.path.join('/jusawi-ko-service-account.json')
		spreadsheet_id = re.findall("(d\/[a-zA-Z0-9-_]+)", url)[0].split('/')[1]
		credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scope)
		service = discovery.build('sheets', 'v4', credentials=credentials)
		RANGES = [
			'BioSheet!F4', # Character Name
			'BioSheet!F5', # Character Occupation
			'BioSheet!E6', # Character Age
			'BioSheet!M6', # Character Height

			'CharSheet!AS2', # Player Name

			'CharSheet!U21', # Character Rank
			'CharSheet!AB23', # Character Level
			'CharSheet!U23', # Character EXP

			'CharSheet!R13', # Character Fortitude
			'CharSheet!W13', # Character Prudence
			'CharSheet!AB13', # Character Justice
			'CharSheet!R20', # Character Charm
			'CharSheet!W20', # Character Insight
			'CharSheet!AB20', # Character Temperance

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

			'CharSheet!E84', # Tool 1 Name
			'CharSheet!Q84', # Tool 1 Portable
			'CharSheet!Q85', # Tool 1 Reusable
			'CharSheet!E85', # Tool 1 Effect 1 Name
			'CharSheet!E86', # Tool 1 Effect 1 Cost
			'CharSheet!E87', # Tool 1 Effect 2 Name
			'CharSheet!E88', # Tool 1 Effect 2 Cost
			'CharSheet!E89', # Tool 1 Effect 3 Name
			'CharSheet!E90', # Tool 1 Effect 3 Cost
			'CharSheet!E91', # Tool 1 Effect 4 Name
			'CharSheet!E92', # Tool 1 Effect 4 Cost
			'CharSheet!E93', # Tool 1 Effect 5 Name
			'CharSheet!E94', # Tool 1 Effect 5 Cost
			'CharSheet!E95', # Tool 1 Effect 6 Name
			'CharSheet!E96', # Tool 1 Effect 6 Cost
			'CharSheet!R95', # Tool 1 Points max
			'CharSheet!R96', # Tool 1 Points used

			'CharSheet!U84', # Tool 2 Name
			'CharSheet!AG84', # Tool 2 Portable
			'CharSheet!AG85', # Tool 2 Reusable
			'CharSheet!U85', # Tool 2 Effect 1 Name
			'CharSheet!U86', # Tool 2 Effect 1 Cost
			'CharSheet!U87', # Tool 2 Effect 2 Name
			'CharSheet!U88', # Tool 2 Effect 2 Cost
			'CharSheet!U89', # Tool 2 Effect 3 Name
			'CharSheet!U90', # Tool 2 Effect 3 Cost
			'CharSheet!U91', # Tool 2 Effect 4 Name
			'CharSheet!U92', # Tool 2 Effect 4 Cost
			'CharSheet!U93', # Tool 2 Effect 5 Name
			'CharSheet!U94', # Tool 2 Effect 5 Cost
			'CharSheet!U95', # Tool 2 Effect 6 Name
			'CharSheet!U96', # Tool 2 Effect 6 Cost
			'CharSheet!AH95', # Tool 2 Points max
			'CharSheet!AH96', # Tool 2 Points used

			'CharSheet!AK84', # Tool 3 Name
			'CharSheet!AW84', # Tool 3 Portable
			'CharSheet!AW85', # Tool 3 Reusable
			'CharSheet!AK85', # Tool 3 Effect 1 Name
			'CharSheet!AK86', # Tool 3 Effect 1 Cost
			'CharSheet!AK87', # Tool 3 Effect 2 Name
			'CharSheet!AK88', # Tool 3 Effect 2 Cost
			'CharSheet!AK89', # Tool 3 Effect 3 Name
			'CharSheet!AK90', # Tool 3 Effect 3 Cost
			'CharSheet!AK91', # Tool 3 Effect 4 Name
			'CharSheet!AK92', # Tool 3 Effect 4 Cost
			'CharSheet!AK93', # Tool 3 Effect 5 Name
			'CharSheet!AK94', # Tool 3 Effect 5 Cost
			'CharSheet!AK95', # Tool 3 Effect 6 Name
			'CharSheet!AK96', # Tool 3 Effect 6 Cost
			'CharSheet!AX95', # Tool 3 Points max
			'CharSheet!X96', # Tool 3 Points used

			'CharSheet!BA84', # Tool 4 Name
			'CharSheet!BM84', # Tool 4 Portable
			'CharSheet!BM85', # Tool 4 Reusable
			'CharSheet!BA85', # Tool 4 Effect 1 Name
			'CharSheet!BA86', # Tool 4 Effect 1 Cost
			'CharSheet!BA87', # Tool 4 Effect 2 Name
			'CharSheet!BA88', # Tool 4 Effect 2 Cost
			'CharSheet!BA89', # Tool 4 Effect 3 Name
			'CharSheet!BA90', # Tool 4 Effect 3 Cost
			'CharSheet!BA91', # Tool 4 Effect 4 Name
			'CharSheet!BA92', # Tool 4 Effect 4 Cost
			'CharSheet!BA93', # Tool 4 Effect 5 Name
			'CharSheet!BA94', # Tool 4 Effect 5 Cost
			'CharSheet!BA95', # Tool 4 Effect 6 Name
			'CharSheet!BA96', # Tool 4 Effect 6 Cost
			'CharSheet!BN95', # Tool 4 Points max
			'CharSheet!BN96', # Tool 4 Points used

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

			'CharSheet!C113', # Skill 1 Name
			'CharSheet!X113', # Skill 1 Type
			'CharSheet!M113', # Skill 1 Dice range
			'CharSheet!O113', # Skill 1 Dice mod
			'CharSheet!S113', # Skill 1 Light cost
			'CharSheet!C115', # Skill 1 Effect 1 Name
			'CharSheet!C116', # Skill 1 Effect 1 Cost
			'CharSheet!J115', # Skill 1 Effect 2 Name
			'CharSheet!J116', # Skill 1 Effect 2 Cost
			'CharSheet!C117', # Skill 1 Effect 3 Name
			'CharSheet!C118', # Skill 1 Effect 3 Cost
			'CharSheet!J117', # Skill 1 Effect 4 Name
			'CharSheet!J118', # Skill 1 Effect 4 Cost
			'CharSheet!C119', # Skill 1 Effect 5 Name
			'CharSheet!C120', # Skill 1 Effect 5 Cost
			'CharSheet!J119', # Skill 1 Effect 6 Name
			'CharSheet!J120', # Skill 1 Effect 6 Cost
			'CharSheet!C121', # Skill 1 Effect 7 Name
			'CharSheet!C122', # Skill 1 Effect 7 Cost
			'CharSheet!J121', # Skill 1 Effect 8 Name
			'CharSheet!J122', # Skill 1 Effect 8 Cost
			'CharSheet!C123', # Skill 1 Effect 9 Name
			'CharSheet!C124', # Skill 1 Effect 9 Cost
			'CharSheet!J123', # Skill 1 Effect 10 Name
			'CharSheet!J124', # Skill 1 Effect 10 Cost
			'CharSheet!AA114', # Skill 1 Legal

			'CharSheet!AC113', # Skill 2 Name
			'CharSheet!AX113', # Skill 2 Type
			'CharSheet!AM113', # Skill 2 Dice range
			'CharSheet!AO113', # Skill 2 Dice mod
			'CharSheet!AS113', # Skill 2 Light cost
			'CharSheet!AC115', # Skill 2 Effect 1 Name
			'CharSheet!AC116', # Skill 2 Effect 1 Cost
			'CharSheet!AJ115', # Skill 2 Effect 2 Name
			'CharSheet!AJ116', # Skill 2 Effect 2 Cost
			'CharSheet!AC117', # Skill 2 Effect 3 Name
			'CharSheet!AC118', # Skill 2 Effect 3 Cost
			'CharSheet!AJ117', # Skill 2 Effect 4 Name
			'CharSheet!AJ118', # Skill 2 Effect 4 Cost
			'CharSheet!AC119', # Skill 2 Effect 5 Name
			'CharSheet!AC120', # Skill 2 Effect 5 Cost
			'CharSheet!AJ119', # Skill 2 Effect 6 Name
			'CharSheet!AJ120', # Skill 2 Effect 6 Cost
			'CharSheet!AC121', # Skill 2 Effect 7 Name
			'CharSheet!AC122', # Skill 2 Effect 7 Cost
			'CharSheet!AJ121', # Skill 2 Effect 8 Name
			'CharSheet!AJ122', # Skill 2 Effect 8 Cost
			'CharSheet!AC123', # Skill 2 Effect 9 Name
			'CharSheet!AC124', # Skill 2 Effect 9 Cost
			'CharSheet!AJ123', # Skill 2 Effect 10 Name
			'CharSheet!AJ124', # Skill 2 Effect 10 Cost
			'CharSheet!BA114', # Skill 2 Legal

			'CharSheet!C125', # Skill 3 Name
			'CharSheet!X125', # Skill 3 Type
			'CharSheet!M125', # Skill 3 Dice range
			'CharSheet!O125', # Skill 3 Dice mod
			'CharSheet!S125', # Skill 3 Light cost
			'CharSheet!C127', # Skill 3 Effect 1 Name
			'CharSheet!C128', # Skill 3 Effect 1 Cost
			'CharSheet!J127', # Skill 3 Effect 2 Name
			'CharSheet!J128', # Skill 3 Effect 2 Cost
			'CharSheet!C129', # Skill 3 Effect 3 Name
			'CharSheet!C130', # Skill 3 Effect 3 Cost
			'CharSheet!J129', # Skill 3 Effect 4 Name
			'CharSheet!J130', # Skill 3 Effect 4 Cost
			'CharSheet!C131', # Skill 3 Effect 5 Name
			'CharSheet!C132', # Skill 3 Effect 5 Cost
			'CharSheet!J131', # Skill 3 Effect 6 Name
			'CharSheet!J132', # Skill 3 Effect 6 Cost
			'CharSheet!C133', # Skill 3 Effect 7 Name
			'CharSheet!C134', # Skill 3 Effect 7 Cost
			'CharSheet!J133', # Skill 3 Effect 8 Name
			'CharSheet!J134', # Skill 3 Effect 8 Cost
			'CharSheet!C135', # Skill 3 Effect 9 Name
			'CharSheet!C136', # Skill 3 Effect 9 Cost
			'CharSheet!J135', # Skill 3 Effect 10 Name
			'CharSheet!J136', # Skill 3 Effect 10 Cost
			'CharSheet!AA126', # Skill 3 Legal

			'CharSheet!AC125', # Skill 4 Name
			'CharSheet!AX125', # Skill 4 Type
			'CharSheet!AM125', # Skill 4 Dice range
			'CharSheet!AO125', # Skill 4 Dice mod
			'CharSheet!AS125', # Skill 4 Light cost
			'CharSheet!AC127', # Skill 4 Effect 1 Name
			'CharSheet!AC128', # Skill 4 Effect 1 Cost
			'CharSheet!AJ127', # Skill 4 Effect 2 Name
			'CharSheet!AJ128', # Skill 4 Effect 2 Cost
			'CharSheet!AC129', # Skill 4 Effect 3 Name
			'CharSheet!AC130', # Skill 4 Effect 3 Cost
			'CharSheet!AJ129', # Skill 4 Effect 4 Name
			'CharSheet!AJ130', # Skill 4 Effect 4 Cost
			'CharSheet!AC131', # Skill 4 Effect 5 Name
			'CharSheet!AC132', # Skill 4 Effect 5 Cost
			'CharSheet!AJ131', # Skill 4 Effect 6 Name
			'CharSheet!AJ132', # Skill 4 Effect 6 Cost
			'CharSheet!AC133', # Skill 4 Effect 7 Name
			'CharSheet!AC134', # Skill 4 Effect 7 Cost
			'CharSheet!AJ133', # Skill 4 Effect 8 Name
			'CharSheet!AJ134', # Skill 4 Effect 8 Cost
			'CharSheet!AC135', # Skill 4 Effect 9 Name
			'CharSheet!AC136', # Skill 4 Effect 9 Cost
			'CharSheet!AJ135', # Skill 4 Effect 10 Name
			'CharSheet!AJ136', # Skill 4 Effect 10 Cost
			'CharSheet!BA126', # Skill 4 Legal

			'CharSheet!C137', # Skill 5 Name
			'CharSheet!X137', # Skill 5 Type
			'CharSheet!M137', # Skill 5 Dice range
			'CharSheet!O137', # Skill 5 Dice mod
			'CharSheet!S137', # Skill 5 Light cost
			'CharSheet!C139', # Skill 5 Effect 1 Name
			'CharSheet!C140', # Skill 5 Effect 1 Cost
			'CharSheet!J139', # Skill 5 Effect 2 Name
			'CharSheet!J140', # Skill 5 Effect 2 Cost
			'CharSheet!C141', # Skill 5 Effect 3 Name
			'CharSheet!C142', # Skill 5 Effect 3 Cost
			'CharSheet!J141', # Skill 5 Effect 4 Name
			'CharSheet!J142', # Skill 5 Effect 4 Cost
			'CharSheet!C143', # Skill 5 Effect 5 Name
			'CharSheet!C144', # Skill 5 Effect 5 Cost
			'CharSheet!J143', # Skill 5 Effect 6 Name
			'CharSheet!J144', # Skill 5 Effect 6 Cost
			'CharSheet!C145', # Skill 5 Effect 7 Name
			'CharSheet!C146', # Skill 5 Effect 7 Cost
			'CharSheet!J145', # Skill 5 Effect 8 Name
			'CharSheet!J146', # Skill 5 Effect 8 Cost
			'CharSheet!C147', # Skill 5 Effect 9 Name
			'CharSheet!C148', # Skill 5 Effect 9 Cost
			'CharSheet!J147', # Skill 5 Effect 10 Name
			'CharSheet!J148', # Skill 5 Effect 10 Cost
			'CharSheet!AA138', # Skill 5 Legal

			'CharSheet!AC137', # Skill 6 Name
			'CharSheet!AX137', # Skill 6 Type
			'CharSheet!AM137', # Skill 6 Dice range
			'CharSheet!AO137', # Skill 6 Dice mod
			'CharSheet!AS137', # Skill 6 Light cost
			'CharSheet!AC139', # Skill 6 Effect 1 Name
			'CharSheet!AC140', # Skill 6 Effect 1 Cost
			'CharSheet!AJ139', # Skill 6 Effect 2 Name
			'CharSheet!AJ140', # Skill 6 Effect 2 Cost
			'CharSheet!AC141', # Skill 6 Effect 3 Name
			'CharSheet!AC142', # Skill 6 Effect 3 Cost
			'CharSheet!AJ141', # Skill 6 Effect 4 Name
			'CharSheet!AJ142', # Skill 6 Effect 4 Cost
			'CharSheet!AC143', # Skill 6 Effect 5 Name
			'CharSheet!AC144', # Skill 6 Effect 5 Cost
			'CharSheet!AJ143', # Skill 6 Effect 6 Name
			'CharSheet!AJ144', # Skill 6 Effect 6 Cost
			'CharSheet!AC145', # Skill 6 Effect 7 Name
			'CharSheet!AC146', # Skill 6 Effect 7 Cost
			'CharSheet!AJ145', # Skill 6 Effect 8 Name
			'CharSheet!AJ146', # Skill 6 Effect 8 Cost
			'CharSheet!AC147', # Skill 6 Effect 9 Name
			'CharSheet!AC148', # Skill 6 Effect 9 Cost
			'CharSheet!AJ147', # Skill 5 Effect 10 Name
			'CharSheet!AJ148', # Skill 6 Effect 10 Cost
			'CharSheet!BA138', # Skill 6 Legal
		]

		character = service.spreadsheets().values().batchGet(spreadsheetId = spreadsheet_id, ranges = RANGES).execute()

		charid = character['spreadsheetId']
		charval = character['valueRanges']

		templist = []

		for i in charval:
			if i.get('values'):
				i = i['values'][0][0]
			else:
				i = None
			print(i)
			templist.append(i)

		charval = templist

		tempdict = {charid: charval}

		return tempdict

	except Exception as e:
		print(e)
		return e
