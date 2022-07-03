
class Wizard:

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} wizard is attacking')

class Ogre:

    def __init__(self, name, power):
        self.name = name
        self.axe_power = power

    def attack(self):
        print(f'{self.name} ogre is attacking by axe {self.axe_power}')

class Shaman(Wizard, Ogre):

    def __init__(self, name, power, axe):
        Wizard.__init__(self , name, power)
        Ogre.__init__(self,name, axe)

shaman1 = Shaman('Boo', 100, 50)
shaman1.attack()