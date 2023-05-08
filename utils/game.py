import random #import random module to choose any word from the list possible_words
class Hangman:# create a hangman class
    
    possible_words = ['apple', 'banana', 'becode', 'learning', 'mathematics', 'sessions'] #creaate possible_words list
       
    def __init__(self):
        """ Initializes a new attributes of the Hangman class."""
        self.word_to_find = random.choice(Hangman.possible_words)#indicate where we get the word
        self.lives = 5 #indicate namber of lives
        self.correctly_guessed_letters = ['_'] * len(self.word_to_find)#indicate 1 letter and count the number of letter in the word_to_find
        self.wrongly_guess_letters = [] # collect wrong letters
        self.turn_count = 0 # the number of turns played by the player
        self.error_count = 0 # the number of errors made by the player

    def play(self):
            """Method that asks the player to enter a letter and evaluats a letter if it is guessed correctly or not."""
            
            letter = input("Enter a letter: ").lower() # asking to enter a letter
            if len(letter) == 1 and letter.isalpha():
                    if letter in self.word_to_find:
                        for i, char in enumerate(self.word_to_find):
                        #if the letter is correct
                            if char == letter:
                                self.correctly_guessed_letters[i] = letter
                                
                    
                    else: #if the letter is wrong
                        self.wrongly_guess_letters.append(letter) #add it to the `wrongly_guessed_letters` list
                        self.error_count += 1 #add 1 to `error_count`
                        self.lives -= 1 # remove 1 life
                    self.turn_count += 1         
            else: #if the lettre is wrong - enter another letter
                print("Only one character is acceptable.")
                self.play()

    def start_game(self):
        """Method  that start the game"""
        while True:
            self.play() # will call `play()` until the game is over (because the use guessed the word or because of a game over)
            print(" ".join(self.correctly_guessed_letters)) #  will print `correctly_guessed_letters`, 
            print(f"Wrongly guessed letters: {self.wrongly_guess_letters}.")
            print(f"You still have {self.lives} lives.") # `bad_guessed_letters`, `life`, `error_count` 
            print(f"You have made {self.error_count} errors.")
            print(f"You have made {self.turn_count} turns.") # and `turn_count` at the end of each turn.

            if self.lives == 0:# will call `game_over()` if `lives` is equal to 0
                self.game_over()
                break
            if "_" not in self.correctly_guessed_letters: # will call `well_played()` if all the letter are guessed.
                self.well_played()
                break

    def game_over(self): # A `game_over()` method that will stop the game and print `game over...`
        """method that will stop the game and print `game over...`"""
        print("Game over...")

    def well_played(self):
        """method that will print `You found the word: {word_to_find_here}
        in {turn_count_here} turns with {error_count_here} errors!`"""
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")   
    # A `well played()` method that will print `You found the word: 
    # {word_to_find_here} in {turn_count_here} turns 
    # with {error_count_here} errors!`
    