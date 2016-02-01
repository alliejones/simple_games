from collections import Counter


score_types = ["Aces","Twos","Threes","Fours","Fives","Sixes",
         "Three of a Kind","Four of a Kind","Full House", "Small Straight",
         "Large Straight", "Chance", "Yahtzee", "Yahtzee Bonus"]



def check_for_straight(array):
    '''checks if the passed array is a straight'''
    #hand is always sorted lowest to highest
    for index, number in enumerate(array):
        if index < len(array)-1:
            if array[index + 1] - 1 != number:
                return False
    return True

def remove_duplicate_dice(hand):
    '''removes duplicates from hand (helper method to check_for_straight)'''
    no_dupes = list(set(hand))
    #sets do not preserve order, so just in case
    no_dupes.sort()
    return no_dupes
    
def check_for_points(hand):
    '''for the given hand, checks for any possible points'''
    #does not care what the player has already used
    possible_scores = {key: 0 for key in score_types}
    for die in hand:
        if die == 1:
            possible_scores["Aces"] += 1
        elif die == 2:
            possible_scores["Twos"] += 2
        elif die == 3:
            possible_scores["Threes"] += 3
        elif die == 4:
            possible_scores["Fours"] += 4            
        elif die == 5:
            possible_scores["Fives"] += 5
        elif die == 6:
            possible_scores["Sixes"] += 6

    total = sum(hand)
    possible_scores["Chance"] = total

    counter = Counter(hand).most_common(2)
    #counter[0][1] is the count of the most common element
    
    if counter[0][1] == 5:
        possible_scores["Yahtzee"] = 50
        possible_scores["Yahtzee Bonus"] = 100
    if counter[0][1] >= 4:
        possible_scores["Four of a Kind"] = total
    if counter[0][1] >= 3:
        possible_scores["Three of a Kind"] = total
        if len(counter) > 1 and counter[1][1] == 2:
            possible_scores["Full House"] = 25
    
        
    no_dupes = remove_duplicate_dice(hand)
    
    if check_for_straight(hand):
        possible_scores["Large Straight"] = 40
        possible_scores["Small Straight"] = 30
    elif len(no_dupes) == 4 and check_for_straight(no_dupes):
        possible_scores["Small Straight"] = 30

    return possible_scores



def tally_score(player):
    '''tallies the players score card'''
    total = sum(player.score_card.values())
    first_half_total = 0
    for key in score_types[:6]:
        first_half_total += player.score_card[key]
    if first_half_total >= 63:
        total += 35
    print(first_half_total)
    return total
    
        
    
