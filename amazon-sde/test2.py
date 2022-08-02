#!/bin/python3
import os

def countGroups(related):
    count_groups = {}
    for index in range(len(related)):
        print(related[index], related[index][index-1], index)
        if len(count_groups)==0:
            count_groups[index] = [related[index]]
        elif related[index][index-1] == "1":
            prev_el = related[index-1]
            for key in count_groups:
                if prev_el in count_groups[key]:
                    count_groups[key].append(related[index])
        else:
            count_groups[index] = [related[index]]
    return len(count_groups.keys())

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    related_count = int(input("Please put number of subscribers: ").strip())

    related = []

    for _ in range(related_count):
        related_item = input("Please put subscriber row: ")
        related.append(related_item)

    result = countGroups(related)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
