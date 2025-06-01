class Player:
    def __init__(self, character):
        self.character = character

        if self.character == "Miss Scarlett":
            self.position = [24, 7]
        elif self.character == "Colonel Mustard":
            self.position = [17, 0]
        elif self.character == "Mrs. White":
            self.position = [0, 9]
        elif self.character == "Reverend Green":
            self.position = [0, 14]
        elif self.character == "Mrs. Peacock":
            self.position = [6, 23]
        elif self.character == "Professor Plum":
            self.position = [19, 23]
        else:
            print("Invalid Character!")

        self.cards = []
        self.accusation = False
        self.moves = 0
        self.room = None

    def move(self):
        for _ in range(self.moves):
            return 1
            # Determine open squares

            # Ask user where they would like to move

            # Set moves to 0 if they enter a room and set their room state
            
            # Set room state to None if exiting a room
