def battle(poke, mon):
     while poke.hp>0 and mon.hp > 0:
        if poke.hp>0:
            mon.hp = mon.hp - poke.power
        if mon.hp>0:
            poke.hp = poke.hp-mon.power
        print poke.hp, mon.hp

class monster():
    def __init__(self, element):
        self.element = element
        self.hp = 1000
        self.power = 100
        self.elements = []
    def attack():
        return (power, element)
    def addElement(self, element):
        self.elements.append(element)
        
class element():
    #"Strong" means 2x, "Weak" means 0.5x, "Immune" is 0x
    # any other elements are 1x
    def __init__(self,
                 attack = {"Strong":(), "Weak":(), "Immune":()},
                 defense = {"Strong":(), "Weak":(), "Immune":()}
                 ):
        self.attack = attack
        self.defense = defense

Fire = element(attack = {"Strong":("bug","grass","ice","steel"),"Weak":("dragon","fire","water","rock","water"),"Immune":()},
               defense = {"Strong":("ground","rock","water"),"Weak":("fairy","bug","fire","grass","ice","steel"),"Immune":()}
               )
Water = element(attack = {"Strong":("fire","ground","rock"),"Weak":("dragon","grass","water"),"Immune":()},
                defense = {"Strong":("electr","grass"),"Weak":("fire","ice","steel","water"),"Immune":()}
                )
elements = (Fire,Water)                         


if __name__ == "__main__":
       battle(monster(Fire),monster(Water))       
