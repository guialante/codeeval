"""
    code eval challenge: https://www.codeeval.com/open_challenges/2/
    to execute: python longest_lines.py longest_lines.txt
"""
import sys

path = sys.argv[1]

f = open(path)
file_lines = f.readlines()
lines_to_output = int(file_lines[0].rstrip())
file_lines = [x.rstrip() for x in file_lines]
sorted_list = sorted(file_lines, key=len, reverse=True)

for i in range(0, lines_to_output):
    print sorted_list[i]
