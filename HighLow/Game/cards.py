import random

#Used symbols instead of words for card suits
card_suits = ["♥️", "♣️", "♦️", "♠️"]

#Name of each card
card_ranks = {
    "Ace",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King"
}

#Since ranks are set as strings this will give each card a numerical value
card_values = {
    "Ace": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13
}

'''This class will be used by the deck class to create all cards needed for the deck
A card will have a suit and a rank.
The rank will align with the value using the card values dictionary and the card ranks set
    Attributes:
        suit (str): pulled from the cards suits, total 4
        rank (str): pulled from the card ranks, name of card
        value (int): the value of the card
'''
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = card_values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

'''
A deck will create 52 cards using the Card class
the deck uses the for loop is the card_suits list to make 13 cards of each suit
    Attributes:
        deck (list): a list of all the cards
'''
class Deck:
    def __init__(self):
        self.deck = []
        for suit in card_suits:
            for rank in card_ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_print = ""
        for card in self.deck:
            deck_print += card.__str__() + f"\n"
        return deck_print

    def shuffle(self):
        random.shuffle(self.deck)

    def drawcard(self):
        return self.deck.pop()