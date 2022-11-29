import time
import os
from art import tprint
from .ascii_art import (print_hangman)
from .settings import (word, highscore, GUESSES, GUESS_MISTAKE,
                       FINISHED, SCORE, RULES_LIST,
                       stringing, SCORE_LIST, first_place,
                       second_place, third_place)



def clear():
    """
    Cleans the terminal when called
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def center_text(text_to_be_printed):
    """
    Prints tprint as ASCI ART
    """
    tprint(f"                {text_to_be_printed}")


center_text("Welcome")
center_text("To")
center_text("Hangman")


def print_new_line():
    """
    Prints new line
    """
    print("")


def save_score():
    """
    Saving score to google sheets
    """
    highscore.append_row(SCORE_LIST)


def get_nickname():
    """
    Takes users nickname and displays it
    """
    time.sleep(1)
    user_input = input("Put your nickname here: \n")
    nickname = user_input
    if user_input == "":
        print("Cant use empty nickname!")
        get_nickname()
    print_new_line()
    time.sleep(1)
    print(f"Your nickname is {user_input}.")
    print_new_line()
    SCORE_LIST.append(nickname)
    return SCORE_LIST


def rules():
    """
    Displays rules after setting your nickname up.
    """
    time.sleep(1)
    center_text("Rules")
    print_new_line()
    time.sleep(1)
    for index, rule in enumerate(RULES_LIST, start=1):
        print(index, rule)
        print_new_line()
        time.sleep(1)
    print("Enjoy the Hangman game.")
    time.sleep(3)
    print_new_line()
    for number in reversed(range(1, 6)):
        center_text(number)
        time.sleep(1)
    print_new_line()


def show_highscore():
    """
    Shows score for highscore in start_game
    """
    print_new_line()
    print(f"First place: {first_place[1]} and has {first_place[2]} points")
    print_new_line()
    print(f"Second places: {second_place[1]} and has {second_place[2]} points")
    print_new_line()
    print(f"Third place: {third_place[1]} and has {third_place[2]} points")
    print_new_line()


def guess_word():
    """
    Draws random word from list and makes it guessable
    """
    global word, GUESSES, GUESS_MISTAKE, FINISHED, SCORE, nickname
    while not FINISHED:
        print_new_line()
        for letter in word:
            if letter.lower() in GUESSES:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print_new_line()

        guess_input = input("Guess the letter: \n")
        GUESSES.append(guess_input.lower())

        if guess_input == "":
            print("\n Warning! your input cannot be empty")

        if guess_input.lower() not in word.lower():
            GUESS_MISTAKE -= 1
            print_hangman(GUESS_MISTAKE)
            if GUESS_MISTAKE == 0:
                break

        FINISHED = True
        for letter in word:
            if letter.lower() not in GUESSES:
                FINISHED = False

    if FINISHED:
        SCORE += 1
        print("Congratulations you guessed the word")
        print_new_line()
        print(f"your score is {SCORE}")
        print_new_line()
        finished_input = input("Do you want to 'continue' or 'finish'?\n")
        finish = finished_input.lower()
        print_new_line()
        if finish == "continue":
            clear()
            center_text("New word:")
            time.sleep(1)
            FINISHED = False
            GUESSES.clear()
            time.sleep(1)
            word = stringing()
            guess_word()
        elif finish == "finish":
            print_new_line()
            time.sleep(1)
            print("saving..")
            SCORE_LIST.append(SCORE)
            save_score()
            print("Thank you for playing!")
            return SCORE_LIST
        else:
            print("Ohh I see you put wrong input..")
            print("Abandoning the ship run the game agian")
    else:
        print("You lost all of ur lifes")
        print_new_line()
        center_text("Game Over")
