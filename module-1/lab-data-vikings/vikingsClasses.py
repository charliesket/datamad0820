import random
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength 
    def receiveDamage(self,damage):
        self.health= self.health - damage

    
    

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name = name
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health= self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"
    

# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health= self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        if self.health <= 0:
            return "A Saxon has died in combat"


# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(Saxon):
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        died = saxon.receiveDamage(saxon.strength)
        if saxon.health <= 0:
            idx_saxon = self.saxonArmy.index(Saxon)
            self.saxonArmy.pop(idx_saxon)
            return died

    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        died = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            idx_viking = self.vikingArmy.index(Viking)
            self.saxonArmy.pop(idx_viking)
            return died

    def showStatus(self):
        sax= len(self.saxonArmy)
        vik= len(self.vikingArmy)
        if not sax:
            return "Vikings have won the war of the century!"
        if not vik:
            return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of the battle"

    
