#!/usr/bin/env python
# AUTHOR: jo
# DATE: 2019-08-19
# DESCRIPTION: "Counting Valleys" problem from HackerRank
# PROBLEM: https://www.hackerrank.com/challenges/counting-valleys/

# Complete the sockMerchant function below.
def countingValleys(n, s):
    valleys = 0
    level = 0

    for i in range(n):
        if (s[i] == 'U'):
            level += 1
        if (s[i] == 'D'):
            level -= 1

        if level == 0 and s[i] == 'U':
            valleys += 1

    return valleys

if __name__ == '__main__':
    # Test cases
    # Test UDDDUDUU -> 1
    # Test DDUUDDUDUUUD -> 2

    testCase1 = 'UDDDUDUU'
    testCase2 = 'DDUUDDUDUUUD'

    print(countingValleys(len(testCase1), testCase1))
    print(countingValleys(len(testCase2), testCase2))
