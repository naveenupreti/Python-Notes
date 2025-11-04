'''
write a Python program to create and shuffle a deck of playing cards using the
random module — with an option to generate the deck with or without list comprehension.
'''

import random
print("=== DECK OF CARDS GENERATOR & SHUFFLER ===")

# Define suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

while True:
    print("\nChoose Deck Creation Method:")
    print("1. Without List Comprehension (using loops)")
    print("2. With List Comprehension (compact method)")

    # Get and validate user choice
    choice = input("Enter your choice (1 or 2): ").strip()
    if not choice.isdigit() or int(choice) not in (1, 2):
        print("❌ Invalid choice! Please enter 1 or 2.")
        again = input("Do you want to try again? (y/n): ").strip().lower()
        if again not in ('y', 'yes'):
            print("\nThank you for using the Deck Shuffler. Goodbye!")
            break
        else:
            continue

    choice = int(choice)

    # --- Option 1: Without List Comprehension ---
    if choice == 1:
        deck = []
        for suit in suits:
            for rank in ranks:
                card = rank + " of " + suit
                deck.append(card)
        print("\n✅ Deck created using loops.")

    # --- Option 2: With List Comprehension ---
    elif choice == 2:
        deck = [rank + " of " + suit for suit in suits for rank in ranks]
        print("\n✅ Deck created using list comprehension.")

    # Shuffle the deck
    random.shuffle(deck)
    print("\nDeck has been shuffled!")

    # Show top few cards
    print("\nFirst 5 cards after shuffling:")
    for card in deck[:5]:
        print(card)

    # Ask user if they want to continue
    again = input("\nDo you want to shuffle again? (y/n): ").strip().lower()
    if again not in ('y', 'yes'):
        print("\nThank you for using the Deck Shuffler. Goodbye!")
        break
