# Project 2 – Character Abilities Showcase

## Overview

This project implements a simple role-playing game (RPG) battle system to demonstrate **classes**, **inheritance**, **method overriding**, and **composition** in Python, using only concepts covered through the **Inheritance** chapter.

The core design centers around a 3-level inheritance chain:

- `Character` → base class for all characters
- `Hero` → intermediate class that adds level and energy
- `Warrior`, `Mage`, `Rogue` → specialized hero subclasses

Each hero also holds a `Weapon` object, which is an example of **composition** (“has-a” relationship).

---

## Class Design

### Weapon (Composition)

- **Attributes**: `name`, `base_damage`, `weapon_type`
- **Methods**:
  - `get_damage()`: Returns base damage.
  - `get_description()`: Text description of the weapon.

### Character (Base Class – Level 1)

- **Attributes**:
  - `name`
  - `max_health`
  - `current_health`
  - `weapon` (a `Weapon` instance)
- **Methods**:
  - `is_alive()`
  - `take_damage(amount)`
  - `heal(amount)`
  - `attack(target)` – basic attack using weapon damage
  - `use_special(target)` – placeholder (no special ability)
  - `get_description()` – description string

### Hero (Intermediate Class – Level 2)

Inherits from `Character`.

- **Additional Attributes**:
  - `level`
  - `energy`
- **Overridden Methods**:
  - `attack(target)` – hero attack includes level-based bonus damage
  - `get_description()` – includes level and energy

### Warrior / Mage / Rogue (Specialized Classes – Level 3)

Each of these subclasses inherits from `Hero` and overrides behavior.

#### Warrior

- Extra attribute: `rage`
- **Overrides**:
  - `attack(target)`: Uses weapon damage + level + rage-based bonus, increases rage.
  - `use_special(target)`: “Raging Slam” – consumes rage to deal heavy damage.

#### Mage

- Extra attribute: `mana`
- **Overrides**:
  - `attack(target)`: Weaker basic attack but regenerates mana.
  - `use_special(target)`: “Fireball” – spends mana to deal big magic damage.

#### Rogue

- Extra attribute: `focus`
- **Overrides**:
  - `attack(target)`: Damage increases with accumulated focus.
  - `use_special(target)`: “Backstab” – consumes focus for burst damage.

---

## Bonus Creative Features

I included the following creative elements beyond the minimum requirements:

1. **Three distinct hero subclasses** (`Warrior`, `Mage`, `Rogue`) with:
   - Different resource systems (`rage`, `mana`, `focus`).
   - Different special ability mechanics.
2. **Weapon system** with:
   - `Weapon` class for composition.
   - Different base damages and weapon types.
3. **Demo battle simulation** via:
   - `build_default_party()` to construct a standard party.
   - `run_demo_battle()` to simulate a fight against a training dummy and showcase polymorphism.

---

## AI Usage

I used AI assistance (ChatGPT) to help:

- Design the inheritance structure (`Character` → `Hero` → subclasses).
- Draft the initial versions of the methods for attacking and special abilities.
- Create this `README.md` template and high-level documentation.


---

## How to Run

1. **Clone your GitHub repo** (from the assignment link):

   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
