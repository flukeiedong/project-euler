from time import process_time as TIME


def import_test_cases():
    f = open("54.txt", "r")
    tc = f.readlines()
    for i in range(len(tc)):
        tc[i] = tc[i].rstrip("\n")
    return tc


def format_player(p):
    l = []
    for i in range(1, 6):
        l.append(p[3*(i-1):3*i].strip())
    return l


alpha = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def number_n_suit(p):
    number = []; suit = []
    for c in p:

        if c[0].isnumeric():
            number.append(int(c[0]))
        else:
            number.append(alpha[c[0]])

        suit.append(c[1])
    return number, suit


def has_multi(p):
    number, suit = number_n_suit(p)
    # print(number, suit)
    pair = []
    three_oak = []
    four_oak = []

    if len(number) == len(set(number)):
        return pair, three_oak, four_oak

    for num in set(number):
        if number.count(num) == 2:
            pair.append(num)
        elif number.count(num) == 3:
            three_oak.append(num)
        elif number.count(num) == 4:
            four_oak.append(num)
    return pair, three_oak, four_oak


def is_fullhouse(p):
    if not has_multi(p):
        return False
    else:
        pair, three_oak, four_oak = has_multi(p)

        if len(pair) == 1 and len(three_oak) == 1:
            return three_oak

        return False


def is_straight(p):
    number, suit = number_n_suit(p)
    number.sort()

    for i in range(4):
        if number[i+1] - number[i] != 1:
            return False
    return number[-1] # max number of straight


def is_flush(p):
    number, suit = number_n_suit(p)
    if len(set(suit)) == 1:
        return suit[0]
    return False

# is_flush(["8C", "KC", "7C", "TC", "2C"])


def is_royal_flush(p):
    number, suit = number_n_suit(p)
    number.sort()
    if number[0] == 10 and number[-1] == 14:
        return suit[0]


def find_max(p):
    number, suit = number_n_suit(p)
    return max(number)


def rank(p):
    flush = is_flush(p)
    straight = is_straight(p)
    if flush and straight:
        if is_royal_flush(p):
            return 10, is_royal_flush(p)
        else:
            return 9, straight

    pair, three_oak, four_oak = has_multi(p)
    if len(four_oak) == 1:
        return 8, four_oak[0]

    # check full house
    if len(pair) == 1 and len(three_oak) == 1:
        return 7, three_oak[0]

    if flush:
        return 6, flush
    if straight:
        return 5, straight

    if len(three_oak) == 1:
        return 4, three_oak[0]
    if len(pair) == 2:
        # print(pair)
        return 3, max(pair)
    if len(pair) == 1:
        return 2, pair[0]
    return 1, find_max(p)


# player_1 = ['9C', 'KS', 'KC', '9H', 'AS']
# player_2 = ['7D', '2S', '5D', '3S', 'AC']
# print(rank(player_1), rank(player_2))

class Player:

    def __init__(self, cards, rank=0, score=0):
        self.cards = cards
        self.rank = rank
        self.score = score

    def identify(self):
        rk, sc = rank(self.cards)
        self.rank = rk
        self.score = sc


test_cases = import_test_cases()

same = 0; different = 0
win_player_1 = 0; win_player_2 = 0
loop = 0; count_error = 0

for tc in test_cases:
    # if loop > 5:
    #     break
    # else:
    #     loop += 1

    player_1 = Player(format_player(tc[:14]))
    player_2 = Player(format_player(tc[15:]))
    player_1.identify()
    player_2.identify()
    # print(player_1.rank, player_2.rank)
    # player_1.identify(); player_2.identify()
    # print(player_1.rank, player_2.rank)

    if player_1.rank == player_2.rank:
        same += 1

        # if player_1.rank == 5:
        #     print(player_1.cards, player_1.score)
        #     print(player_2.cards, player_2.score)

        print(player_1.score, player_2.score)
        if player_1.score > player_2.score:
            win_player_1 += 1
        elif player_1.score < player_2.score:
            win_player_2 += 1
        else:
            count_error += 1
            print(player_1.cards, player_1.score)
            print(player_2.cards, player_2.score)
    else:
        if player_1.rank > player_2.rank:
            win_player_1 += 1
        elif player_1.rank < player_2.rank:
            win_player_2 += 1
        else:
            count_error += 1
            print(player_1.cards, player_1.score)
            print(player_2.cards, player_2.score)

print()
print(count_error)
print(same)
print(win_player_1, win_player_2)
print("EXECUTED IN", TIME())

# win_player_1 + 1 is the actual answer
# Haven't fixed case same pairs
# Only one case
#   same 5 pair
#   then check for single highest card
