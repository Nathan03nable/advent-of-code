import fileinput

game = "Game"
red = "red"
green = "green"
blue = "blue"

def count():
    powers = []
    for line in fileinput.input("/Users/nathan.pringle/repos/advent-of-code/day2/input.txt"):
        line = line.replace(':', '').replace(';', '').replace(',', '')
        split = line.split()

        dictionary = {
            game: 0,
            red: 0,
            green: 0,
            blue: 0,
        }
        index = 0
        for word in split:
            if word == game:
                dictionary[game] += int(split[index + 1])
            if word == red:
                newval = int(split[index - 1])
                if newval > dictionary[red]:
                    dictionary[red] = newval
            if word == blue:
                newval = int(split[index - 1])
                if newval > dictionary[blue]:
                    dictionary[blue] = newval
            if word == green:
                newval = int(split[index - 1])
                if newval > dictionary[green]:
                    dictionary[green] = newval
            index += 1

        cube_power = dictionary[red] * dictionary[green] * dictionary[blue]
        powers.append(cube_power)
    return powers

if __name__ == '__main__':
    powers = count()
    print(sum(powers))
