import fileinput
ranks = {
    'A': 1,
    'K': 2,
    'Q': 3,
    'T': 4,
    '9': 5,
    '8': 6,
    '7': 7,
    '6': 8,
    '5': 9,
    '4': 10,
    '3': 11,
    '2': 12,
    'J': 13,
}



def camel():
    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    total_lines = 0
    for line in fileinput.input("/Users/nathan.pringle/repos/advent-of-code/day7/input.txt"):
        total_lines += 1
        card_count = {}
        splito = line.split(" ")
        cards = splito[0]
        bet = splito[1].strip()

        jokers = 0
        for card in cards:
            if card == "J":
                jokers+=1
            elif card != "J":
                card_count[card] = (card_count.get(card) or 0) + 1

        if cards == "JJJJJ":
            card_count["J"] = 5
        for key in card_count.keys():
            card_count[key] += jokers
        if cards == "8JJJA":
            hi = 2
        a_three = 0
        a_two = 0
        a_four = 0
        a_five = 0

        num_of_threes = 0
        num_of_twos = 0
        num_of_fours = 0
        for val in card_count.values():
            if val == 4:
                num_of_fours+=1
            if val == 3:
                num_of_threes+=1
            if val == 2:
                num_of_twos+=1

        if num_of_fours == 2:
            highest_card = 'J'
            for card in card_count.keys():
                if ranks[card] < ranks[highest_card]:
                    highest_card = card
            for card in card_count.keys():
                if card != highest_card:
                    card_count[card] -= 3

        if num_of_threes == 3:
            highest_card = 'J'
            for card in card_count.keys():
                if ranks[card] < ranks[highest_card]:
                    highest_card = card
            for card in card_count.keys():
                if card != highest_card:
                    card_count[card] -= 2

        if num_of_threes==1 and num_of_twos==2:
            for card in card_count.keys():
                if card_count[card] == 2:
                    card_count[card] -= 1
        if num_of_twos == 4:
            highest_card = 'J'
            for card in card_count.keys():
                if ranks[card] < ranks[highest_card]:
                    highest_card = card
            for card in card_count.keys():
                if card != highest_card:
                    card_count[card] -= 1
        for res in card_count.values():
            if res == 5 or res == 10:
                five_of_a_kind.append((cards, bet))
                a_five += 1
            elif res == 4:
                four_of_a_kind.append((cards, bet))
                a_four += 1
            elif res == 3:
                a_three +=1
            elif res == 2:
                a_two += 1
        if a_five == 0 and a_four ==0:
            if (a_three > 0 and a_two > 0) or a_three > 1:
                full_house.append((cards, bet))
            elif a_three > 0:
                three_of_a_kind.append((cards, bet))
            elif a_two > 1:
                two_pair.append((cards, bet))
            elif a_two > 0:
                one_pair.append((cards, bet))
            elif a_four == 0 and a_five == 0:
                high_card.append((cards, bet))
    sortay(five_of_a_kind)
    sortay(four_of_a_kind)
    sortay(full_house)
    sortay(three_of_a_kind)
    sortay(two_pair)
    sortay(one_pair)
    sortay(high_card)

    big_total = 0
    total, lines_used = calculate_total(five_of_a_kind, total_lines)
    big_total += total
    total_lines -= lines_used

    total, lines_used = calculate_total(four_of_a_kind, total_lines)
    big_total += total
    total_lines -= lines_used

    total, lines_used = calculate_total(full_house, total_lines)
    big_total += total
    total_lines -= lines_used

    total, lines_used = calculate_total(three_of_a_kind, total_lines)
    big_total += total
    total_lines -= lines_used

    total, lines_used = calculate_total(two_pair, total_lines)
    big_total += total
    total_lines -= lines_used

    total, lines_used = calculate_total(one_pair, total_lines)
    big_total += total
    total_lines -= lines_used

    total, lines_used = calculate_total(high_card, total_lines)
    big_total += total
    total_lines -= lines_used

    return big_total

def calculate_total(some_list, rank):
    total = 0
    lines_used = 0
    for el in some_list:
        total += int(el[1])*rank
        lines_used+=1
        rank -=1
    return total, lines_used
def sortay(some_list):
    for i in range(len(some_list)):
        for j in range(0, len(some_list)-i-1):
            subject_cards = some_list[j+1][0]
            compare_cards = some_list[j][0]

            diff = False
            count = 0
            while diff == False:
                if count == len(subject_cards):
                    diff = True
                    break
                subj_val_of_el = ranks[subject_cards[count]]
                comp_val_of_el = ranks[compare_cards[count]]

                if subj_val_of_el < comp_val_of_el:
                    some_list[j], some_list[j+1] = some_list[j+1], some_list[j]
                    diff = True
                elif subj_val_of_el > comp_val_of_el:
                    diff = True
                    break
                count += 1

if __name__ == "__main__":
    tot = camel()
    print(tot)
