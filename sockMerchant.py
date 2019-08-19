#!/usr/bin/env python
# AUTHOR: jo
# DATE: 2019-08-15
# DESCRIPTION: "Sock Merchant" problem from HackerRank
# PROBLEM: https://www.hackerrank.com/challenges/sock-merchant

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counter = 0
    my_dict = {}
    for val in ar:
        if val not in my_dict:
            my_dict[val] = 1
        else:
            my_dict[val] += 1
    
    for v in my_dict.values():
        if math.floor(v/2) >= 1:
            counter += math.floor(v/2)

    return counter

if __name__ == '__main__':
    # Test cases
    print(sockMerchant(9, [10,20,20,10,10,30,50,10,20]))
    print(sockMerchant(10, [1,1,3,1,2,1,3,3,3,3]))

