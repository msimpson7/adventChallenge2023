
input_file = 'puzzle_input.txt'
rank = 1
alpha = '23456789TJQKA'
order = {i: alpha.index(i) for i in alpha}

'''
Strength of the hand:
0 - High Card
1 - One Pair
2 - Two Pair
3 - Three of a Kind
4 - Full House
5 - Four of a Kind
6 - Five of a Kind
'''
def update_strength(h):
    count = {}
    for card in h['cards']:
        count.setdefault(card, 0)
        count[card] += 1
    print(f"For {h['cards']} the count is {count}")
    # TODO: update the strength of the hand
    if 5 in count.values():  # 5 of a kind
        h['strength'] = 6
    elif 4 in count.values():  # 4 of a kind
        h['strength'] = 5
    elif 3 in count.values() and 2 in count.values():  # full house
        h['strength'] = 4
    elif 3 in count.values():  # 3 of a kind
        h['strength'] = 3
    elif 2 in count.values() and len(count.values()) == 3:  # 2 pairs
        h['strength'] = 2
    elif 2 in count.values():  # 1 pair
        h['strength'] = 1
    else:  # High card
        h['strength'] = 0


def update_rank(hands):
    sorted_hands = sorted(hands, key=lambda k: [alpha.index(c) for c in k['cards']])
    sorted_hands.sort(key=lambda k: k['strength'])
    i = 1
    for hand in sorted_hands:
        hand['rank'] = i
        i += 1
    print(f'sorted_hands: {sorted_hands}')

    return sorted_hands


with open(input_file, 'r') as my_file:
    file_info = my_file.readlines()

hands = []
for info in file_info:
    cards, bid = info.split(' ')
    hand = {'cards': cards, 'bid': int(bid.replace('\n', '')), 'strength': 0, 'rank': 0}
    hands.append(hand)

for hand in hands:
    update_strength(hand)
    print(f'The hand looks like: {hand}')

hands = update_rank(hands)

total = 0
for hand in hands:
    total += hand['bid'] * hand['rank']

print(f'Total: {total}')
