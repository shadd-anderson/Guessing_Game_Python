"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    high_score = None
    name = input("Please enter your name: ")
    print("Welcome to the guessing game, {}!".format(name))
    high_score = play_game(high_score)
    playing = True
    while playing:
        again = input("Would you like to play again? y/N ").lower()
        if again == "y":
            high_score = play_game(high_score)
        else:
            print("Okay, come again soon!")
            playing = False


def play_game(top_score):
    highscore(top_score)
    number = random.randint(1, 50)
    game_won = False
    num_guesses = 0
    while game_won is False:
        guess = get_guess()
        if guess > 50 or guess < 1:
            print("Whoops! We're looking for a number between 1 and 50. Try again!")
        elif guess < number:
            print("Guess was too low. Try again!")
            num_guesses += 1
        elif guess > number:
            print("Guess was too high. Try again!")
            num_guesses += 1
        else:
            num_guesses += 1
            print("Congrats, you got it in {} tries!".format(num_guesses))
            if not top_score:
                top_score = num_guesses
                print("You set a new high score!")
            elif top_score and num_guesses < top_score:
                top_score = num_guesses
                print("You set a new high score!")
            game_won = True
    return top_score


def get_guess():
    proper_guess = False
    while not proper_guess:
        try:
            guess = int(input("Guess a number between 1 and 50: "))
            proper_guess = True
        except ValueError:
            print("Please only enter integers for a guess!")
    return guess


def highscore(high_score):
    print("The current high score is: {}".format(high_score if high_score else "None, set one now!"))


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
