import fileinput


def calculate_subvalues(values):
    a_subvalue = []
    for i in range(len(values) - 1):
        current_val = int(values[i])
        next_val = int(values[i + 1])

        diff = next_val - current_val
        a_subvalue.append(diff)
    return a_subvalue


def sequence():
    total_addition = 0
    for line in fileinput.input("/Users/nathan.pringle/repos/advent-of-code/day9/input.txt"):
        values = line.replace("\n", "").split(" ")
        subvalues = []
        a_subvalue = calculate_subvalues(values)
        subvalues.append(a_subvalue)
        for subvalue in subvalues:
            if any(element != 0 for element in subvalue):
                useless = 1
            else:
                break
            subvalue = calculate_subvalues(subvalue)
            subvalues.append(subvalue)

        addition = 0
        for i in range(len(subvalues) - 1):
            reversed_subvalues = subvalues.copy()
            reversed_subvalues.reverse()
            subvalue = reversed_subvalues[i]

            last_el = subvalue[0]
            reversed_subvalues[i + 1].insert(0, reversed_subvalues[i + 1][0] - last_el)
        addition += int(values[0]) - subvalues[0][0]

        total_addition += addition

    print(total_addition)


if __name__ == "__main__":
    sequence()
