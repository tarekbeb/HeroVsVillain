#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character(object):
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"You did {self.power} damage to the {enemy}.")
        if enemy.health <= 0:
            print(f"The {enemy} is dead.")
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power ))
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def __str__(self):
        return "hero"
class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def __str__(self):
        return "goblin"

hero = Hero(10,5)
goblin = Goblin(6, 2)

while goblin.alive() and hero.alive():
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
    # Hero attacks goblin
        hero.attack(goblin)
    elif raw_input == "2":
        goblin.attack(hero)
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))