
input_file = 'puzzle_input.txt'
rank = 1
alpha = 'J23456789TQKA'

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


def get_cards_count(card):
    count = {}
    for c in card:
        count.setdefault(c, 0)
        count[c] += 1

    maxval = max(count.values())
    keys = [k for k, v in count.items() if v == maxval]

    if 'J' in count:
        if 'J' not in keys:
            count[keys[0]] += count['J']
            count['J'] = 0
        elif 'J' in keys and len(keys) > 1:
            keys.remove('J')
            count[keys[0]] += count['J']
            count['J'] = 0
        elif 'J' in keys and count['J'] == 5:
            pass
        else:
            j_count = count['J']
            del count['J']
            maxval = max(count.values())
            keys = [k for k, v in count.items() if v == maxval]
            count[keys[0]] += j_count

    return count


def update_strength(h):
    count = get_cards_count(h['cards'])
    print(f"For {h['cards']} the count is {count}")

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

hands = update_rank(hands)

total = 0
for hand in hands:
    total += hand['bid'] * hand['rank']

print(f'Total: {total}')
