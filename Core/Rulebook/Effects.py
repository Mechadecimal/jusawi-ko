import os, sys
from CombatBase import *

#####   ----- Status Effect List -----   #####

# TODO: implement remaining status effects AFTER getting a working clash and turn system

# burn
class burn(statusEffect):
    @classmethod
    def on_TURN_END(self):
        self.owner.hp -= self.potentcy
        self.count /= 2
        if (self.count <= 0):
            del self

# frostbite
class frostbite(statusEffect):
    @classmethod
    def on_TURN_END(self):
        self.owner.stagger -= self.potentcy
        self.count /= 2
        if (self.count <= 0):
            del self

# bleed
class bleed(statusEffect):
    @classmethod
    def on_ACTION_USED(self):
        self.owner.hp -= self.potentcy
        self.count /= 2
        if (self.count <= 0):
            del self
    def on_REACTION_USED(self):
        self.owner.hp -= self.potentcy
        self.count /= 2
        if (self.count <= 0):
            del self
    

# rupture
class rupture(statusEffect):
    @classmethod
    def on_ATTACKED(self):
        self.owner.hp -= self.potentcy
        del self
    def on_TURN_END(self):
        del self

# tremor
class tremor(statusEffect):
    @classmethod
    def on_ATTACKED(self):
        self.owner.stagger -= self.potentcy
        del self
    def on_TURN_END(self):
        del self

# poise and critical
class poise(statusEffect): # functionality includes critical handling
    pass

# ruin and devastation
class ruin(statusEffect): # functionality includes devastation handling
    pass

# paralysis
class paralysis(statusEffect): 
    pass

# protection, stagger protection, fragile, and stagger fragility
class protection(statusEffect): # functionality reused for stagger protection, fragile, and stagger fragility
    pass

# typed protection and typed fragility
class protection_typed(statusEffect): # functionality reused for typed fragility
    @classmethod
    def on_HIT(self):
        pass
    def on_TURN_END(self):
        del self
        

# strength and feeble
class strength(statusEffect): # functionality reused for feeble
    pass

# endurance and disarm
class endurance(statusEffect): # functionality reused for disarm
    pass

# haste and bind
class haste(statusEffect): # funcionality reused for bind
    pass

# smoke
class smoke(statusEffect):
    pass

# charge
class charge(statusEffect):
    pass

# mark
class mark(statusEffect):
    pass

# combo
class combo(statusEffect):
    pass

# staggered
class staggered(statusEffect):
    pass

# panic
class panic(statusEffect):
    pass

# defeated
class defeated(statusEffect):
    pass

#####   ----- Weapon Effects -----   #####

# dice power up
class dicePower(combatEffect):
    pass

# dice max up
class diceMax(combatEffect):
    pass

#####   ----- Outfit Effects -----   #####

#####   ----- Skill Effects -----   #####

#####   ----- Augment Effects -----   #####

#####   ----- Tool Effects -----   #####
#! tools can use skill effects as well !