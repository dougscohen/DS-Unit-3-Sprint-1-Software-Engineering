
# NOT finished yet

# from app.game import determine_winner

# FYI normally we'd have this application code (determine_winner()) in another file,
# ... but for this exercise we'll keep it here
def determine_winner(user_choice, computer_choice):
    '''choices should either be 'rock' or 'paper' or 'scissors' '''

    if user_choice == computer_choice:
        winner = None
    elif user_choice == "rock" and computer_choice == "scissors":
        winner = "rock"
    return "rock" # todo: write logic here to make the tests pass!

def test_determine_winner():
    assert determine_winner("rock", "rock") == None
    assert determine_winner("rock", "paper") == "paper"
    assert determine_winner("rock", "scissors") == "rock"

    assert determine_winner("paper", "rock") == "paper"
    assert determine_winner("paper", "paper") == None
    assert determine_winner("paper", "scissors") == "scissors"

    assert determine_winner("scissors", "rock") == "rock"
    assert determine_winner("scissors", "paper") == "scissors"
    assert determine_winner("scissors", "scissors") == None