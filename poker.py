import random

card_set = ["2 Clubs", "3 Clubs", "4 Clubs", "5 Clubs", "6 Clubs",
            "7 Clubs", "8 Clubs", "9 Clubs", "10 Clubs",
            "2 Hearts", "3 Hearts", "4 Hearts", "5 Hearts", "6 Hearts",
            "7 Hearts", "8 Hearts", "9 Hearts", "10 Hearts",
            "2 Spades", "3 Spades", "4 Spades", "5 Spades", "6 Spades",
            "7 Spades", "8 Spades", "9 Spades", "10 Spades",
            "2 Diamonds", "3 Diamonds", "4 Diamonds", "5 Diamonds", "6 Diamonds",
            "7 Diamonds", "8 Diamonds", "9 Diamonds", "10 Diamonds",
            "Ace of Clubs", "Ace of Hearts", "Ace of Spades", "Ace of Diamonds"]

players = {
    "Player 1": [],
    "Player 2": [],
    "Player 3": [],
    "Player 4": [],
}

random.shuffle(card_set)

for _ in range(2):
    for player in players:
        card = card_set.pop()
        players[player].append(card)

for player, hand in players.items():
    print(f"{player}: {hand}")