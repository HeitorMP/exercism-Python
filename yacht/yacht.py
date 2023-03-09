# Score categories.
# Change the values as you see fit.
YACHT = lambda score: 50 if len(set(score)) == 1 else 0
ONES = lambda score: score.count(1)
TWOS = lambda score: score.count(2) * 2
THREES = lambda score: score.count(3) * 3
FOURS = lambda score: score.count(4) * 4
FIVES = lambda score: score.count(5) * 5
SIXES = lambda score: score.count(6) * 6
FULL_HOUSE = lambda score: sum(score) if len(set(score)) == 2 and any(score.count(i) == 3 for i in score) else 0
FOUR_OF_A_KIND = lambda score: sum([x for x in score if score.count(x) >= 4][0:4])
LITTLE_STRAIGHT = lambda score: 30 if sum(score) == 15 else 0
BIG_STRAIGHT = lambda score: 30 if sum(score) == 20 else 0
CHOICE = lambda score: sum(score)



def score(dice, category):
    return category(dice)
