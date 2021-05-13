class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def __str__(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))
    def alive(self):
        if self.health >= 0:
            return True
    def attack(self, enemy):
        enemy.health -= self.power
    def print_status(self):
        print("%s has %d health and %d power." % (self, gawain.health, gawain.power))

class Hero(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

class Goblin(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
class Zombie(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

gawain = Hero("Gawain", 10, 5)
green_knight = Goblin("Green Knight", 6, 2)
zombie = Zombie("Zombie", 25, 2)

def main():

    while green_knight.health > 0 and gawain.health > 0:
        gawain.__str__()
        green_knight.__str__()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            gawain.attack(green_knight)
            print("You do %d damage to the goblin." % gawain.power)
            if green_knight.health == False:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if green_knight.health > 0:
            # Goblin attacks hero
            green_knight.attack(gawain)
            print("The goblin does %d damage to you." % green_knight.power)
            if gawain.health == False:
                print("You are dead.")
main()