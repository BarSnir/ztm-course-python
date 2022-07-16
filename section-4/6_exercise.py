from functools import reduce
import re

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize_pets(item):
    return item.upper()

print(list(map(capitalize_pets, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()
print(list(zip(my_strings, my_numbers)))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def filter_score(score):
    return score > 50

print(list(filter(filter_score, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item

my_numbers_total = reduce(accumulator, my_numbers)
scores_total = reduce(accumulator, scores)
print(f'The total is {my_numbers_total+scores_total}')