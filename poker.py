import random

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]

players = {
    "Player 1": [],
    "Player 2": [],
    "Player 3": [],
    "Player 4": [],
}

random.shuffle(deck)

for _ in range(2):
    for player in players:
        card = deck.pop()
        players[player].append(card)

community_card = []

deck.pop()
for _ in range(3):
    community_card.append(deck.pop())

deck.pop()
community_card.append(deck.pop())

deck.pop()
community_card.append(deck.pop())

for player, hand in players.items():
    print(f"{player}: {hand}")

print("")
print("Community cards:")
print(community_card)