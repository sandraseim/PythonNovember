import random
end_of_game = False
word_list = ["printer", "mouse", "television", "keyboard", "charger", "cable"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

display = []
for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
        print("You have 6 lives and have to guess a word")
        guess = input("Guess a letter: ").lower()

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("you lose")
                print(f"The word is {chosen_word}")
        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("you win")
