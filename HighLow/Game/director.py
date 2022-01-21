from game.cards import Deck
import game.ascii_art as art

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        deck (List[deck]): A 52 deck of cards is created and the shuffled
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): Players current score
        current_cards(List): Two cards are taken from the deck list.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.deck = Deck()
        self.deck.shuffle()
        self.is_playing = True
        self.total_score = 300
        self.current_cards = []
        for x in range(2):
            self.current_cards.append(self.deck.drawcard())

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            print(self.is_playing)
            self.get_inputs()
            self.get_card()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        print(f"Current Card: {self.current_cards[0]}")
        self.check_answer(input("Will the next card be higher or lower? [H/L]").capitalize())
        if self.total_score > 0:
            print(f"Current Score: {self.total_score}")
            keep_playing = input("Would you like to continue? [Y/N] ").capitalize()
            self.is_playing = (keep_playing == "Y")
       
    def get_card(self):
        """Gets a new card to add to current cards list

        Args:
            self (Director): An instance of Director.
        """
        self.current_cards.pop(0)
        self.current_cards.append(self.deck.drawcard())


    def check_answer(self,answer):
        """Checks players answer and determines if the game can continue base on players score

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        if answer == "H" and self.current_cards[0].value < self.current_cards[1].value:
            self.total_score += 100
            print(f"Card was {self.current_cards[1]}\nCorrect, 100 points added to score")
        elif answer == "L" and self.current_cards[0].value > self.current_cards[1].value:
            self.total_score += 100
            print(f"Card was {self.current_cards[1]}\nCorrect, 100 points added to score")
        else:
            self.total_score -= 75
            print(f"Card was {self.current_cards[1]}\nIncorrect, 75 points subtracted from score")

        if self.total_score < 0:
            print(art.game_over)
            self.is_playing = False