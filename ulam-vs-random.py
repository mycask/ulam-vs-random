#!/usr/bin/env python3
import random

"""Seives Algo to find prime numbers within n . More Time Efficient. """
def get_primes(n):

    primes = []
    
    if(n<2):
        return primes;


    prime = [True for i in range(n+1)]
 
    i = 2
    while (i * i <= n):
		
        if (prime[i] == True):
			
            for j in range(i * 2, n+1, i):
            	prime[j] = False
        i += 1
	
    for i in range(2, n):
        if prime[i]:
            primes.append(i)
    
    return primes


def get_random_odds(n, k):
    """Get k random odd numbers less than or equal to n."""
    return sorted(random.sample(range(1, n+1, 2), k))


def get_spiral(n):
    """Return an n x n by spiral of 1, 2, ..., n*n."""
    assert n % 2 == 1
    a = [[0 for i in range(n)] for j in range(n)]
    i = j = n // 2
    d = 0
    a[i][j] = 1
    for x in range(2, n**2+1):
        if d == 0:
            j += 1
            if a[i-1][j] == 0:
                d = 1
        elif d == 1:
            i -= 1
            if a[i][j-1] == 0:
                d = 2
        elif d == 2:
            j -= 1
            if a[i+1][j] == 0:
                d = 3
        else:
            i += 1
            if a[i][j+1] == 0:
                d = 0
        a[i][j] = x
    return a


def print_grid(a):
    """Print a spiral grid for debugging purpose."""
    print('\n'.join(''.join('{:5d}'.format(y) for y in x) for x in a))


def plot(n):
    """Plot Ulam (prime) spiral followed by a random odd spiral."""
    spiral = get_spiral(n)
    primes = get_primes(n * n)
    rands = get_random_odds(n * n, len(primes))

    print('len(primes):', len(primes))
    print('len(rands):', len(rands))

    print('ULAM SPIRAL')
    print('-----------')
    print('\n'.join(''.join('*' if y in primes else ' ' for y in x)
                    for x in spiral))
    print()

    print('RANDOM SPIRAL')
    print('-------------')
    print('\n'.join(''.join('*' if y in rands else ' ' for y in x)
                    for x in spiral))
    print()


if __name__ == '__main__':
    # Constant seed to get the same random output on every run.
    random.seed(0)

    # Plot the spirals as text.
    plot(99)
