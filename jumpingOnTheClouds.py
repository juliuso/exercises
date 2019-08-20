#!/usr/bin/env python
# AUTHOR: jo
# DATE: 2019-08-20
# DESCRIPTION: "Jumping on the Clouds" problem from HackerRank
# PROBLEM: https://www.hackerrank.com/challenges/jumping-on-the-clouds/

# Complete the jumpingOnClouds function below.

def jumpingOnClouds(c):
    cloudLength = len(c)
    cost = 0
    index = 0

    while index < cloudLength:
        if (index == cloudLength-2):
            if c[index+1] == 0:
                cost += 1
                break
        elif (index == cloudLength-1):
            break
        if c[index+2] == 0:
            cost += 1
            index += 2
        elif c[index+1] == 0:
            cost += 1
            index += 1
        else:
            index += 1

    return cost

if __name__ == '__main__':

    # Some test cases
    c = [0,1,0,0,0,1,0] # least cost: 3
    d = [0,0,1,0,0,1,0] # least cost: 4
    e = [0,0,0,0,1,0] # least cost: 3
    f = [0,0,0,1,1,0] # least cost: 2

    print(jumpingOnClouds(c))
    print(jumpingOnClouds(d))
    print(jumpingOnClouds(e))
    print(jumpingOnClouds(f))
