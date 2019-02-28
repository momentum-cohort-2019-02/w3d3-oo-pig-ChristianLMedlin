from new_pig import Computer, Human, Gameplay

def test_minimum_score_checker():
    player = Computer(None)

    player.minimum_score_checker(25, 20)
    assert player.roll_again == False

    player.minimum_score_checker(15, 20)
    assert  player.roll_again == True


def test_hold_or_roll_again():
    player = Human()
    
    human_roll_decision = "y"
    assert player.roll_again == True

    human_roll_decision = "n"
    assert player.roll_again == False