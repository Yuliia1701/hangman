#import random module to choose any word from the list possible_words
import random
# create a hangman class
class hangman:
    #creaate possible_words list
    possible_words = ['apple', 'banana', 'becode', 'learning', 'mathematics', 'sessions']
       
    def __init__(self):
        """ Initializes a new attributes of the Hangman class.
        - A `possible_words` attribute that contains a list of words. Out of these words, one will be selected as the word to find. The list must also contain the following words: `['becode', 'learning', 'mathematics', 'sessions']`.
        - A `word_to_find` attribute that contains a list of strings. Each element will be a letter of the word.
        - A `lives` attribute that contains the number of lives that the player still has left. It should start at 5.
        - A `correctly_guessed_letters` attribute that contains a list of strings where each element will be a letter guessed by the user. At the start, it should be equal to: `_ _ _ _ _`, with the same number of `_` as the length of the word to find.
               Each time the player finds a letter, replace the `_` with the letter that the user suggested. If the word contains multiple times the same letter, the letter should be revealed at every place it appears in the word to find.
               For example, if the word to find is `P A P E R` and the first guess of the user is `P` then `correctly_guessed_letters` should be equal to `P _ P _ _`.
        - A `wrongly_guessed_letters` attribute that contains a list of strings where each element will be a letter guessed by the user that is not in the `word_to_find`.
        - A `turn_count` attribute that contain the number of turns played by the player. This will be represented as an `int`.
        - An `error_count` attribute that contains the number of errors made by the player."""
         #indicate where we get the word
        self.word_to_find = random.choice(hangman.possible_words)
        #indicate namber of lives
        self.lives = 5
       #indicate 1 letter and count the number of letter in the word_to_find
        self.correctly_guessed_letters = ['_'] * len(self.word_to_find)
        # collect wrong letters
        self.wrongly_guess_letters = []
        # the number of turns played by the player
        self.turn_count = 0
        # the number of errors made by the player
        self.error_count = 0

    def play(self):
            """Method that asks the player to enter a letter and evaluats a letter if it is guessed correctly or not.
            1. checks if a letter is a letter and if it is single letter
            2. If the player guessed a letter well, add it to the `correctly_guessed_letters` list
            3. If not, add it to the `wrongly_guessed_letters` list and add 1 to `error_count`
            4. the method counts errors, lives and how many attempts were made"""
            # asking to enter a letter
            letter = input("Enter a letter: ").lower()
            if len(letter) == 1 and letter.isalpha():
                    if letter in self.word_to_find:
                        for i in range(len(self.word_to_find)):
                        #if the letter is correct
                            if self.word_to_find[i] == letter:
                                self.correctly_guessed_letters[i] = letter
                                
                    #if the letter is wrong
                    else:
                        #add it to the `wrongly_guessed_letters` list
                        self.wrongly_guess_letters.append(letter)
                        #add 1 to `error_count`
                        self.error_count += 1
                        # remove 1 life
                        self.lives -= 1
                    self.turn_count += 1         
            else:
            #if the lettre is wrong - enter another letter
                print("Only one character is acceptable.")
                self.play()

    def start_game(self):
        """Method  that:
  - will call `play()` until the game is over (because the use guessed the word or because of a game over).
  - will call `game_over()` if `lives` is equal to 0.
  - will call `well_played()` if all the letter are guessed.
  - will print `correctly_guessed_letters`, `bad_guessed_letters`, `life`, `error_count` and `turn_count` at the end of each turn."""
        while True:
            # will call `play()` until the game is over 
            # (because the use guessed the word or because of a game over)
            self.play()
            #  will print `correctly_guessed_letters`, 
            # `bad_guessed_letters`, `life`, `error_count` 
            # and `turn_count` at the end of each turn.
            print(" ".join(self.correctly_guessed_letters))
            print(f"Wrongly guessed letters: {self.wrongly_guess_letters}.")
            print(f"You still have {self.lives} lives.")
            print(f"You have made {self.error_count} errors.")
            print(f"You have made {self.turn_count} turns.")

            # will call `game_over()` if `lives` is equal to 0
            if self.lives == 0:
                self.game_over()
                break
            # will call `well_played()` if all the letter are guessed.
            if "_" not in self.correctly_guessed_letters:
                self.well_played()
                break

    # A `game_over()` method that will stop the game and print `game over...`
    def game_over(self):
        """method that will stop the game and print `game over...`"""
        print("Game over...")

    # A `well played()` method that will print `You found the word: 
    # {word_to_find_here} in {turn_count_here} turns 
    # with {error_count_here} errors!`
    def well_played(self):
        """method that will print `You found the word: {word_to_find_here}
        in {turn_count_here} turns with {error_count_here} errors!`"""
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")   

