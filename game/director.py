from game.cards import Deck

class Director:
    """A person who is directing the game and controls the sequence of play.
    
    Attributes:
    total_score (int): The starting score, but will change with wins (+100 points)
    and loses (-75 points)
    is_playing (boolean): Whether or not the games is being player
    deck (Deck): an object with the deck attributes, used to shuffle and draw the playing cards
    pile []: the list of 2 playing cards that is being used as current_card(0) and next_card (1)
    """
    def __init__(self):
        """Constructs a new Director
        Args:
            self(Director): an instance of Director
        """
        self.total_score = 300
        self.is_playing = True
        self.deck = Deck()
        self.deck.shuffle()
        self.pile = []
        for x in range(2):
            self.pile.append(self.deck.drawcard())

    def start_game(self):
        """Starts the game by running the main game loop
        
        Args:
            self(Director): an instance of Director"""
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        """Reveals the first card and asks for the guess input which is higher or lower
        
        Args:
            self(Director): an instance of Director"""
        print(f"The card is: {self.pile[0]}")
        self.guess = input("Higher,Lower, or Equal? [h/l/e] ")
    
    def do_updates(self):
        """Prints the next cards and calculates points based on the previously inputted guess
        
        Args:
            self(Director): an instance of Director"""
        print(f"The next card is {self.pile[1]}")
        #calculates points
        if (self.pile[0].value < self.pile[1].value) and self.guess.lower() == "h" :
            self.total_score += 100
        elif (self.pile[0].value < self.pile[1].value) and self.guess.lower() == "l":
            self.total_score -=75
        elif (self.pile[0].value > self.pile[1].value) and self.guess.lower() == "h":
            self.total_score -=75
        elif (self.pile[0].value > self.pile[1].value) and self.guess.lower() == "l":
            self.total_score += 100
        elif (self.pile[0].value == self.pile[1].value) and self.guess.lower() == "e":
            self.total_score += 100
        elif (self.pile[0].value != self.pile[1].value) and self.guess.lower() == "e":
            self.total_score -=75

    
    def do_outputs(self):
        """Prints the total score, checks to see if that score is less than or equal to zero
        and asks the user if they would like to play again. If yes is selected the old current 
        card is removed and a new card is used as the new card
        
        Args:
            self(Director): an instance of Director"""
        def print_ascii(file_name):
            f=open(file_name, 'r')
            print(''.join([line for line in f]))
            return False

        print(f"Your score is: {self.total_score}")
        if self.total_score <=0:
            self.is_playing = print_ascii(r'CSE210W03\game\ascii_art.txt')
            
        else:
            playAgain = input("Play again? [y/n] ")

            if playAgain.lower() == "n":
                self.is_playing = self.is_playing = print_ascii(r'CSE210W03\game\ascii_art.txt')
                
            else:
                self.pile.pop(0)
                self.pile.append(self.deck.drawcard())
            print()