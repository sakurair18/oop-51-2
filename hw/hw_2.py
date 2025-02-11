class Heroes:

    def __init__(self, name, hp):
        
        self.name_1 = name
        self.hp_1 = hp
        
    def action(self, ):
        print(f"{self.name_1} runs")
        
    def attack(self, ):
        print(f"{self.name_1} pulls a sword")
        
shieldhero = Heroes("Naofumi", 100)
shieldhero.action()

shieldhero = Heroes("Naofumi", 100)
shieldhero.attack()


class Archer(Heroes):
    
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision
    
    def rest(self ):
        self.arrows += 5
        print(f"У вас сейчас {self.arrows} стрел")
        
    def status(self ):
        print(f"Имя: {self.name_1}, здоровье: {self.hp_1}, количество стрел: {self.arrows}, точность: {self.precision}")
    
    def attack(self ):
        self.arrows -= 1
        if self.arrows <= 0:
            print("У вас закончились стрелы")
        
        if self.precision > 1:
            print("Удачная атака")
        else:
            print("Неудачная атака")
            
gamehero = Archer("Fishl", 80, 0, 0)
gamehero.rest()
gamehero.status()
gamehero.attack()
    