import random

title = """ _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_/
                       _/ |                
                      |__/ """

print(title)

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
def draw():
    index = random.randint(0, 12)
    return deck[index]

def cal_score(cards):
    score = 0
    for i in cards:
        score += i

    #TODO handle multiple Aces
    if score > 21 and 11 in cards:
        score -= 10

    return score

def dealers_hand_str():
    dealer_cards = dealers_hand.copy()
    dealer_cards[1] = "*"
    return dealer_cards

def players_turn():
    """
    Returns the players score
    """
    score = cal_score(players_hand)
    while True:
        display_hands()
        if input("Do you wanna to hit? Y or N\n").lower() == "y":
            players_hand.append(draw())
            print(f"players hand {players_hand}")
            score = cal_score(players_hand)
            if score > 21:
                break
        else:
            break
    return score

def dealers_turn():
    """
    Returns the dealers score
    """
    score = cal_score(dealers_hand)
    while score < 17:
        dealers_hand.append(draw())
        score = cal_score(dealers_hand)
    return score

def display_hands():
    print(f"Your hand: {players_hand}")
    print(f"Dealers hand: {dealers_hand_str()}")

playing = True
while playing:
    dealers_hand = [draw(), draw()]
    players_hand = [draw(), draw()]

    players_score = cal_score(players_hand)
    if players_score == 21:
        print("Black Jack! You win!")
        if input("Do you wanna play another hand? Y or N\n").lower() == "n":
            playing = False
        continue

    dealers_score = 0
    players_score = players_turn()
    if players_score <= 21:
        dealers_score = dealers_turn()

    print(f"Your hand: {players_hand}")
    print(f"Dealers hand: {dealers_hand}")

    if players_score > 21:
        print("You busted!")
    elif dealers_score > 21:
        print("Dealer busted. You win!")
    elif dealers_score == players_score:
        print("Draw!")
    elif players_score > dealers_score:
        print("You win!")
    else:
        print("You lose")

    if input("Do you wanna play another hand? Y or N\n").lower() == "n":
        playing = False
