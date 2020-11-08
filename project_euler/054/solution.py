#!/usr/bin/python3

from functools import reduce

VALUES = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}

# Utils
def load_file(filename):
    hands = []
    with open(filename) as f:
        for line in f:
            hand = []
            for ch in line.strip('\n').split(' '):
                hand.append(ch)
            hands.append(hand)
    return hands

def count_occurences(hand, index):
    count = {}
    for card in hand:
        if card[index] in count:
            count[card[index]] += 1
        else:
            count[card[index]] = 1
    return count

def same_of_a_kind(hand, card_count, times):
    count = count_occurences(hand, 0)
    sames = filter(lambda x: x[1] == card_count, count.items())
    values = list(map((lambda x: VALUES[x[0]]), sames))
    if len(values) == times:
        return sum(values)
    return 0

def same_suit(hand):
    count = count_occurences(hand, 1)
    return len(count) == 1

def consecutive_values(hand):
    values = list(map((lambda x: VALUES[x[0]]), hand))
    sorted_hand = sorted(values)
    for index, card in enumerate(sorted_hand):
        if index > 0 and sorted_hand[index - 1] != card - 1:
            return 0
    return sorted_hand[-1]

def get_highest_different_card(hand1, hand2):
    sorted_values1 = list(reversed(sorted(map((lambda x: VALUES[x[0]]), hand1))))
    sorted_values2 = list(reversed(sorted(map((lambda x: VALUES[x[0]]), hand2))))
    for index in range(len(sorted_values1)):
        if sorted_values1[index] != sorted_values2[index]:
            return (sorted_values1[index], sorted_values2[index])
    return (0, 0)

# Hands
def high_card(hand, power):
    return max(map(lambda x: VALUES[x[0]], hand)) * 10 ** power

def one_pair(hand, power):
    return same_of_a_kind(hand, 2, 1) * 10 ** power

def two_pairs(hand, power):
    return same_of_a_kind(hand, 2, 2) * 10 ** power

def three_of_a_kind(hand, power):
    return same_of_a_kind(hand, 3, 1) * 10 ** power

def straight(hand, power):
    return consecutive_values(hand) * 10 ** power

def flush(hand, power):
    return 10 ** power if same_suit(hand) else 0

def full_house(hand, power):
    pair_result = one_pair(hand, 0) * 2
    triple_result = three_of_a_kind(hand, 0) * 3
    return (pair_result + triple_result) * 10 ** power if pair_result and triple_result else 0

def four_of_a_kind(hand, power):
    return same_of_a_kind(hand, 4, 1) * 10 ** power

def straight_flush(hand, power):
    return consecutive_values(hand) * 10 ** power if same_suit(hand) else 0 

def royal_flush(hand, power):
    max_value = consecutive_values(hand)
    return max_value * 10 ** power if same_suit(hand) and max_value == VALUES['A'] else 0

# Game
check_hands = [high_card, one_pair, two_pairs, three_of_a_kind, straight, flush, full_house, four_of_a_kind, straight_flush, royal_flush]

def get_winner(game):
    person1 = 0
    person2 = 0
    for index, fn in reversed(list(enumerate(check_hands))):
        person1 += fn(game[:5], index)
        person2 += fn(game[5:], index)
        if person1 == person2 and person1 > 0:
            # get highest card
            (highest1, highest2) = get_highest_different_card(game[:5], game[5:])
            person1 += highest1
            person2 += highest2
        if person1 != person2:
            # we have a winner
            return 1 if person1 > person2 else 0
    return 0

person1_wins = 0
all_games = load_file('poker.txt')
for game in all_games:
    person1_wins += get_winner(game)
print(person1_wins)
