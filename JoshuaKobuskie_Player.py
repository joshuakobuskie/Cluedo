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
        # Only move if you have not made an accusation
        if self.accusation:
            print("You have already made an incorrect accusation!")
            self.moves = 0

        while self.moves > 0:
            print("Steps remaining: {}".format(self.moves))

            # Determine open squares
            possible_moves = board.check_moves(self.position)
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

        print("Steps remaining: {}".format(self.moves))
        print("Current position: {}".format(self.position))

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

    # Add an entranceway and new room for the accusation station
