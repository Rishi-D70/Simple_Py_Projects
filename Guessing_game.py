import random
number = random.randint(1,100)
print("Welcome to the number guessing game user")
guess = float(input('Enter a guess between 0 - 100: '))
number_of_guesses = 0
guess_limit = 7
out_of_guesses = False

while guess != number and not(out_of_guesses):
    if guess > number and number_of_guesses != guess_limit:
        print("Your guess is too high")
        number_of_guesses += 1
        print("Number of guesses left ", guess_limit - number_of_guesses)
        guess = float(input('Enter another guess: '))
    elif guess < number and number_of_guesses != guess_limit:
        print("Your guess is too low")
        number_of_guesses += 1
        print("Number of guesses left ", guess_limit - number_of_guesses)
        guess = float(input('Enter another guess: '))
    elif number_of_guesses == guess_limit:
        print("Out of guesses, YOU LOSE!")
print("Your guess", str(guess), "is correct, You took", str(number_of_guesses), "Tries \n Thankyou for playing ")










