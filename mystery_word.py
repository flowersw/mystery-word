import random


def easy_words(word_list):
    easy_word_list = []
    for words in word_list:
        if len(words) >= 4 and len(words) <= 6:
            easy_word_list.append(words)
    return easy_word_list


def medium_words(word_list):
    normal_word_list = []
    for words in word_list:
        if len(words) >= 6 and len(words) <= 8:
            normal_word_list.append(words)
    return normal_word_list


def hard_words(word_list):
    hard_word_list = []
    for words in word_list:
        if len(words) >=8:
            hard_word_list.append(words)
    return hard_word_list

def random_word(word_list):
    word_choice = random.choice(word_list)
    return word_choice

def pick_random_word(word_list):
    easy_words(word_list)
    medium_words(word_list)
    hard_words(word_list)
    difficulty = input("Welcome to mystery word What difficulty would you like to play on Easy, Normal or Hard?  ")
    if difficulty.lower() == "easy":
        print("You have chosen Easy")
        word = random.choice(easy_words)
        return word
    elif difficulty.lower() == "normal":
        print("You have chosen Normal")
        word = random.choice(easy_words)
        return word
    elif difficulty.lower() == "hard":
        print("You have chosen Hard")
        hard_word_choice = random.choice(easy_words)
        return word
    else:
        print("Invalid entry")
        random_word(word_list)
word = "integration"
list_of_guesses = ['i', 'g', 't', 'e', 'r']

def display_word(word, list_of_guesses):
    blank_slate = []
    correct_guesses = []
    incorrect_guesses = []
    #Initiliaze empty cells
    for blanks in range(len(word)):
        blank_slate.append("_ ")

    blank_slate[-1] = '_'


    for guess in list_of_guesses:
        if guess in word:
            correct_guesses.append(guess)
        else:
            incorrect_guesses.append(guess)

    for i in range(len(word)):
        if word[i] in correct_guesses:
            blank_slate = list(blank_slate[:i]) + list(word[i]) + list(blank_slate[i+1:])

    blank_slate = str(blank_slate)

    blank_slate.join('')

    print(blank_slate)








def is_word_complete(word, correct_guessed_letters):
    correct_letters = []

    for letters in word:
        if letters not in correct_letters:
            correct_letters.append(letters)

    is_game_won = False

    if sorted(correct_letters) == sorted(correct_guessed_letters):
        is_game_won = True
    else:
        is_game_won = False

    return is_game_won
