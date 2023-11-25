import os, sys
from CombatBase import *
from Effects import *


#####   ----- Character Class -----   #####

class Character(characterBase):
    def __init__(self, name, hp, hp_Max, stagger, stagger_Max, sanity, sanity_Max, light, light_Max, stats, statuses) -> None:
        super().__init__(name, hp, hp_Max, stagger, stagger_Max, sanity, sanity_Max, light, light_Max, stats, statuses)

        self.statuses = statusEffect(statuses)

#####   ----- Import functions -----   #####
#TODO: implement from other files