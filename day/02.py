f = open("test/02.txt", "r")
text = f.read()

def part1(text):
    games = text.split("\n")
    sum_ids = 0
    for game in games:
        colors = {
            'blue': 0,
            'red': 0,
            'green': 0
        }
        maximum = {
            'blue': 14,
            'green': 13,
            'red': 12
        }
        possible = True
        id, sets = game.split(": ")
        id = int(id.split("Game ")[1])
        sets = sets.split("; ")
        for set in sets:
            for item in set.split(", "):
                n, color = item.split(" ")
                n = int(n)
                colors[color] = n
                if colors[color] > maximum[color]:
                    possible = False
        # print(id, possible)
        if possible:
            sum_ids += id
    return sum_ids

def part2(text):
    games = text.split("\n")
    power_total = 0
    for game in games:
        colors = {
            'blue': 0,
            'red': 0,
            'green': 0
        }
        possible = True
        id, sets = game.split(": ")
        id = int(id.split("Game ")[1])
        sets = sets.split("; ")
        for set in sets:
            for item in set.split(", "):
                n, color = item.split(" ")
                n = int(n)
                colors[color] = max(colors[color], n)
        # print(colors)
        # print(id, possible)
        power = colors['red'] * colors['blue'] * colors['green']
        if possible:
            power_total += power
    return power_total


print(part1(text))
print(part2(text))
