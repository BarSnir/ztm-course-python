#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMaxProducts' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY products as parameter.
#

def findMaxProducts(products, products_count):
    products_counter = 0
    for bucket in products:
        if int(bucket) >= int(products_count):
            products_counter = products_counter + int(bucket)
            print(products_counter)
    return products_counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    products_count = int(input("Please put number of products per bucket: ").strip())

    products = []

    for _ in range(products_count):
        products_item = int(input("Number of products in the index bucket: ").strip())
        products.append(products_item)

    result = findMaxProducts(products, products_count)

    fptr.write(str(result) + '\n')

    fptr.close()
