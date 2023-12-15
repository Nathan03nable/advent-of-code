def horizontal(all_lines, matches):
    total_matches = 0
    for match in matches:
        first_line = match[0]
        second_line = match[1]

        a_diff = False
        for i in range(len(all_lines)):
            backwards_index = first_line - i
            if backwards_index < 0:
                break
            backwards_line = all_lines[backwards_index]

            forwards_index = second_line + i
            if forwards_index >= len(all_lines):
                break
            forwards_line = all_lines[forwards_index]
            if backwards_line == forwards_line:
                total_matches += 1
            elif only_1_diff_chars(backwards_line, forwards_line):
                a_diff = True
            else:
                a_diff = False
                break
        if a_diff:
            return second_line
    return 0


def vertical(all_lines):
    i = 0
    match_columns = []
    previous_column = ''
    all_columns = []
    while i < len(all_lines[0]):
        column = ''
        for j in range(len(all_lines)):
            column += all_lines[j][i]
        if column == previous_column or only_1_diff_chars(column, previous_column):
            match_columns.append((i-1, i))
        all_columns.append(column)
        previous_column = column
        i += 1
    return all_columns, match_columns

def only_1_diff_chars(string1, string2):
    diff_count = sum(1 for a, b in zip(string1, string2) if a != b)

    return diff_count == 1

def mirrors():
    total = 0
    with open("input.txt") as f:
        lines = f.read()
        chunks = lines.split("\n\n")
    for chunk in chunks:
        all_lines = []
        previous_line = ''
        line_count = 0
        matches = []
        lines = chunk.split("\n")
        for line in lines:
            line = line.strip()
            all_lines.append(line)

            if line == previous_line or only_1_diff_chars(line, previous_line):
                matches.append((line_count - 1, line_count))
            line_count += 1
            previous_line = line
          
        horz = horizontal(all_lines, matches)
        things = vertical(all_lines)
        all_columns = things[0]
        columns_matches = things[1]

        vertz = horizontal(all_columns, columns_matches)

        if horz is None:
            horz = 0
        if vertz is None:
            vertz = 0
        if vertz != 0 or horz != 0:
            total += horz * 100 + vertz
    print(total)

if __name__ == "__main__":
    mirrors()

