digits = {"one" : "1", "two" : "2", "three" : "3", "four" : "4",
          "five" : "5", "six" : "6", "seven" : "7", "eight": "8", "nine": "9"}

def find_first_last_concat(line):
    val_ind_pairs = []
    for d in digits.keys():
        ind = line.find(d)
        if ind != -1:
            val_ind_pairs.append((digits[d], ind))
        ind = line.rfind(d)
        if ind != -1:
            val_ind_pairs.append((digits[d], ind))

    for i in range(len(line)):
        if line[i].isdigit():
            val_ind_pairs.append((line[i], i))

    val_ind_pairs.sort(key = lambda x: x[1])
    return int(val_ind_pairs[0][0] + val_ind_pairs[-1][0])


with open("data/1.txt") as f:
    lines = f.readlines()
    s = 0
    for line in lines:
        line = line.strip()

        s += find_first_last_concat(line)
    print(s)

"""
Part 1:
with open("data/1.txt") as f:
    lines = f.readlines()
    s = 0
    for line in lines:
        line = line.strip()
        parsed = [c for c in line if c.isdigit()]
        s += int(parsed[0] + parsed[-1])
    print(s)
"""