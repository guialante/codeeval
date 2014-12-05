"""
    code eval challenge: https://www.codeeval.com/open_challenges/172/
    to execute: python card_number_validation.py card_number_validation.txt
"""
import sys
f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()

for line in lines:
    number = u''.join(line.strip('\n').split(' '))
    reversed_number = list(reversed(number))
    for count, i in enumerate(reversed_number):
        if count % 2 == 1:
            result = int(i) * 2
            if result > 9:
                result = sum(divmod(result, 10))
            reversed_number[count] = str(result)
    if sum(map(int, str(u''.join(reversed_number)))) % 10 == 0:
        print 1
    else:
        print 0
