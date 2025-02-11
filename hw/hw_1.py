class Hero:

    def __init__(self, name, hp, lvl):
        
        self.name_1 = name
        self.hp_1 = hp
        self.lvl_1 = lvl
        
        
    def introduce(self, ):
        print(f"Меня зовут {self.name_1}, мой lvl {self.lvl_1} , мое HP {self.hp_1}")
        
    def isadult(self, ):
        if self.lvl_1 >= 10:
            return True
        else:
            return False
            
superman = Hero("Captain America", 100, 50)
superman.introduce()

shieldhero = Hero("Naofumi", 70, 100)
print(shieldhero.isadult())

animehero = Hero("Goku", 1000, 8)
print(animehero.isadult())

sailorhero = Hero("Sailor Moon", 9999, 11)
print(sailorhero.isadult())