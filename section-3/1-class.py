
class PlayerCharacter:

    my_attribute = 'some_text'

    def __init__(self, name):
        self.name = name # Attributes

    def run(self):
        print('run')

player1 = PlayerCharacter('Bar')
player2 = PlayerCharacter('Andrew')
print(player1.name)
print(player2.name)
player1.run()
player2.run()
help(player1)