import re

f = open("./Day2/input.txt", "r")
lines = f.readlines()

#12 red cubes, 13 green cubes, and 14 blue cubes
maxes = {
    'red': 12,
    'green': 13,
    'blue': 14
}
regex = r'(\d+)\s(blue|green|red)'
games = [re.findall(regex, line) for line in lines]

possible =[all(int(x[0]) <= maxes[x[1]] for x in game) for game in games ]

result = sum([index+1 for index, x in enumerate(possible) if x is True])
print(result)
