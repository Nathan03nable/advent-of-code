import fileinput


gears = {}
related_numbers = {}
# Function to add/update an item
def add_item(x, y):
    if x not in gears:
        gears[x] = {}
    gears[x][y] = gears[x].get(y, 0) + 1

def update_related_nums(x, y, value):
    if x not in related_numbers:
        related_numbers[x] = {}

    if y not in related_numbers[x]:
        # Initialize with an empty list
        related_numbers[x][y] = []

        # Append the specified value to the list at this coordinate
    related_numbers[x][y].append(value)
def count():
    characters = []  # line index, char index, character

    line_counter = 0
    for line in fileinput.input("/Users/nathan.pringle/repos/advent-of-code/day3/input.txt"):
        char_counter = 0
        for char in line:
            if char != '.' and not char.isdigit() and char != "\n":
                characters.append((line_counter, char_counter, char))
            char_counter += 1
        line_counter += 1

    numbers: list[tuple[int, int, int, int]] = []  # line index, char index, whole number, length

    line_i = 0
    for line in fileinput.input("/Users/nathan.pringle/repos/advent-of-code/day3/input.txt"):
        char_i = 0
        i = 0
        while i < len(line):
            # if i != 0:
            #     i = i + times_looped
            if i < 140 and line[i].isdigit():
                length = 1
                whole_num = line[i]
                times_looped = 0

                while line[i+length].isdigit():
                    whole_num += line[i+length]
                    length += 1
                    times_looped += 1
                numbers.append((line_i, i, int(whole_num), length))
                char_i += length
                i += length
            char_i += 1
            i += 1

        line_i += 1

    valid_numbers: [(int, int, int)] = []
    for number in numbers:
        number_line_index = number[0]
        number_char_index = number[1]
        real_number = number[2]
        number_length = number[3]

        for char in characters:
            char_line_index = char[0]
            char_char_index = char[1]
            if abs(char_line_index - number_line_index) <= 1 and abs(char_char_index - number_char_index) <= 1:
                if (real_number, number_line_index, number_char_index) not in valid_numbers:
                    valid_numbers.append((real_number, number_line_index, number_char_index))
                    if char[2] == "*":
                        add_item(char_line_index, char_char_index)
                        update_related_nums(char_line_index, char_char_index, real_number)
            if abs(char_line_index - number_line_index) <= 1 and char_char_index - number_char_index <= number_length and char_char_index - number_char_index >= 0:
                if (real_number, number_line_index, number_char_index) not in valid_numbers:
                    valid_numbers.append((real_number, number_line_index, number_char_index))
                    if char[2] == "*":
                        add_item(char_line_index, char_char_index)
                        update_related_nums(char_line_index, char_char_index, real_number)
    return [t[0] for t in valid_numbers]

if __name__ == '__main__':
    nums = count()

    all_vals = 0
    for outer_key in gears:
        for inner_key in gears[outer_key]:
            if gears[outer_key][inner_key] == 2:
                the_nums = related_numbers[outer_key][inner_key]
                val = the_nums[0] * the_nums[1]
                all_vals += val

    print(all_vals)