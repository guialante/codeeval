"""
    code eval challenge: https://www.codeeval.com/open_challenges/46/
    to execute: python prime_numbers.py prime_numbers.txt
"""
import sys
f = open(sys.argv[1], 'r')

lines = f.readlines()

def sieve(n):
    s = xrange(3, n + 1, 2)
    r = set(s)
    [r.difference_update(xrange(n << 1, s[-1] + 1, n)) for n in s if n in r]
    primes = list(r.union([2]))
    primes.sort()
    print ','.join(map(str, primes))

for line in lines:
    n = int(line)
    sieve(n)
f.close()
