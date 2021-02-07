import words
import random
import art
def getWord():
    return random.choice(words.word_list)

def play():
    selected_word = getWord()
    word_len = len(selected_word)
    print(selected_word)
    guess_wordList = ["_"] * word_len
    lives = 6
    endGame = False
    while not endGame:
        letter = input("Guess a letter: ").lower()
        if letter not in guess_wordList:
            for i in range(word_len):
                if selected_word[i] == letter:
                    guess_wordList[i] = letter
            if letter not in guess_wordList:
                print(f"You guessed {letter}, that's not in the word. You lose a life.")
                lives -= 1
        else:
            print("Already guessed the letter")
        print(" ".join(guess_wordList))
        if lives == 0:
            endGame = True
            print("You lose")
            print(f"Actual Word is {selected_word}")
        elif "_" not in guess_wordList:
            print("You win")
            endGame = True
        print(art.stages[lives])


if __name__ == '__main__':
    print(art.logo)
    play()




