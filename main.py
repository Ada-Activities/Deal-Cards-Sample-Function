import random

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣︎"]
HAND_SIZE = 10

def build_deck():
    return [f"{card}{suit}" for card in CARDS for suit in SUITS]

def sample(items, count):

    if count > len(items) or count <= 0:
        raise ValueError("invalid number of samples")

    items = list(items)  # So we don't modify the passed in deck
    last_card = len(items) - 1
    picked_count = 0

    # Loop until we pick the requested count
    while picked_count < count:
        card_pos = random.randint(
            picked_count, last_card)  # Get a random position in the deck
        items[picked_count], items[card_pos] = (
            items[card_pos], items[picked_count]
        )  # Swap it to the "front" (our sampled area)
        picked_count += 1  # Move the end of the sample area

    # Return the sample area
    return items[0:picked_count]

# Write a function that deals 10 cards from a deck of cards without using the sample function
def deal_ten_cards(deck_of_cards):
    return sample(deck_of_cards, HAND_SIZE)


deck = build_deck()

# Sample draws
print("####### DRAWS #######")
print(", ".join(deal_ten_cards(deck)))
print(", ".join(deal_ten_cards(deck)))
print(", ".join(deal_ten_cards(deck)))
print(", ".join(deal_ten_cards(deck)))
print(", ".join(deal_ten_cards(deck)))

# prove the deck hasn't been modified
print("\n####### DECK #######")
print(", ".join(deck))

# sample too many
print("\n####### ERROR #######")
print(sample(deck, 53))