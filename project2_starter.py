"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Jadyn DeWitt-Smith
Date: 11/14/2025

AI Usage: This file's class design and method implementations were created with help
from ChatGPT (for structure, naming, and example logic). I have reviewed
and understand each class, method, and line of code.
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

# ---------------------------
# Composition: Weapon class
# ---------------------------

class Weapon:
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        print("Weapon: " + self.name + " | Damage Bonus: " + str(self.damage_bonus))


# ---------------------------------
# Base class: Character (Level 1)
# ---------------------------------

class Character:
    """
    Base character class.
    All characters share: name, health, strength, magic, weapon, and core actions.
    """

    def __init__(self, name, health, strength, magic, weapon=None):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic

        # Composition: a Character "has a" Weapon
        if weapon is None:
            # default weapon with no bonus
            self.weapon = Weapon("Fists", 0)
        else:
            self.weapon = weapon

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        if damage < 0:
            damage = 0
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
        print(self.name + " takes " + str(damage) +
              " damage. Health now: " + str(self.health))

    def attack(self, target):
        """
        Basic physical attack using strength + weapon bonus.
        Subclasses override this for custom behaviors (polymorphism).
        """
        if not self.is_alive():
            print(self.name + " cannot attack (defeated).")
            return
        if not target.is_alive():
            print(target.name + " is already defeated.")
            return

        base_damage = self.strength + self.weapon.damage_bonus
        print(self.name + " attacks " + target.name +
              " for " + str(base_damage) + " damage.")
        target.take_damage(base_damage)

    def display_stats(self):
        print("Name: " + self.name)
        print("Health: " + str(self.health))
        print("Strength: " + str(self.strength))
        print("Magic: " + str(self.magic))
        print("Weapon: " + self.weapon.name +
              " (+" + str(self.weapon.damage_bonus) + " dmg)")


# ----------------------------------------
# Player class: inherits Character (Level 2)
# ----------------------------------------

class Player(Character):
    """
    Player is a Character with extra RPG stats:
    - character_class (e.g., "Warrior")
    - level
    - experience
    """

    def __init__(self, name, character_class, health, strength, magic, weapon=None):
        Character.__init__(self, name, health, strength, magic, weapon)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

    def gain_experience(self, amount):
        if amount < 0:
            amount = 0
        self.experience = self.experience + amount

    def display_stats(self):
        """
        Enhanced display_stats that shows player-specific info.
        Overrides Character.display_stats.
        """
        print("=== Player Stats ===")
        print("Name: " + self.name)
        print("Class: " + self.character_class)
        print("Level: " + str(self.level))
        print("Experience: " + str(self.experience))
        print("Health: " + str(self.health))
        print("Strength: " + str(self.strength))
        print("Magic: " + str(self.magic))
        print("Weapon: " + self.weapon.name +
              " (+" + str(self.weapon.damage_bonus) + " dmg)")
        print("====================")


# -----------------------------------------------------
# Warrior / Mage / Rogue: inherit from Player (Level 3)
# -----------------------------------------------------

class Warrior(Player):
    """
    Warrior: high health, high strength, low magic.
    Required stats:
      Health = 120, Strength = 15, Magic = 5
    Special ability: power_strike(target)
    """

    def __init__(self, name, weapon=None):
        Player.__init__(self, name, "Warrior", 120, 15, 5, weapon)

    def attack(self, target):
        """
        Override Player/Character attack:
        Warriors hit harder with physical attacks.
        """
        if not self.is_alive():
            print(self.name + " cannot attack (defeated).")
            return
        if not target.is_alive():
            print(target.name + " is already defeated.")
            return

        # Strong physical attack: strength + weapon + small flat bonus
        damage = self.strength + self.weapon.damage_bonus + 3
        print(self.name + " (Warrior) slashes " + target.name +
              " for " + str(damage) + " damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        """
        Special Ability: Power Strike
        High damage single attack using strength and a multiplier.
        """
        if not self.is_alive():
            print(self.name + " cannot use Power Strike (defeated).")
            return
        if not target.is_alive():
            print(target.name + " is already defeated.")
            return

        damage = (self.strength * 2) + self.weapon.damage_bonus
        print(self.name + " uses POWER STRIKE on " + target.name +
              " for " + str(damage) + " damage!")
        target.take_damage(damage)


class Mage(Player):
    """
    Mage: low health, moderate strength, high magic.
    Required stats:
      Health = 80, Strength = 8, Magic = 20
    Special ability: fireball(target)
    """

    def __init__(self, name, weapon=None):
        Player.__init__(self, name, "Mage", 80, 8, 20, weapon)

    def attack(self, target):
        """
        Override attack:
        Basic attack uses a mix of magic and weapon bonus, but weaker
        than full Fireball.
        """
        if not self.is_alive():
            print(self.name + " cannot attack (defeated).")
            return
        if not target.is_alive():
            print(target.name + " is already defeated.")
            return

        # Light magical attack
        damage = (self.magic // 2) + self.weapon.damage_bonus
        print(self.name + " (Mage) casts a small spell at " + target.name +
              " for " + str(damage) + " damage.")
        target.take_damage(damage)

    def fireball(self, target):
        """
        Special Ability: Fireball
        Heavy magic damage attack.
        """
        if not self.is_alive():
            print(self.name + " cannot cast Fireball (defeated).")
            return
        if not target.is_alive():
            print(target.name + " is already defeated.")
            return

        damage = self.magic + self.weapon.damage_bonus + 5
        print(self.name + " hurls a FIREBALL at " + target.name +
              " for " + str(damage) + " magic damage!")
        target.take_damage(damage)


class Rogue(Player):
    """
    Rogue: balanced health, good strength, moderate magic.
    Required stats:
      Health = 90, Strength = 12, Magic = 10
    Special ability: sneak_attack(target)
    """

    def __init__(self, name, weapon=None):
        Player.__init__(self, name, "Rogue", 90, 12, 10, weapon)

    def attack(self, target):
        """
        Override attack:
        Rogues rely on quick strikes; chance-like flavor using
        a small bonus to represent agility.
        """
        if not self.is_alive():
            print(self.name + " cannot attack (defeated).")
            return
        if not target.is_alive():
            print(target.name + " is already defeated.")
            return

        damage = self.strength + self.weapon.damage_bonus + 1
        print(self.name + " (Rogue) swiftly cuts " + target.name +
              " for " + str(damage) + " damage.")
        target.take_damage(damage)

    def sneak_attack(self, target):
        """
        Special Ability: Sneak Attack
        Critical-style hit that deals extra damage.
        """
        if not self.is_alive():
            print(self.name + " cannot use Sneak Attack (defeated).")
            return
        if not target.is_alive():
            print(target.name + " is already defeated.")
            return

        damage = (self.strength + self.weapon.damage_bonus) * 2
        print(self.name + " performs a SNEAK ATTACK on " + target.name +
              " for " + str(damage) + " critical damage!")
        target.take_damage(damage)



# Example manual test (safe to keep or tweak)
if __name__ == "__main__":
    # Create some weapons
    sword = Weapon("Iron Sword", 5)
    staff = Weapon("Oak Staff", 3)
    daggers = Weapon("Twin Daggers", 4)

    # Create characters (inheritance in action)
    warrior = Warrior("Marcus", sword)
    mage = Mage("Aria", staff)
    rogue = Rogue("Shadow", daggers)

    # Display stats (method overriding in action)
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    # Simple manual combat test (not SimpleBattle)
    print("\n--- Manual Test: Polymorphic attacks ---")
    dummy = Character("Training Dummy", 200, 5, 0)

    for c in [warrior, mage, rogue]:
        c.attack(dummy)

    print("\n--- Manual Test: Special abilities ---")
    warrior.power_strike(dummy)
    mage.fireball(dummy)
    rogue.sneak_attack(dummy)

    print("\nDummy health after tests: " + str(dummy.health))
