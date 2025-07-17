import random
import os
import time

class Player:
    def __init__(self, player_number, character, cards):
        self.character = character

        # Self.position will always either be an array as [x, y] for a hall space
        # or a string such as "Hall" if in a room

        self.player_number = player_number

        if self.character == "Miss Scarlett":
            self.position = [24, 7]
            self.color = "R"
        elif self.character == "Colonel Mustard":
            self.position = [17, 0]
            self.color = "Y"
        elif self.character == "Mrs. White":
            self.position = [0, 9]
            self.color = "W"
        elif self.character == "Reverend Green":
            self.position = [0, 14]
            self.color = "G"
        elif self.character == "Mrs. Peacock":
            self.position = [6, 23]
            self.color = "B"
        elif self.character == "Professor Plum":
            self.position = [19, 23]
            self.color = "P"

        self.cards = cards
        self.accusation = False
        self.moves = 0
        self.prior_position = self.position

    def get_position(self):
        return self.position
    
    def get_color(self):
        return self.color
    
    def get_character(self):
        return self.character
    
    def set_position(self, position):
        self.position = position
        self.prior_position = position

    def get_cards(self):
        return self.cards
    
    def get_player_number(self):
        return self.player_number
    
    def get_accusation(self):
        return self.accusation

    def move(self, board):
        # Roll for number of moves

        # IMPORTANT: Using testing value as 100
        # Replace with the following
        # self.moves = random.randint(1, 6)
        self.moves = 100

        os.system("cls" if os.name == "nt" else "clear")
        board.print_board()
        self.get_info()

        # Only move if you have not made an accusation
        if self.accusation:
            self.moves = 0
            print("Steps remaining: {}".format(self.moves))
            print("Current position: {}".format(self.position))
            print("You have already made an incorrect accusation! You have lost the game!")
        else:
            print("You have rolled a {}".format(self.moves))
            print("Steps remaining: {}".format(self.moves))
            print("Current position: {}".format(self.position))
        
        while self.moves > 0:

            # Determine open squares
            possible_moves = board.check_moves(self)
            for i in range(len(possible_moves)):
                print("Option {}: Move {} to {}".format(i+1, possible_moves[i][0], possible_moves[i][1]))

            # Ask user where they would like to move and enforce selection parameters
            selection = ""
            while type(selection) != int:
                try:
                    selection = input("Please enter an option number to move: ")
                    selection = int(selection)
                    if selection < 1 or selection > len(possible_moves):
                        print("Invalid selection: Please enter a value between 1 and {}".format(len(possible_moves)))
                        selection = ""
                    else:
                        selection -= 1
                except ValueError:
                    print("Invalid selection: Please enter a value between 1 and {}".format(len(possible_moves)))
            
            # Take step and save new position
            self.position = possible_moves[selection][1]
            self.moves -= 1

            # Set moves to 0 if they enter a room and set their room state
            if type(possible_moves[selection][1]) == str:
                self.moves = 0
                
            os.system("cls" if os.name == "nt" else "clear")
            board.print_board()
            self.get_info()

            print("Steps remaining: {}".format(self.moves))
            print("Current position: {}".format(self.position))
        
        # Make a suggestion after entering a room
        print("Position: {}, prior: {}".format(self.position, self.prior_position))
        if type(self.position) == str and self.position != self.prior_position:
            print("You have entered the {} and can now make a suggestion!".format(self.position))
            character_selection = ""
            weapon_selection = ""
            destination_selection = self.position

            # Character suggestion
            print("Suggest one of the following characters:")
            characters = board.get_characters()
            for i in range(len(characters)):
                print("Option {}: {}".format(i+1, characters[i]))
            while type(character_selection) != int:
                try:
                    character_selection = input("Please enter an option number to suggest a character: ")
                    character_selection = int(character_selection)
                    if character_selection < 1 or character_selection > len(characters):
                        print("Invalid selection: Please enter a value between 1 and {}".format(len(characters)))
                        character_selection = ""
                    else:
                        character_selection -= 1
                except ValueError:
                    print("Invalid selection: Please enter a value between 1 and {}".format(len(characters)))
            character_selection = characters[character_selection]
            
            # Weapon Suggestion
            print("Suggest one of the following weapons:")
            weapons = board.get_weapons()
            for i in range(len(weapons)):
                print("Option {}: {}".format(i+1, weapons[i]))
            while type(weapon_selection) != int:
                try:
                    weapon_selection = input("Please enter an option number to suggest a weapon: ")
                    weapon_selection = int(weapon_selection)
                    if weapon_selection < 1 or weapon_selection > len(weapons):
                        print("Invalid selection: Please enter a value between 1 and {}".format(len(weapons)))
                        weapon_selection = ""
                    else:
                        weapon_selection -= 1
                except ValueError:
                    print("Invalid selection: Please enter a value between 1 and {}".format(len(weapons)))
            weapon_selection = weapons[weapon_selection]

            print("You suggest that it was {} in the {} with the {}!".format(character_selection, destination_selection, weapon_selection))
            time.sleep(5)
            os.system("cls" if os.name == "nt" else "clear")

            # Move suggested player into the room
            for p in board.get_players():
                if p.get_character() == character_selection:
                    p.set_position(destination_selection)

            # Disprove guess
            disprove = board.disprove(self.player_number, character_selection, destination_selection, weapon_selection)

            if disprove[0]:
                print("Your suggestion was incorrect!")
                print("Player {} revealed the card: {}".format(disprove[1], disprove[2]))
            else:
                print("No one was able to disprove your suggestion!")

            self.prior_position = self.position


        # Offer accusation
        if not self.accusation:
            print("Would you like to make your final accusation?")
            print("Option 1: Yes")
            print("Option 2: No")
            accusation_selection = ""
            while type(accusation_selection) != int:
                try:
                    accusation_selection = input("Please enter an option number to select if you will make your final accusation: ")
                    accusation_selection = int(accusation_selection)
                    if accusation_selection < 1 or accusation_selection > 2:
                        print("Invalid selection: Please enter a value between 1 and 2")
                        accusation_selection = ""
                    else:
                        accusation_selection -= 1
                except ValueError:
                    print("Invalid selection: Please enter a value between 1 and 2")

            if accusation_selection == 0:
                character_selection = ""
                weapon_selection = ""
                destination_selection = ""

                # Character Accusation
                print("Accuse one of the following characters:")
                characters = board.get_characters()
                for i in range(len(characters)):
                    print("Option {}: {}".format(i+1, characters[i]))
                while type(character_selection) != int:
                    try:
                        character_selection = input("Please enter an option number to accuse a character: ")
                        character_selection = int(character_selection)
                        if character_selection < 1 or character_selection > len(characters):
                            print("Invalid selection: Please enter a value between 1 and {}".format(len(characters)))
                            character_selection = ""
                        else:
                            character_selection -= 1
                    except ValueError:
                        print("Invalid selection: Please enter a value between 1 and {}".format(len(characters)))
                character_selection = characters[character_selection]
                
                # Weapon Accusation
                print("Accuse one of the following weapons:")
                weapons = board.get_weapons()
                for i in range(len(weapons)):
                    print("Option {}: {}".format(i+1, weapons[i]))
                while type(weapon_selection) != int:
                    try:
                        weapon_selection = input("Please enter an option number to accuse a weapon: ")
                        weapon_selection = int(weapon_selection)
                        if weapon_selection < 1 or weapon_selection > len(weapons):
                            print("Invalid selection: Please enter a value between 1 and {}".format(len(weapons)))
                            weapon_selection = ""
                        else:
                            weapon_selection -= 1
                    except ValueError:
                        print("Invalid selection: Please enter a value between 1 and {}".format(len(weapons)))
                weapon_selection = weapons[weapon_selection]

                # Destination Accusation
                print("Accuse one of the following rooms:")
                destinations = board.get_destinations()
                for i in range(len(destinations)):
                    print("Option {}: {}".format(i+1, destinations[i]))
                while type(destination_selection) != int:
                    try:
                        destination_selection = input("Please enter an option number to accuse a room: ")
                        destination_selection = int(destination_selection)
                        if destination_selection < 1 or destination_selection > len(destinations):
                            print("Invalid selection: Please enter a value between 1 and {}".format(len(destinations)))
                            destination_selection = ""
                        else:
                            destination_selection -= 1
                    except ValueError:
                        print("Invalid selection: Please enter a value between 1 and {}".format(len(destinations)))
                destination_selection = destinations[destination_selection]

                print("You accuse {} in the {} with the {}!".format(character_selection, destination_selection, weapon_selection))

                self.accusation = True

                # Check Accusation
                if board.accuse(character_selection, weapon_selection, destination_selection):
                    print("You have used your clues and solved the mystery! Congratulations! You win!")
                else:
                    print("You have missed a critical piece of evidence and made an incorrect accusation! You lose!")
            time.sleep(5)
        

    def get_info(self):
        print("Hello Player {}!".format(self.player_number))
        print("Character: {}".format(self.character))
        print("Color/Symbol: {}".format(self.color))
        print("Position: {}".format(self.position))
        print("Cards: {}".format(self.cards))

    # STILL NEEDED
    # Add clue to middle of board
