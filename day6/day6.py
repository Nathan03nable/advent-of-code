import fileinput

def race():
    total_winners = 1
    times = []
    dists = []
    for line in fileinput.input("/Users/nathan.pringle/repos/advent-of-code/day6/input.txt"):
        if "Time" in line:
            times = line.split("Time: ")[1].replace(" ", "").replace("\n", "")
        if "Distance" in line:
            dists = line.split("Distance: ")[1].replace(" ", "")

    time = int(times)
    dist = int(dists)

    winners = 0
    for j in range(time):
        time_left = time - j
        charge = j
        dist_travelled = charge * time_left
        if dist_travelled > dist:
            winners+=1
    total_winners*=winners
    return total_winners

if __name__ == "__main__":
    wins = race()
    print(wins)