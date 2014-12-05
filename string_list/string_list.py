"""
    code eval challenge: https://www.codeeval.com/open_challenges/38/
    to execute: python string_list.py string_list.txt
"""
import sys
from itertools import product


f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()

for line in lines:
    tmp_list = line.strip('\n').split(',')
    result = list(product(tmp_list[1], repeat=int(tmp_list[0])))
    new_result = map(''.join, result)
    new_result = list(set(new_result))
    new_result.sort()
    print ','.join(new_result)
