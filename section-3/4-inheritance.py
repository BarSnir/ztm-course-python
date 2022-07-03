
class User:

    def print_something(self):
        print('print something')

    def attack(self):
        print(f'Character {self.character} attack with power of {self.power}')


class Archer(User):
    character = 'Archer'
    power = 50

class Ogre(User):
    character = 'Ogre'
    power = 1500

archer1 = Archer()
ogre1 = Ogre()
archer1.attack()
ogre1.attack()
print(isinstance(archer1, object))
print(archer1.__getattribute__('character'))