from JoshuaKobuskie_Gameboard import CluedoBoard

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

        self.cards = []
        self.accusation = False
        self.moves = 3

        # Self.position will always either be an array as [x, y] for a hall space
        # or a string such as "Hall" if in a room

    def move(self, board):
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
                    selection -= 1
                except ValueError:
                    print("Invalid selection: Please enter a value between 1 and {}".format(len(possible_moves)))
                

            # Set moves to 0 if they enter a room and set their room state
            if type(possible_moves[selection][1]) == str:
                self.moves = 0
            
            # Take step and save new position
            self.position = possible_moves[selection][1]
            self.moves -= 1


        print("Steps remaining: {}".format(self.moves))
        print("Current position: {}".format(self.position))

test = Player("Miss Scarlett")
board = CluedoBoard()
test.move(board)