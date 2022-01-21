from game.cards import Deck
import game.ascii_art as art

class Director:
    def __init__(self):
        self.total_score = 300
        self.isPlaying = True
        self.deck = Deck()
        self.deck.shuffle()
        self.pile = []
        for x in range(2):
            self.pile.append(self.deck.drawcard())

    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        print(f"The card is: {self.pile[0]}")
        self.guess = input("Higher,or Lower? [h/l] ")
    
    def do_updates(self):
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

    
    def do_outputs(self):
        #Checks for a losing score (0 or below)
        print(f"Your score is: {self.total_score}")
        if self.total_score <=0:
            self.is_playing = False
        else:
            playAgain = input("Play again? [y/n] ")

            if playAgain.lower() == "n":
                self.is_playing = False
            else:
                self.pile.pop(0)
                self.pile.append(self.deck.drawcard())
            print()