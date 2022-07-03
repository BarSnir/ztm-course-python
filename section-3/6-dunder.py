
class Toy:

    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": "Bar",
            "position": "Data Engineer"
        }

    def __call__(self):
        return "Hey"

    def __getitem__(self, item):
        return self.my_dict.get(item)


action_figure1 = Toy('red', 0)
print(action_figure1.__str__())
print(action_figure1.__dict__)
print(action_figure1.__hash__())
print(action_figure1())
print(action_figure1['name'])