import os, sys

class Combatant:
	def __init__(self, char, hp, stagger, sanity, light, speed, actions, reactions, status)
		self.char = char
		self.hp = hp
		self.stagger = stagger
		self.sanity = sanity
		self.light = light
		self.speed = speed
		self.actions = actions
		self.reactions = reactions
		self.status = status

class Combat:
	def __init__(self, channel, combatants, round, surprise):
		self.channel = channel
		self.combatants = combatants
		self.round = round
		self.surprise = surprise

	def combat_begin(self):
		# Somehow...

	def combat_join(self):
		# Join combat with standard rule (CR 3.0)
		# Remember that joining during mid-combat is permitted, but will have to take their first move last

	def action(self):
		# Melee Attack
		# Ranged Attack
		# Protect
		# Reduce Status
		# Dash
		# Disengage
		# Use Tool
		# Grapple
		# Take Cover
		# Hide
		# Change Weapons
		# Convert to Reaction
		# Delay

		# Somehow give prompt to target for Clash
		# One-sided is Clash Win
		# Tie si do again --> recursively call action()?

	def reaction(self):
		# Do you want to react to <Action>?
		# Button: yes/no
		# On yes: do block/counter/evade
		# Special case: Opportunity attack

	def combat_end(self):
		# Only initiator can end
