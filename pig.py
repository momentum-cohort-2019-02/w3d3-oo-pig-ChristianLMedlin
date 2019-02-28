import random







class Game:

    def __init__(self, player1, player2, current_score=0, round_score=0, roll_again=True):
        self.player1 = player1
        self.player2 = player2
        self.current_score = current_score
        self.round_score = round_score
        self.roll_again = roll_again


    def dice_roller(self):
        #Should return the number that was rolled, while roll again == True, recurse the function,
        #else, return a non-int
        while roll_again == True:
            self.round_score += random.randrange(1, 7)
            roll_again_checker()
            print(self.round_score)
        print("This turn has ended")
        
        

    def roll_again_checker(self, roll_again):
        #Currently filled in with dummy information to check dice_roller. Will contain a function that checks if the
        #player should roll again.
        
        
        if self.round_score >= 5:
            self.roll_again = False
        else:
            self.roll_again = True


    def round_score_from_dice(self):
        #Should check whether or not dice_roller returns an int. If it does, add it to round_score
        r



class Computer:
    """Contains all information and rules regarding computer gameplay."""
    
    roll_again = True

    def __init__(self, minimum_score_to_hold):
        self.minimum_score = minimum_score_to_hold

    def is_minimum_score_reached(self, minimum_score):
        if self.round_score <= self.minimum_score_to_hold:
            roll_again = True
        else:
            roll_again = False












if __name__ == "__main__":
    p1 = None
    p2 = Computer(20)

    game = Game(p1, p2)

    game.dice_roller()




