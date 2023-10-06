import random

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

def create_deck():
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    value = sum(values[card['rank']] for card in hand)
    
    # Handle Aces
    aces = [card for card in hand if card['rank'] == 'Ace']
    for _ in range(len(aces)):
        if value > 21:
            value -= 10  # Change an Ace's value from 11 to 1 if it prevents busting
    
    return value

def blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("Welcome to Blackjack!")

    while True:
        print("\nYour hand:", [card['rank'] + ' of ' + card['suit'] for card in player_hand])
        print("Dealer's hand:", dealer_hand[0]['rank'] + ' of ' + dealer_hand[0]['suit'], "and an unknown card")
        
        player_value = calculate_hand_value(player_hand)
        if player_value == 21:
            print("Congratulations! You got a Blackjack!")
            break
        elif player_value > 21:
            print("Bust! You went over 21. You lose.")
            break
        
        action = input("Do you want to 'hit' or 'stand'? ").strip().lower()
        
        if action == 'hit':
            player_hand.append(deck.pop())
        elif action == 'stand':
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
            
            dealer_value = calculate_hand_value(dealer_hand)
            print("\nDealer's hand:", [card['rank'] + ' of ' + card['suit'] for card in dealer_hand])
            
            if dealer_value > 21:
                print("Dealer busts! You win.")
            elif dealer_value >= player_value:
                print("Dealer wins.")
            else:
                print("You win!")
            
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")

if __name__ == "__main__":
    blackjack()
