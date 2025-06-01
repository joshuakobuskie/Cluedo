class CluedoBoard:
    def __init__(self):
        self.board = [
            ["X","X","X","X","X","X","X","X","X","H","X","X","X","X","H","X","X","X","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","X","H","H","H","X","X","X","X","H","H","H","X","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","H","H","X","X","X","X","X","X","X","X","H","H","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","H","H","X","X","X","X","X","X","X","X","H","H","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","H","H","X","X","X","X","X","X","X","X","H","H","UC","X","X","X","X","X"],
            ["X","X","X","X","X","X","H","H","RB","X","X","X","X","X","X","LB","H","H","H","X","X","X","X","X"],
            ["X","X","X","X","UA","X","H","H","X","X","X","X","X","X","X","X","H","H","H","H","H","H","H","H"],
            ["H","H","H","H","H","H","H","H","X","UB","X","X","X","X","UB","X","H","H","H","H","H","H","H","X"],
            ["X","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","X","X","X","X","X","X"],
            ["X","X","X","X","X","H","H","H","H","H","H","H","H","H","H","H","H","H","RE","X","X","X","X","X"],
            ["X","X","X","X","X","X","X","X","H","H","X","X","X","X","X","H","H","H","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","X","X","H","H","X","X","X","X","X","H","H","H","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","X","LD","H","H","X","X","X","X","X","H","H","H","X","X","X","X","UE","X"],
            ["X","X","X","X","X","X","X","X","H","H","X","X","X","X","X","H","H","H","H","H","H","H","H","X"],
            ["X","X","X","X","X","X","X","X","H","H","X","X","X","X","X","H","H","H","X","X","DF","X","X","X"],
            ["X","X","X","X","X","X","UD","X","H","H","X","X","X","X","X","H","H","X","X","X","X","X","X","X"],
            ["X","H","H","H","H","H","H","H","H","H","X","X","X","X","X","H","H","RF","X","X","X","X","X","X"],
            ["H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","X","X","X","X","X","X","X"],
            ["X","H","H","H","H","H","H","H","H","X","X","DH","DH","X","X","H","H","H","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","DG","H","H","X","X","X","X","X","X","H","H","H","H","H","H","H","H","H"],
            ["X","X","X","X","X","X","X","H","H","X","X","X","X","X","LH","H","H","H","H","H","H","H","H","X"],
            ["X","X","X","X","X","X","X","H","H","X","X","X","X","X","X","H","H","DI","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","X","H","H","X","X","X","X","X","X","H","H","X","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","X","H","H","X","X","X","X","X","X","H","H","X","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","X","H","X","X","X","X","X","X","X","X","H","X","X","X","X","X","X","X"]
        ]
        self.rooms = {"A":"Kitchen", "B":"Ballroom", "C":"Conservatory", "D":"Dining Room", "E":"Billiard Room", "F":"Library", "G":"Lounge", "H":"Hall", "I":"Study"}
        self.passages = {"Kitchen":"Study", "Conservatory":"Lounge", "Study":"Kitchen", "Lounge":"Conservatory"}

    def print_board(self):
        for row in self.board:
            for square in row:
                if list(square)[0] == "H":
                    print("#", end="")
                elif list(square)[0] != "X":
                    print("O", end="")
                else:
                    print(" ", end="")
            print()

    def check_moves(self, position):
        moves = []

        if position[0]-1 >= 0:
            # Check for halls
            if list(self.board[position[0]-1][position[1]])[0] == "H":
                moves.append(["Up", [position[0]-1, position[1]]])

            # Check for rooms
            elif list(self.board[position[0]-1][position[1]])[0] == "U":
                moves.append(["Up", self.rooms[list(self.board[position[0]-1][position[1]])[1]]])

        if position[0]+1 < len(self.board):
            # Check for halls
            if list(self.board[position[0]+1][position[1]])[0] == "H":
                moves.append(["Down", [position[0]+1, position[1]]])

            # Check for rooms
            elif list(self.board[position[0]+1][position[1]])[0] == "D":
                moves.append(["Down", self.rooms[list(self.board[position[0]+1][position[1]])[1]]])

        if position[1]-1 >= 0:
            # Check for halls
            if list(self.board[position[0]][position[1]-1])[0] == "H":
                moves.append(["Left", [position[0], position[1]-1]])

            # Check for rooms
            if list(self.board[position[0]][position[1]-1])[0] == "L":
                moves.append(["Left", self.rooms[list(self.board[position[0]][position[1]-1])[1]]])

        if position[1]+1 < len(self.board[0]):
            # Check for halls
            if list(self.board[position[0]][position[1]+1])[0] == "H":
                moves.append(["Right", [position[0], position[1]+1]])
            
            # Check for rooms
            if list(self.board[position[0]][position[1]+1])[0] == "R":
                moves.append(["Right", self.rooms[list(self.board[position[0]][position[1]+1])[1]]])

        return moves


board = CluedoBoard()
board.print_board()
print(board.check_moves([17, 12]))
print(board.check_moves([18, 6]))