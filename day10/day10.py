import fileinput
import sys

matrix = []

characters: dict[str, list[list[int]]] = {
    "|": [[-1, 1], [0, 0]],
    "-": [[0, 0], [-1, 1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [-1, 0]],
    "7": [[0, 1], [-1, 0]],
    "F": [[0, 1], [0, 1]],
    ".": [[0, 0], [0, 0]]
}

seen_befores = {}

def add_seen(x, y, distance):
    if x not in seen_befores:
        seen_befores[x] = {}
    seen_befores[x][y] = distance

def crawl(start_line, start_char, line, char, distance_away):
    current = matrix[line][char]
    ranges = characters[current]

    for i in range(ranges[0][0], ranges[0][1] + 1):
        for j in range(ranges[1][0], ranges[1][1] + 1):
            if i == 1 and j == -1 or i == -1 and j == 1:
                continue
            if abs(i+j) > 1:
                continue
            next_char = find_next_char(line, char, [i, j])
            if next_char == "." or next_char == "S":
                continue
            # elif how_far_away(start_line, start_char, line + i, char+j) <= furthest_away:
            #     continue
            elif line + i in seen_befores and char + j in seen_befores[line+i]:
                continue
            else:
                add_seen(line + i, char + j, distance_away+1)
                distance_away = crawl(start_line, start_char, line + i, char + j, distance_away + 1)

    return distance_away


def find_next_char(line, char, direction: list[int]):
    absolute_line = line + direction[0]
    absolute_char = char + direction[1]
    if absolute_line < 0 or absolute_char < 0 or absolute_char > 139 or absolute_line > 139:
        return "."
    return matrix[absolute_line][absolute_char]


def how_far_away(start_line, start_char, current_line, current_character):
    return abs(start_line - current_line) + abs(start_char - current_character)


def find_first_move(start_line, start_char):
    global seen_befores
    furthest = 0
    for i in range(start_line - 1, start_line + 2):
        for j in range(start_char - 1, start_char + 2):
            at_char = matrix[i][j]
            if at_char == "S" or at_char == ".":
                continue
            ranges = characters[at_char]
            for k in range(ranges[0][0], ranges[0][1]+1):
                for l in range(ranges[1][0], ranges[1][1]+1):
                    if i + k == start_line and j + l == start_char:
                        add_seen(i, j, 1)
                        distance = crawl(start_line, start_char, i, j, 1)
                        if distance > furthest:
                            furthest = distance
                        continue

    print(round(furthest/2 + 1e-10))

def intersect_both_keys_and_values(dict_list):
    common_outer_keys = set(dict_list[0].keys())
    for dictionary in dict_list[1:]:
        common_outer_keys.intersection_update(dictionary.keys())

    result = {}
    for key in common_outer_keys:
        common_inner_dict = {}
        reference_inner_dict = dict_list[0][key]
        for inner_key, inner_value in reference_inner_dict.items():
            if all(inner_key in d[key] and d[key][inner_key] == inner_value for d in dict_list[1:]):
                common_inner_dict[inner_key] = inner_value
        result[key] = common_inner_dict

    return result

def path():
    start_line = -1
    count = 0
    for line in fileinput.input("/Users/nathan.pringle/repos/advent-of-code/day10/input.txt"):
        line = line.replace("\n", "")
        if "S" in line:
            start_line = count
        matrix.append(line)

        count += 1

    start_char = matrix[start_line].find("S")
    # add_seen(start_line, start_char, 0)
    find_first_move(start_line, start_char)

if __name__ == "__main__":
    sys.setrecursionlimit(10000000) # Python has a recursion limit of 1k which isnt enough
    path()
