#!/bin/python3

import math
import os
import random
import re
import sys

from pytz import country_timezones



#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#

def processLogs(logs, threshold):
    user_transactions_list = []
    count_dict = {}
    for log in logs:
        log_list = log.split(" ")
        if len(log_list) > 3:
            continue
        count_dict[log_list[0]] = 0
        count_dict[log_list[1]] = 0

    for log in logs:
        log_list = log.split(" ")
        count_dict[log_list[0]] = count_dict[log_list[0]] + 1
        count_dict[log_list[1]] = count_dict[log_list[1]] + 1

    for key in count_dict:
        if count_dict[key] < threshold:
            continue
        user_transactions_list.append(key)
    
    user_transactions_list.sort()
    return user_transactions_list

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(input("Logs count? ").strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input(f"Please put you log here {_+1}/{logs_count} ")
        logs.append(logs_item)

    threshold = int(input("Please put your threshold: ").strip())

    result = processLogs(logs, threshold)
    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()