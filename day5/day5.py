import fileinput


def find_location():
    all_lines = ""
    for line in fileinput.input("/Users/nathan.pringle/repos/advent-of-code/day5/input.txt"):
        all_lines += line

    #print("Made the first string")
    past_seeds = all_lines.split("seeds: ")[1]

    seeds = past_seeds.split("seed-to-soil map:\n")[0].split("\n")[0].split(" ")
    seed_list = []
    counter = 2
    for i in range(len(seeds)):
        if counter%2 == 0:
            seed_list.append((int(seeds[i]), int(seeds[i+1])))
        counter+=1

    seed_soil = past_seeds.split("seed-to-soil map:\n")[1].split("soil-to-fertilizer map:\n")[0].split("\n")
    soil_fertilizer = past_seeds.split("soil-to-fertilizer map:\n")[1].split("fertilizer-to-water map:\n")[0].split(
        "\n")
    fertilizer_water = past_seeds.split("fertilizer-to-water map:\n")[1].split("water-to-light map:\n")[0].split("\n")
    water_to_light = past_seeds.split("water-to-light map:\n")[1].split("light-to-temperature map:\n")[0].split("\n")
    light_to_temperature = past_seeds.split("light-to-temperature map:\n")[1].split("temperature-to-humidity map:\n")[
        0].split("\n")
    temperature_to_humidity = \
    past_seeds.split("temperature-to-humidity map:\n")[1].split("humidity-to-location map:\n")[0].split("\n")
    humidity_to_location = past_seeds.split("humidity-to-location map:\n")[1].split("\n")

    #print("Made all the arrays")

    #print("Made the maps")
    lowest = 999999999999999999999999
    list_of_all_seeds = set()
    # for tup in seed_list:
    #     for seed in range(tup[0], tup[0]+tup[1]):
    #         list_of_all_seeds.add(seed)

    # #print("On seed " + str(seed))
    for i in range(10000000000):
        #print("Checking location " + str(i))
        humidity = inverse(humidity_to_location, int(i))
        temperature = inverse(temperature_to_humidity, int(humidity))
        light = inverse(light_to_temperature, int(temperature))
        water = inverse(water_to_light, int(light))
        fertilizer = inverse(fertilizer_water, int(water))
        soil = inverse(soil_fertilizer, int(fertilizer))
        seed = inverse(seed_soil, int(soil))

        for ravey_seed in seed_list:
            if seed in range(ravey_seed[0], ravey_seed[0]+ravey_seed[1]):
                return i

        # if int(location) < lowest:
        #     lowest = int(location)
    return lowest

    #print("Location is " + str(location))

    #print("Finished seed " + str(seed))

def calculate_something(some_array, seed):
    for line in some_array:
        if line == "":
            continue
        nums = line.split(" ")
        source = int(nums[1])
        destination = int(nums[0])  # Input is given the wrong way around!
        rangey = int(nums[2])

        if seed in range(source, source+rangey):
            diff = destination-source
            return seed+diff
    return seed

def inverse(some_array, seed):
    for line in some_array:
        if line == "":
            continue
        nums = line.split(" ")
        source = int(nums[0])
        destination = int(nums[1])  # Input is given the wrong way around!
        rangey = int(nums[2])

        if seed in range(source, source+rangey):
            diff = destination-source
            return seed+diff
    return seed

if __name__ == '__main__':
    location = find_location()
    print(location)
