#!/usr/bin/python3
"""
fuction that determine the fewest number of coins needed to meet a given amount 
"""

def makeChange(coins, total);
   """takes in list of coins and use that to calc how much total
      will require
    """
    if total <= 0;
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for x in coin:
            while(total >= x):
                counter += 1
                total -= x
        if total == 0:
            return counter
        return -1
