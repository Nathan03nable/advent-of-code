import fileinput


def starhop():
    universe = []
    empty_lines = []
    count = 0
    for line in fileinput.input("/Users/nathan.pringle/repos/advent-of-code/day11/input.txt"):
        line = line.replace("\n", "")
        if '#' not in line:
            empty_lines.append(count)
        universe.append(line)
        count += 1

    i = 0
    empty_columns = []
    while i < len(universe[0]):
        gal_found = False
        for j in range(len(universe)):
            if universe[j][i] == '#':
                gal_found = True
                break
        if not gal_found:
            empty_columns.append(i)
        i += 1
    galaxies = []

    line_count = 0
    for line in universe:
        char_count = 0
        for char in line:
            if char == "#":
                galaxies.append((line_count, char_count))
            char_count += 1
        line_count += 1

    total = 0
    for i in range(len(galaxies)):
        subject = galaxies[i]
        for j in range(i + 1, len(galaxies)):
            comparison = galaxies[j]

            subj_column = subject[1]
            comp_column = comparison[1]

            range_start = min(subj_column, comp_column)
            range_end = max(subj_column, comp_column)
            columns_to_account = sum(1 for num in range(range_start, range_end + 1) if num in empty_columns)

            subj_line = subject[0]
            comp_line = comparison[0]

            line_range_start = min(subj_line, comp_line)
            line_range_end = max(subj_line, comp_line)
            lines_to_account = sum(1 for num in range(line_range_start, line_range_end + 1) if num in empty_lines)

            diff = abs(subject[0] - comparison[0]) + abs(subject[1] - comparison[1])

            diff += columns_to_account * (1000000-1) + lines_to_account * (1000000-1)
            total += diff

    print(total)


if __name__ == "__main__":
    starhop()

