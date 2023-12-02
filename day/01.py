f = open("test/01.txt", "r")
text = f.read()

words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

def part1(text):
    lines = text.split("\n")
    s = 0

    for line in lines:
        min_i, min_found = float('inf'), None
        max_i, max_found = float('-inf'), None
        for num in words.keys():
            num_min = line.find(str(num))
            num_max = line.rfind(str(num))
            if num_min != -1 and num_min < min_i:
                min_i = num_min
                min_found = num
            if num_max != -1 and num_max > max_i:
                max_i = num_max
                max_found = num
        s += int(f"{min_found}{max_found}")
        
    return s

def part2(text):
    lines = text.split("\n")
    s = 0

    for line in lines:
        min_i, min_found = float('inf'), None
        max_i, max_found = float('-inf'), None
        for num, word in words.items():
            num_min, word_min = line.find(str(num)), line.find(word)
            num_max, word_max = line.rfind(str(num)), line.rfind(word)
            if num_min != -1 and num_min < min_i:
                min_i = num_min
                min_found = num
            if word_min != -1 and word_min < min_i:
                min_i = word_min
                min_found = num
            if num_max != -1 and num_max > max_i:
                max_i = num_max
                max_found = num
            if word_max != -1 and word_max > max_i:
                max_i = word_max
                max_found = num
        s += int(f"{min_found}{max_found}")
        
    return s

print(part1(text))
print(part2(text))
