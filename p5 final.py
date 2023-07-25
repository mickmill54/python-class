print("Hello")

#greet user
name = input("What is your name? ")
print("Welcome to the Guessing Game,", name)

#prompt user to enter word
word_to_guess = input("Enter a guess word (blank to quit): ")

# Check if the word is blank, if so, exit the program
if not word_to_guess:
    print("Goodbye!")
    exit()

print("Good Luck!", name )

# prompts user to guess
print("Guess a letter of the word,", name)

# Initialize variables for matched, unmatched, total guesses, and turns
matched_guesses = ""
unmatched_guesses = ""
total_guesses = 0
turns = 5

while turns > 0:

    # ask user to guess
    guess_letter = input("Enter a guess letter (blank to quit): ")

    # Check if the user wants to quit
    if not guess_letter:
        print("Goodbye!")
        break

    # Check for letter in word
    if len(guess_letter) != 1:
        print("\t> Only enter a single letter")
        continue

    # Increment the total number of guesses
    total_guesses += 1

    # Check if the letter is contained within the word
    if guess_letter in word_to_guess:
        # Check if the letter has been guessed before
        if guess_letter in matched_guesses:
            print(f"\t> {guess_letter} already guessed and found")
        else:
            matched_guesses += guess_letter
            print(f"\t> {guess_letter} found")
    else:
        # Check if the letter has been guessed before
        if guess_letter in unmatched_guesses:
            print(f"\t> {guess_letter} already guessed and not found")
        else:
            unmatched_guesses += guess_letter
            print(f"\t> {guess_letter} not found")

        # Subtract a turn
        turns -= 1
        # Print the number of turns left for the user
        print("You have", turns, 'more guesses')

    # Display the list of guessed letters
    all_guesses = matched_guesses + unmatched_guesses
    print(f"\t> Guesses so far: {all_guesses}")

    # Check if the word has been completely guessed
    if all(letter in matched_guesses for letter in word_to_guess):
        print("You Win!")
        break

if turns == 0:
    print("You Lose!")

# Display the final results
print("\n*** Results ***")
print(f"Word:\t\t{word_to_guess}")
print(f"Matched:\t{matched_guesses}")
print(f"Unmatched:\t{unmatched_guesses}")
print(f"Guesses:\t{total_guesses}")


    

 
    