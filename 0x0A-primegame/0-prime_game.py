#!/usr/bin/python3
"""
Prime Game
"""

def primeNumbers(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    numPrime = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            numPrime.append(prime)
            for j in range(prime, n + 1, prime):
                filtered[j] = False
        return numPrime

def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x ==0 or num == []:
        return None
    Maria = Ben = 0
    for j in range(x):
        numPrime = primeNumbers(nums[j])
        if len(numPrime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
        if Maria > Ben:
            return 'Maria'
        elif Ben > Maria:
            return 'Ben'
        return None



