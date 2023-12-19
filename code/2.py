cubes = {"red": 0, "green": 0, "blue": 0}


def set_possible():
    return cubes["red"] <= 12 and cubes["green"] <= 13 and cubes["blue"] <= 14

with open("data/2.txt") as f:
    lines = f.readlines()
    cur_game = 1
    id_sum = 0
    for line in lines:
        line = line.strip().split(": ")[1]
        game = line.split(";")
        possible = True
        for bag_set in game:
            colors = bag_set.split(", ")
            for color in colors:
                color = color.lstrip()
                nums = color.split(" ")
                cubes[nums[1]] += int(nums[0])
            if not set_possible():
                possible = False

            for c in cubes.keys():
                cubes[c] = 0

        if possible:
            id_sum += cur_game

        cur_game += 1
    print(id_sum)