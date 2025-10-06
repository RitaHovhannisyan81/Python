print("Start guessing.")
word = "secret"
guesses = ''
turns = 6

while turns > 0:
    failed = 0
    print()  # նոր տող
    for el in word:
        if el in guesses:
            print(el, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\nYou won!")
        break

    guess = input("\nGuess a character: ").lower()
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong guess.")
        print(f"You have {turns} turns left.")

    # կախաղանի փուլերը ըստ սխալների քանակի (turns-ի)
    if turns == 5:
        print("\n+---+")
        print(" O   |")
        print("     |")
        print("     |")
        print("=====")
    elif turns == 4:
        print("\n+---+")
        print(" O   |")
        print(" |   |")
        print("     |")
        print("=====")
    elif turns == 3:
        print("\n+---+")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("=====")
    elif turns == 2:
        print("\n+---+")
        print(" O   |")
        print("/|\\  |")
        print("     |")
        print("=====")
    elif turns == 1:
        print("\n+---+")
        print(" O   |")
        print("/|\\  |")
        print("/    |")
        print("=====")
    elif turns == 0:
        print("\n+---+")
        print(" O   |")
        print("/|\\  |")
        print("/ \\  |")
        print("=====")
        print("You lose! The word was:", word)
