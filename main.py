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

# Purpose: Print intro to game
def intro():
    intro = '''
Welcome to Player Pairs!
In this game each player will receive 5 cards.
Once each hand has been dealt, we will compare to see who has the most pairs!
    '''
    return intro

# Purpose: From list of individual card values, build and return (sorted) deck. (52 cards)
def build_deck():
    individual_card_values = ["Ace", '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    sorted_deck = []
    count = 0

    for item in individual_card_values:
        while count < 4:
            sorted_deck.append(item)
            count += 1
            if count == 4:
                count = 0
                break
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
        deck_of_cards.remove(card)
        count += 1
    return hand_of_cards

# Purpose: Initializes 4 players, places them in list and returns list
def initialize_players():
    player_1 = []
    player_2 = []
    player_3 = []
    player_4 = []
    list_of_players = [player_1, player_2, player_3, player_4]
    return list_of_players

# Purpose: Takes in list of players, assigns built hands to players
def assigning_hand_to_players(list_of_players):
    deck_of_cards = shuffle_deck()
    count = 1
    while count < 5:
        for index in range(len(list_of_players)):
            list_of_players[index] = building_hand(deck_of_cards)
            count += 1
    return list_of_players

# Purpose: Takes in list of players, prints string of players hand
def print_player_hands(players):
    pairs_list = []
    list_of_players = assigning_hand_to_players(players)
    count = 1
    for player in list_of_players:
        pairs = check_for_pairs(player)
        pairs_list.append(int(pairs))
        print(f'Player {count}:\nHand: {player}\nNumber of Pairs: {pairs}\n')
        count += 1
    return pairs_list

# Purpose: Determine who won or tied
def determine_winner(players):
    pairs_list = print_player_hands(players)
    max_pair = max(pairs_list)
    winners = []
    for index in range(len(pairs_list)):
        if pairs_list[index] == max_pair:
            winners.append(index + 1)
    return winners

# Purpose: Print winners or tie
def print_winner(winners_list):
    winning_string = f"There was a tie among players {winners_list}\n" if len(winners_list) > 1 else f"Winner is Player {winners_list[0]}\n"
    print(winning_string)

# Purpose: Checks players hand for pairs, returns amount of pairs in hand
def check_for_pairs(hand):
    pairs = [card for card in hand if hand.count(card) > 1]
    list_of_pairs = list(set(pairs))
    number_of_pairs = (len(list_of_pairs))
    return number_of_pairs

# Purpose: Main - run program
def main():
    list_of_players = initialize_players()
    print(intro())
    winners = determine_winner(list_of_players)
    print_winner(winners)



main()
