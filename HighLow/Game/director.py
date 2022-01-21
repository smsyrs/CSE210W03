from game.cards import Deck
import game.ascii_art as art

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.deck = Deck()
        self.deck.shuffle()
        self.is_playing = True
        self.score = 0
        self.total_score = 75
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
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        self.current_cards.pop(0)
        self.current_cards.append(self.deck.drawcard())


    def check_answer(self,answer):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

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
            print("Game Over")
            self.is_playing = False