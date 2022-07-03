
#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def print_oldest_cat(cats_list):
        oldest_age = 0
        for cat in cats_list:
            if cat.age > oldest_age:
                oldest_age = cat.age
                oldest_cat = cat
        print(f'The oldest cat is {oldest_cat.name} in age {oldest_cat.age}')
        
cat1 = Cat('Tom', 10)
cat2 = Cat('Edward', 5)
cat3 = Cat('John', 2)
cats_list = [cat1, cat2, cat3]
Cat.print_oldest_cat(cats_list)