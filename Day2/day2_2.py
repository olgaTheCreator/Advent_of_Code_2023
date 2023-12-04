import re
import math

f = open("./Day2/input.txt", "r")
lines = f.readlines()

#12 red cubes, 13 green cubes, and 14 blue cubes
mins = {
    'red': 0,
    'green': 0,
    'blue': 0
}
regex = r'(\d+)\s(blue|green|red)'
games = [re.findall(regex, line) for line in lines]
print(games)

powers = []
for game in games:
    for element in game:
        if mins[element[1]] < int(element[0]):
            mins[element[1]] = int(element[0])
    powers.append(math.prod(list(mins.values())))
    mins = {
    'red': 0,
    'green': 0,
    'blue': 0
}
result=sum(powers)
print(result)

# possible =[all(int(x[0]) <= maxes[x[1]] for x in game) for game in games ]

# result = sum([index+1 for index, x in enumerate(possible) if x is True])
# print(result)
