# Enigmatic Card Oracle: Unveil the Mysteries of Your Chosen Card

deck = [
    'King of Clubs (Black)',
    'King of Diamonds (Red)',
    'King of Spades (Black)',
    'King of Hearts (Red)',  
    'Queen of Clubs (Black)',
    'Queen of Hearts (Red)',
    'Queen of Spades (Black)',
    'Queen of Diamonds (Red)'
]

# Shuffling of cards
def shuffle_cards(cards):
    top_deck = cards[1::2]
    bottom_deck = cards[0::2]
    return top_deck, bottom_deck

# Get user input
def get_user_input():
    while True:
        user_input = input('Unlock the Secrets: Please enter "Yes" or "No": ').strip().lower()
        if user_input == 'yes' or user_input == 'no':
            return user_input
        else:
            print("Invalid input. Unravel the Enigma - Please enter 'Yes' or 'No' only.")

# Display cards
def display_cards(cards):
    for card in cards:
        print(f"- {card}")

print("Welcome to the Enigmatic Card Oracle!")
print("Unveil the Mysteries of Your Chosen Card:")
display_cards(deck)
input('Enter the Realm of Secrets...')

# Guessing the card (3 rounds)
for round_number in range(3):
    top_deck, bottom_deck = shuffle_cards(deck)
    
    print('\nDoes the card you seek reveal itself in the following selection?')
    display_cards(top_deck)

    user_input = get_user_input()

    if user_input == 'yes':
        deck = top_deck + bottom_deck
    else:
        deck = bottom_deck + top_deck

# The revelation
top_deck, bottom_deck = shuffle_cards(deck)
the_right_card = top_deck[0]

# Color and Suit
new_bottom_deck, new_top_deck = shuffle_cards(bottom_deck[::-1])
color = new_top_deck[0]
suit = new_bottom_deck[0]

print(f'\nThe Enigma Unveiled! Your chosen card is the {the_right_card}.')
print(f'It emanates a {color} aura of {suit}.')