import fileinput
import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_of_list(numbers):
    if not numbers:
        return 0
    lcm_result = numbers[0]
    for number in numbers[1:]:
        lcm_result = lcm(lcm_result, number)
    return lcm_result


# Example usage

def left_right():
    instruction_converter = {
        'L': 0,
        'R': 1
    }
    all_nodes = {}
    all_lines = ""
    for line in fileinput.input("/Users/nathan.pringle/repos/advent-of-code/day8/input.txt"):
        all_lines += line

    splity = all_lines.split("\n")
    instructions = splity[0]
    nodes = splity[2:]
    ends_in_a = []
    for node in nodes:
        key = node.split(" = ")[0]
        if key[2] == "A":
            ends_in_a.append(key)
        vals = node.split(" = ")[1]
        left = vals.split(", ")[0].replace("(", "")
        right = vals.split(", ")[1].replace(")", "")
        all_nodes[key] = (left, right)

    multiples = []

    for node in ends_in_a:
        next_key = node
        count = 0
        while next_key[2] != "Z":
            instruction_count = count
            if count > len(instructions)-1:
                instruction_count = count % len(instructions)
            element = instruction_converter[instructions[instruction_count]]
            next_key = all_nodes[next_key][element]
            count += 1
            if next_key[2] == "Z":
                multiples.append(count)
                break

    print(lcm_of_list(multiples))

if __name__ == "__main__":
    left_right()