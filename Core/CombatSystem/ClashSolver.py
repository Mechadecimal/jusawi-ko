import os, sys
from ..Rulebook.CombatBase import *
from ..Rulebook.Effects import *


# ClashSolver is a helper class which resolves and logs attacks and clashes
class ClashSolver:
	def __init__(self, attacker, attacker_action, defender, defender_action, combatLog) -> None:
		self.attacker = characterBase(attacker)
		self.attacker_action = combatAction(attacker_action)
		self.defender = characterBase(defender)
		self.defender_action = combatAction(defender_action)
		self.combatLog = combatLog

	@classmethod
	def iterateClash(self) -> bool:
		#TODO: implement
		return True

	def solve(self):
		#TODO: implement
		pass
