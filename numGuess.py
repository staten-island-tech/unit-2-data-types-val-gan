import random

def numGuess():
    num = random.randint(1, 10)
    guessHistory = []
    guess = int(input("Guess a random integer between 1 and 10\n"))
    while guess != num:
        if guess < num:
            guessHistory.append(guess)
            print(f"Numbers used: {guessHistory}\n")
            guess = int(input("Guess is too low, try again\n"))   
        elif guess > num:
            guessHistory.append(guess)
            print(f"Numbers used: {guessHistory}\n")
            guess = int(input("Guess is too high, try again\n"))
    guessHistory.append(guess)
    print("You got it right, congrats!\n")
    print("Here are all your guesses:\n")
    for i in guessHistory:
        print(f"{i} ")
    print(f"It took you {len(guessHistory)} times to get it right.")

numGuess()