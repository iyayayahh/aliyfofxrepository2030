#The RPG Hero Game

class Hero:
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp
    def take_damage(self, amount):
        self.hp -= amount

arthur = Hero ("Arthur", 100)
morgana = Hero ("Morgana", 100)

arthur.take_damage(10)
print (f"{arthur.name}'s took 10 damage after Morgana used her Phoenix Strike!")

print (f"{arthur.name}'s HP: {arthur.hp}")
print (f"{morgana.name}'s HP: {morgana.hp}")

