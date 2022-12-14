import gspread
from google.oauth2.service_account import Credentials
from .helpers.api import (get_response_from_api)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hangman")

highscore = SHEET.worksheet("hangman_sheet")
word = get_response_from_api()
first_place = highscore.row_values(2)
second_place = highscore.row_values(3)
third_place = highscore.row_values(4)
SCORE_LIST = []
GUESSES = []
GUESS_MISTAKE = 7
FINISHED = False
SCORE = 0
RULES_LIST = ["Random word is printed out and you have to guess it",
              "Guess 1 letter at a time if its correct it will be displayed",
              "If not you lose one life out of seven"]
