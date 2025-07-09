import random

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

    def getPos(self):
        return self.position
    
    def getColor(self):
        return self.color

    def move(self, board):
        # Roll for number of moves

        # IMPORTANT: Using testing value as 100
        # Replace with the following
        # self.moves = random.randint(1, 6)
        self.moves = 100

        # Only move if you have not made an accusation
        if self.accusation:
            print("You have already made an incorrect accusation!")
            self.moves = 0
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
                
            board.print_board()
            print("Steps remaining: {}".format(self.moves))
            print("Current position: {}".format(self.position))
        
        # Make a suggestion after entering a room
        if type(self.position) == str:
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

    def get_info(self):
        print("Hello Player {}!".format(self.player_number))
        print("Character: {}".format(self.character))
        print("Color/Symbol: {}".format(self.color))
        print("Position: {}".format(self.position))
        print("Cards: {}".format(self.cards))

    # STILL NEEDED
    # Guess a character, weapon, and the room you have just moved into
    # It is important to note that the room is fixed as the room you just entered
    # The player you guess must also move into the room with you - display this based on the active player

    # Need player movement, roll dice each turn, make movements

    # Create a message that says which player to pass the computer to and let them pick which card they are going to show you after a suggestion?
    # Or just show the same first card every time. This is how most people play anyway and simplifies the game