import random

# Main Stories
'''
(5 points): As a developer, I want to make at least five commits on GitHub with descriptive  messages.

(10 points): As a developer, I want every function to be a pure function that does not modify or  
            access global variables. (Receives data through parameters and returns data through the  “return” keyword).

(5 points): As a pair player, I want a fifty-two (52) deck of cards to be created and stored in a List  (number/type only, no suits).

(2.5 points): As a pair player, I want to ensure that only four (4) of each number/type exist within the shuffled deck.

(5 points): As a pair player, I want to be able to shuffle the deck of cards so that they are in random order.

(5 points): As a pair player, I want five (5) cards dealt to four (4) players. 

(5 points): As a pair player, I want to determine the number of pairs within each player’s hand and display the player number, 
            their hand, and the number of pairs to the terminal. 

(5 points): As a pair player, I want to determine the game’s winner or tied players and display them to the terminal.  
'''

# Purpose: From list of individual card values, build and return (sorted) deck. (52 cards)
def build_deck():
    individual_card_values = ["Ace", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    sorted_deck = []
    count = 0

    for item in individual_card_values:
        while count < 4:
            sorted_deck.append(item)
            count += 1
            if count == 4:
                count = 0
                break
    #print(f'Sorted Deck:  {sorted_deck}\n')
    return sorted_deck

# Purpose: Take in (sorted) deck, return shuffled deck
def shuffle_deck():
    deck = build_deck()
    random.shuffle(deck)
    return deck
    
# Purpose: Take in a shuffled deck, choose 5 random cards, return built hand
def building_hand(deck_of_cards):
    hand_of_cards = []
    count = 0
    while count != 5:
        card = random.choice(deck_of_cards)
        hand_of_cards.append(card)
        count += 1
    return hand_of_cards

def building_all_players_hands(deck_of_cards):
    list_of_players = []
    for player in range(4):
        player = building_hand(deck_of_cards)
    

def main():
    shuffled_deck = shuffle_deck()
    result = building_hand(shuffled_deck)
    print(result)

    
main()


#sdfasdf