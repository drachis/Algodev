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


'''

    Text-based adventure [Key topics: basic i/o, basic code structure]
    Conway's Game of Life [Key topics: cellular automata, arrays, mouse input, simple rendering]
    Tetris [Key topics: basic collisions, keyboard input, slightly less simple rendering]
    Snake [Key topics: linked lists]
    Asteroids [Key topics: trigonometry, slightly less basic collisions]
    Minesweeper [Key topics: flood fill]
    Sudoku [Key topics: basic procedural generation]
    Tile-based editor [Key topics: file access, gui creation]
    Perlin noise algorithm [Key topics: advanced procedural generation]
    A* algorithm [Key topics: pathfinding]
    Galcon [Key topics: basic AI]
    Brainfuck interpreter [Key topics: basic parsing]
    Hash table [Key topics: atypical applications of linked lists, data structures]
    Splayed binary search tree [Key topics: advanced data structures]
    XML parser [Key topics: slightly more advanced parsing, practical applications of complex data structures]
    Falling sand game [Key topics: practical applications of parsing, basic particle physics simulation, complex application of gui]
    Platformer game [Key topics: basic rigid body physics]
    Chess versus a computer opponent [Key topics: advanced AI]
    GIF saving & loading algorithm [Key topics: advanced file access, compression and decompression, bitwise arithmetic]
    Simple Lua/Python-driven game engine [Key topics: virtual machines, basic engine creation]
    Raycasting renderer [Key topics: pseudo-3D rendering]
    FPS [Key topics: 3D rendering, Basic 3D collisions]

'''
