import fileinput
def winners():
    scratchcards = {}
    for line in fileinput.input("/Users/nathan.pringle/repos/advent-of-code/day4/input.txt"):
        card_num = int(line.replace("\n", "").split(": ")[0].split("Card ")[1])
        if card_num == 1:
            scratchcards[card_num]=1
        elif card_num not in scratchcards:
            scratchcards[card_num]= 1
        elif card_num!=1:
                scratchcards[card_num]+=1
        all_nums = line.replace("\n", "").split(": ")[1]
        winners = all_nums.split(" |")[0].split(" ")
        my_nums = all_nums.split("| ")[1].split(" ")


        loop_counter = 1
        if card_num != 1:
            loop_counter = scratchcards[card_num]
        for i in range(loop_counter):
            winning_cards = 0
            for num in my_nums:
                if num == "":
                    continue
                for winner in winners:
                    if num == winner:
                        winning_cards += 1
                        break
            for i in range(card_num + 1, card_num + winning_cards + 1):
                scratchcards[i] = (scratchcards.get(i) or 0) + 1

    return sum(scratchcards.values())
if __name__ == '__main__':
    points = winners()
    print(points)