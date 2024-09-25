# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_valid_input(prompt):
    while True:
        try:
            # Prompt user for input
            value = int(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("Error, negative number. Please enter a number from 0 to 100")
        except ValueError:
            # Handle the case were input is not an integer
            print("Invalid input. Please enter a valid integer from 0 to 100")

def validate_input1():
    n = get_valid_input("Enter a secret number from 0 to 100: ")
    return n

def validate_input2():
    m = get_valid_input("Guess the secret number entered by player one. \nEnter a number from 0 to 100: ")
    return m

def compare_numbers(secret, guess):
    if secret > guess:
        print()
        print("Your guess is smaller than the secret number. ")
    elif secret < guess:
        print()
        print("Your guess is bigger than the secret number. ")
    else:
        print()
        print("You guesed it!  Bravo. You want a cookie?"
              "\nGet out of here! ")
        return True # Return True when the guess is correct
    return False # Return False if the guess is incorrect

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    secret_number = validate_input1()
    counter = 0
    max_attempts = 5
    while counter < max_attempts:
        guess = validate_input2()
        if compare_numbers(secret_number,guess): # Breaks if guessed correctly
            break
        counter += 1
        if counter == max_attempts:
            print("Boo hoo you loose sucka! ")



