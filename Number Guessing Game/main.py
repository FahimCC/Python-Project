import random

print("To stop anytime, enter q")
score = 0
while True:
    number = random.randint(1, 10)
    guess = input("\nGuess a number between (0 to 10): ")

    if guess == 'q':
        print("\n\n\tGame Over.\nYour score is ", score)
        break

    if int(guess) == number:
        score += 10
        print("Your guessed is correct.\nYour new score is", score)
    else:
        print("Your guess is not correct.\nThe number is", number)
