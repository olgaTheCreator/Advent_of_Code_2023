import re

f = open("./Day1/input.txt", "r")
lines = f.readlines()


'''part2'''
regex = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'
numberWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

nums = [[re.findall(regex, line)[0], re.findall(regex,line)[-1]] for line in lines ]
result = [int("".join([(str(numberWords.index(element)+ 1)) if element in numberWords else element for element in sublist])) for sublist in nums]
total = sum(result)
print(total)
