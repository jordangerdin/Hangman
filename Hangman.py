from random import randint

def main():

    dictionary = ["capstone", "javascript", "python", "android", "programming", "pizza", "tacos", "spaghetti"]
    word = dictionary[selectWord(dictionary)]
    guesses = []

    while(True):
        # Guess letters
        guess = guessLetter(guesses)
        checkletters(word, guess)
        showletters(word, guesses)
        if(checkwin(word, guesses)):
            break

def guessLetter(guesses):
    letter = input("Guess a letter: ")
    while True:
        if (letter.isalpha() and len(letter) == 1):
            break
        letter = input("Please enter a single letter A-Z only")

    guesses.append(letter)
    return letter


def checkletters(word, guess):
    count = 0
    for char in word:
        if char == guess:
            count += 1
    
    print("There are " + str(count) + " " + str(guess) + " in the word.")


def showletters(word, guesses):
    for char in word:
        if char in guesses:
            print(char + " ", end='')
        else:
            print("_ ", end='')
    print()


def checkwin(word, guesses):
    wordmatch = ''
    for char in word:
        if char in guesses:
            wordmatch += char
        else:
            wordmatch += "*"
    
    if word == wordmatch:
        print("Congrats! You've guessed the word!")
        return True
    else:
        return False


def selectWord(words):
    return randint(0, len(words) - 1)

if __name__ == '__main__':
    main()