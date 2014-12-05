"""
    code eval challenge: https://www.codeeval.com/open_challenges/14/
    to execute python string_permutations.py string_permutations.txt
"""
import sys
from itertools import permutations

f = open(sys.argv[1], 'r')
lines = f.readlines()
for line in lines:
    perms = map(''.join, permutations(line.strip('\n')))
    perms.sort()
    print u','.join(perms)
f.close()
