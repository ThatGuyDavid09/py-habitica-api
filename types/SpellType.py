from enum import Enum

class SpellType(Enum):
    # Mage
    FIREBALL = "fireball"
    MPHEAL = "mpheal"
    EARTH = "earth"
    FROST = "frost"

    # Warrior
    SMASH = "Brutal Smash"
    DEFENSIVE_STANCE = "Defensive Stance"
    VALOROUS_PRESENCE = "valorousPresence"
    INTIMIDATE = "intimidate"

    # Rogue
    PICK_POCKET = "pickPocket"
    BACK_STAB = "backStab"
    TOOLS_OF_TRADE = "toolsOfTrade"
    STEALTH = "stealth"

    # Healer
    HEAL = "heal"
    PROTECT_AURA = "protectAura"
    BRIGHTNESS = "brightness"
    HEAL_ALL = "healAll"

    # Transformation items
    SNOWBALL = "snowball"
    SPOOKY_SPARKLES = "spookySparkles"
    SEAFOAM = "seafoam"
    SHINY_SEED = "shinySeed"
