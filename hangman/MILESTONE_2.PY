import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """Initialize the Hangman game."""
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.select_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def select_random_word(self):
        """Select a random word from the word_list."""
        return random.choice(self.word_list)

    def check_guess(self, guess):
        """Check if the guessed letter is in the word."""
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """Ask the user to guess a letter."""
        while True:
            guess = input("Enter a single letter: ").strip()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

    def play_game(self):
        """Run the game loop until the game ends."""
        while True:
            if self.num_lives == 0:
                print("You lost!")
                break
            elif self.num_letters > 0:
                self.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                break

# Example usage:
if __name__ == "__main__":
    word_list = ["apple", "banana", "orange", "strawberry", "pineapple"]
    game = Hangman(word_list)
    game.play_game()
