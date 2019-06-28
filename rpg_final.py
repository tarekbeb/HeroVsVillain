import random
import time
class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            exit
        print (f"{self.name} attacks {enemy.name}")
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print (f"{self.name} received {points} damage.")
        if self.name == 'Zombie' and self.health <= -10:
            print (f"{self.name} is dead.")
        elif self.name != 'Zombie' and self.health <= 0:
            print (f"{self.name} is dead.")

    def print_status(self):
        print (f"{self.name} has {self.health} health and {self.power} power.")

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armour = 0
        self.evade = 0

    def receive_damage(self, points):
        evade_points_1 = random.random() > 0.9
        evade_points_2 = random.random() > 0.85
        if self.evade == 2 and evade_points_1 == True:
            print ("evade used")
        elif self.evade >= 4 and evade_points_2 == True:
            print ("evade used")
        else:
            self.health -= points
            self.health += self.armour
            print (f"{self.name} received {points} damage.")

        if self.name == 'Zombie' and self.health <= -10:
            print (f"{self.name} is dead.")
        elif self.name != 'Zombie' and self.health <= 0:
            print (f"{self.name} is dead.")

    def attack(self, enemy):
        if not self.alive():
            return
        print (f"{self.name} attacks {enemy.name}")
        double_power = random.random() > 0.8
        if double_power == True:
            enemy.receive_damage(self.power * 2)
        else:
            enemy.receive_damage(self.power)
        time.sleep(1.5)

    def restore(self):
        self.health = 10
        print (f"Hero's heath is restored to {self.health}!")
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.coins = 5

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.coins = 7

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print (f"{self.name} swaps power with {enemy.name} during attack")
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        self.name = 'Medic'
        self.health = 10
        self.power = 3
        self.coins = 8

    def receive_damage(self, points):
        self.health -= points
        recuperate = random.random() > 0.8
        if recuperate == True:
            self.health += 2
        print (f"{self.name} received {points} damage.")
        if self.health <= 0:
            print (f"{self.name} is dead.")

class Shadow(Character):
    def __init__(self):
        self.name = 'Shadow'
        self.health = 1
        self.power = 3
        self.coins = 10

    def receive_damage(self, points):
        shadow_damage = random.random() > 0.9
        if shadow_damage == True:
            self.health -= points
            print (f"{self.name} received {points} damage.")
        else:
            print (f"{self.name} received no damage.")
        if self.health <= 0:
            print (f"{self.name} is dead.")

class Zombie(Character):
    def __init__(self):
        self.name = 'Zombie'
        self.health = 5
        self.power = 3
        self.coins = 11

    def alive(self):
        return True

class Dragon(Character):
    def __init__(self):
        self.name = 'Dragon'
        self.health = 10
        self.power = 3
        self.coins = 12

    def attack(self, enemy):
        if not self.alive():
            return False
        print (f"{self.name} attacks {enemy.name}")
        dragon_damage = random.random() > 0.5
        if dragon_damage == True:
            enemy.receive_damage(self.power * 10)
        else:
            enemy.receive_damage(self.power)
        time.sleep(1.5)

class Battle(object):
    def do_battle(self, hero, enemy):
        print ("=====================")
        print (f"Hero faces the {enemy.name}")
        print ("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print ("-----------------------")
            print ("What do you want to do?")
            print (f"1. fight {enemy.name}")
            print ("2. do nothing")
            print ("3. flee")
            print ("> ")
            raw_input = int(input())
            if raw_input == 1:
                hero.attack(enemy)
            elif raw_input == 2:
                pass
            elif raw_input == 3:
                print ("Goodbye.")
                break
            else:
                print (f"Invalid input {input}")
                continue
            enemy.attack(hero)
            if not enemy.alive():
                return True
        if hero.alive():
            print (f"You defeated the {enemy.name}")
            hero.coins += enemy.coins
            print (f"Hero has {hero.coins} coins")
            return True
        # elif not enemy.alive():
        #     return False

class Evade(object):
    cost = 5
    name = 'Evade'
    def apply(self, character):
        character.evade += 2
        print (f"{character.name}'s evade amount increased to {character.evade}.")


class Armour(object):
    cost = 10
    name = "Armour"
    def apply(self, character):
        character.armour += 2
        print (f"{character.name}'s armour increased to {character.armour}.")

class SuperTonic(object):
    cost = 10
    name = 'SuperTonic'
    def apply(self, character):
        character.health += 10
        print (f"{character.name}'s health increased to {character.health}.")

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print (f"{character.name}'s health increased to {character.health}.")

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, character):
        character.power += 2
        print (f"{character.name}'s power increased to {character.power}.")

class Shopping(object):
    items = [Tonic, Sword, SuperTonic, Armour, Evade]
    def do_shopping(self, hero):
        itemsRange = range(len(Shopping.items))
        while True:
            print ("=====================")
            print ("Welcome to the store!")
            print ("=====================")
            print (f"You have {hero.coins} coins.")
            print ("What do you want to do?")
            for i in itemsRange:
                item = Shopping.items[i]
                print (f"{i+1}. buy {item.name} ({item.cost})")
            print ("10. leave")
            raw_input = int(input("> "))
            if raw_input == 10:
                break
            else:
                ItemToBuy = Shopping.items[raw_input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Dragon(), Zombie(), Goblin(), Wizard(), Medic(), Shadow()]
battle_engine = Battle()
shopping_engine = Shopping()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print ("YOU LOSE!")
        break
    shopping_engine.do_shopping(hero)