import re

f = open("./Day1/input.txt", "r")
lines = f.readlines()
print(lines)

'''part1'''
numbers = [int("".join([re.search(r'\d',line).group(), re.search(r'\d',line[::-1]).group()])) for line in lines]
total = sum(numbers)
print(total)

