import os, sys
from enum import Enum

#####   ----- Combat Base Classes -----   #####

# Enumeration for combat events
class CombatEvents(Enum):
    TURN_START    = 0
    TURN_END      = 1
    COMBAT_START  = 2
    COMBAT_END    = 3
    ACTION_USED   = 4
    REACTION_USED = 5
    CLASH_START   = 6
    CLASH_END     = 7
    CLASH_WIN     = 8
    CLASH_LOSE    = 9
    HIT           = 10
    DEFEND        = 11
    EVADE         = 12
    ATTACKED      = 13

# Enumeration for damage types
# TODO: Add remaining damage types
class DamageTypes(Enum):
    TRUE             = 0
    SLASH            = 1
    PIERCE           = 2
    BLUNT            = 3
    STATUS           = 4
    BURN             = 5
    BLEED            = 6
    RUIN             = 7
    RUIN_DEVASTATION = 8
    RUPTURE          = 9
    FALL             = 10
    EFFECT           = 11

# Enumeration for combat action types
class combatActionType(Enum):
    ATTACK = 0
    DEFEND = 1
    EVADE  = 2
    NONE   = 3

# CombatEffect is an abstract class that should not be used directly
# Override these functions in child classes to add effects to their respective delegate events
class combatEffect:
    def __init__(self) -> None:
        pass
        
    @classmethod
    def on_TURN_START(self) -> None:
        pass
    def on_TURN_END(self) -> None:
        pass
    def on_COMBAT_START(self) -> None:
        pass
    def on_COMBAT_END(self) -> None:
        pass
    def on_ACTION_USED(self) -> None:
        pass
    def on_REACTION_USED(self) -> None:
        pass
    def on_CLASH_START(self) -> None:
        pass
    def on_CLASH_END(self) -> None:
        pass     
    def on_CLASH_WIN(self) -> None:
        pass
    def on_CLASH_LOSE(self) -> None:
        pass
    def on_HIT(self) -> None:
        pass
    def on_DEFEND(self) -> None:
        pass
    def on_EVADE(self) -> None:
        pass
    def on_ATTACKED(self) -> None:
        pass

    def useEvent(self, event: CombatEvents) -> None:
        #TODO: if this throws an error, update to python 3.10 or newer to use switch cases
        match event:
            case CombatEvents.TURN_START:
                self.on_TURN_START()
            case CombatEvents.TURN_END:
                self.on_TURN_END()
            case CombatEvents.COMBAT_START:
                self.on_COMBAT_START()
            case CombatEvents.COMBAT_END:
                self.on_COMBAT_END()
            case CombatEvents.ACTION_USED:
                self.on_ACTION_USED()
            case CombatEvents.REACTION_USED:
                self.on_REACTION_USED()
            case CombatEvents.CLASH_START:
                self.on_CLASH_START()
            case CombatEvents.CLASH_END:
                self.on_CLASH_END()
            case CombatEvents.CLASH_WIN:
                self.on_CLASH_WIN()
            case CombatEvents.CLASH_LOSE:
                self.on_CLASH_LOSE()
            case CombatEvents.HIT:
                self.on_HIT()
            case CombatEvents.DEFEND:
                self.on_DEFEND()
            case CombatEvents.EVADE:
                self.on_EVADE()
            case CombatEvents.ATTACKED:
                self.on_ATTACKED()
            case _:
                pass



#####   ----- Status Base Class -----   #####

# StatusBase is an abstract class that should not be used directly
# It is used as a base for status effects, and other lingering effects
# This class should be seen by the characterBase class to allow for multi-status interactions
class statusBase(combatEffect):
    def __init__(self, potentcy, count, isBeneficial, persistance) -> None:
        super.__init__(self)
        self.potentcy = int(potentcy)               # the potency of the status' effects
        self.count = int(count)                     # the number of times the effect is applied
        self.isBeneficial = bool(isBeneficial)      # whether the status is beneficial (a buff) or not (a debuff)
        self.persistance = int(persistance)         # how hard the debuff is to remove through external means; -1 cannot remove
        

    @classmethod
    def on_Entry(self) -> None:                   # effects that are activated once on application of the status
        pass
    def on_Removal(self) -> None:                 # effects that are activated once on removal of the status
        pass   
    def __del__(self) -> None:
        self.on_Removal()



#####   ----- Item Base Classes -----   #####

class usableItem:
    def __init__(self, uses, skillEffects_Combat) -> None:
        self.uses = int(uses)                                                # cannot use if uses are equal to zero; -1 means infinite uses
        self.skillEffects_Combat = combatEffect(skillEffects_Combat)         # wrapper for activatable effects

class weapon(usableItem):
    def __init__(self, uses, skillEffects_Combat, damageType, diceModifier, diceMax, attackRange) -> None:
        super.__init__(uses, skillEffects_Combat)
        self.damageType   = damageType
        self.diceModifier = int(diceModifier)
        self.diceMax      = int(diceMax)
        self.attackRange  = int(attackRange)

        self.uses = -1
    
    @classmethod
    def use(self):
        pass

class outfit(usableItem):
    def __init__(self, uses, skillEffects_Combat, hpResistances, stgResistances) -> None:
        super.__init__(self, uses, skillEffects_Combat)
        self.hpResistances = hpResistances
        self.stgResistances = stgResistances

        self.uses = -1

class augment(usableItem):
    def __init__(self, uses, skillEffects_Combat) -> None:
        super.__init__(self, uses, skillEffects_Combat)
        self.uses = -1

class ammunition(usableItem):
    def __init__(self, uses, skillEffects_Combat) -> None:
        super.__init__(uses, skillEffects_Combat)

class weapon_ranged(weapon):
    def __init__(self, uses, skillEffects_Combat, ammoType) -> None:
        super.__init__(uses, skillEffects_Combat)
        self.ammoType = ammoType



#####   ----- Character Base Classes -----   #####

class combatAction:
    def __init__(self, type, diceMax, dicePower, diceNumber, effects) -> None:
        self.type = combatActionType(type)
        self.diceMax = int(diceMax)
        self.dicePower = int(dicePower)
        self.diceNumber = int(diceNumber)
        self.effects = [combatEffect(effects)]

class characterStats:
    def __init__(self, fortitude, wisdom, justice, charm, insight, temperance) -> None:
        self.fortitude = int(fortitude)
        self.wisdom = int(wisdom)
        self.justice = int(justice)
        self.charm = int(charm)
        self.insight = int(insight)
        self.temperance = int(temperance)

class characterBase:
    def __init__(self, name, hp, hp_Max, stagger, stagger_Max, sanity, sanity_Max, light, light_Max, stats, statuses) -> None:
        self.name = str(name)
        self.hp = int(hp)
        self.hp_Max = int(hp_Max)
        self.stg = int(stagger)
        self.stg_Max = int(stagger_Max)
        self.sp = int(sanity)
        self.sp_Max = int(sanity_Max)
        self.light = int(light)
        self.light_Max = int(light_Max)
        self.stats = characterStats(stats)
        self.statuses = [statusBase(statuses)]

# Status effect base

# statusEffect is an abstract class that should not be used directly
# This class adds a characterbase target to statuses, allowing child classes of this to effect a given character
class statusEffect(statusBase):
    def __init__(self, potentcy, count, isBeneficial, persistance ,target) -> None:
        super.__init__(self, potentcy, count, isBeneficial, persistance)
        self.target = characterBase(target)

