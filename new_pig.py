class Human():
    """This controls and tracks all of the information associated with the human."""

    def __init__(self, round_score=0, total_score=0, roll_again=True):
        self.round_score = round_score
        self.total_score = total_score
        self.roll_again = roll_again

    def is_user_input_valid(self):
        """Checks whether or not the user_input is valid, if it isn't, requires input again."""

        human_roll_decision = input(f"You have scored {self.round_score} points this turn. Would you like to roll again?")

        while human_roll_decision.startswith("Y", "y", "N", "n") == False:
             human_roll_decision = input(f"You must enter yes or no to decide. Your score for this turn is {self.round_score}")
        
        return human_roll_decision
        
        ##Unknown if working propery, still needs testing along with hold_or_roll_again.

    
    def hold_or_roll_again(self):
        """Checks whether the human wishes to hold or roll again. Only accepts yes or no answers."""

        roll_or_hold = self.is_user_input_valid()

        if roll_or_hold.startswith("y", "Y"):
            self.roll_again = True
        elif roll_or_hold.startswith("n", "N"):
            self.roll_again = False

        ##Put the while loop that makes sure the user_input is acceptable into a different function.
            
            





class Computer():
    """This controls and tracks all of the information assoiated with the computer and also controls a simple algorithm that determines certain computer gameplay decisions"""

    def __init__(self, roll_again, round_score=0, total_score=0, minimum_hold_score=20):
        self.roll_again = roll_again
        self.round_score = round_score
        self.total_score = total_score
        self.minimum_hold_score = minimum_hold_score


    def minimum_score_checker(self, round_score, minimum_hold_score):
        """If the round score isn't above the minimum needed for the CPU to hold, it rolls again."""
        if round_score <= minimum_hold_score:
            self.roll_again = True
        else:
            self.roll_again = False



class Gameplay():
    """This contains the basic rules and parameters for the game."""

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2