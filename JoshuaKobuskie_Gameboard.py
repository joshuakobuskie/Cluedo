import random
import numpy as np
from JoshuaKobuskie_Player import Player

class CluedoBoard:
    def __init__(self):
        self.board = [
            ["X","X","X","X","X","X","X","X","X","H","X","X","X","X","H","X","X","X","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","X","H","H","H","X","X","X","X","H","H","H","X","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","H","H","X","X","X","X","X","X","X","X","H","H","X","X","X","X","X","X"],
            ["ZK","ZT","ZC","ZH","ZN","X","H","H","X","ZB","ZA","ZL","ZL","ZR","ZM","X","H","H","X","ZC","ZO","ZN","ZS","X"],
            ["X","X","X","X","X","X","H","H","X","X","X","X","X","X","X","X","H","H","UC","X","X","X","X","X"],
            ["X","X","X","X","X","X","H","H","RB","X","X","X","X","X","X","LB","H","H","H","X","X","X","X","X"],
            ["X","X","X","X","UA","X","H","H","X","X","X","X","X","X","X","X","H","H","H","H","H","H","H","H"],
            ["H","H","H","H","H","H","H","H","X","UB","X","X","X","X","UB","X","H","H","H","H","H","H","H","X"],
            ["X","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","X","X","X","X","X","X"],
            ["X","X","X","X","X","H","H","H","H","H","H","H","H","H","H","H","H","H","RE","X","X","X","X","X"],
            ["X","X","X","X","X","X","X","X","H","H","X","X","X","X","X","H","H","H","X","X","X","X","X","X"],
            ["X","ZD","ZI","ZN","ZE","ZR","ZM","X","H","H","X","X","X","X","X","H","H","H","X","ZB","ZL","ZR","ZD","X"],
            ["X","X","X","X","X","X","X","LD","H","H","X","X","X","X","X","H","H","H","X","X","X","X","UE","X"],
            ["X","X","X","X","X","X","X","X","H","H","X","X","X","X","X","H","H","H","H","H","H","H","H","X"],
            ["X","X","X","X","X","X","X","X","H","H","X","X","X","X","X","H","H","H","X","X","DF","X","X","X"],
            ["X","X","X","X","X","X","UD","X","H","H","X","X","X","X","X","H","H","X","ZL","ZI","ZB","ZR","ZY","X"],
            ["X","H","H","H","H","H","H","H","H","H","X","X","X","X","X","H","H","RF","X","X","X","X","X","X"],
            ["H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","X","X","X","X","X","X","X"],
            ["X","H","H","H","H","H","H","H","H","X","X","DH","DH","X","X","H","H","H","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","DG","H","H","X","X","X","X","X","X","H","H","H","H","H","H","H","H","H"],
            ["X","X","X","X","X","X","X","H","H","X","X","X","X","X","LH","H","H","H","H","H","H","H","H","X"],
            ["X","X","X","X","X","X","X","H","H","X","X","X","X","X","X","H","H","DI","X","X","X","X","X","X"],
            ["X","ZL","ZO","ZN","ZG","ZE","X","H","H","X","ZH","ZA","ZL","ZL","X","H","H","X","ZS","ZT","ZU","ZD","ZY","X"],
            ["X","X","X","X","X","X","X","H","H","X","X","X","X","X","X","H","H","X","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","X","H","X","X","X","X","X","X","X","X","H","X","X","X","X","X","X","X"]
        ]
        self.rooms = {"A":"Kitchen", "B":"Ballroom", "C":"Conservatory", "D":"Dining Room", "E":"Billiard Room", "F":"Library", "G":"Lounge", "H":"Hall", "I":"Study"}
        self.passages = {"Kitchen":"Study", "Conservatory":"Lounge", "Study":"Kitchen", "Lounge":"Conservatory"}
        self.room_positions = {"Kitchen":[[6, 4]], "Ballroom":[[5, 8], [5, 15], [7, 9], [7, 14]], "Conservatory":[[4, 18]], "Dining Room":[[12, 7], [15, 6]], "Billiard Room":[[9, 18], [12, 22]], "Library":[[14, 20], [16, 18]], "Lounge":[[19, 6]], "Hall":[[18, 11], [18, 12], [20, 14]], "Study":[[21, 17]]}
        self.characters = ["Miss Scarlett", "Colonel Mustard", "Mrs. White", "Reverend Green", "Mrs. Peacock", "Professor Plum"]
        self.weapons = ["Candlestick holder", "Knife", "Lead pipe", "Revolver", "Rope", "Wrench"]
        self.destinations = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"]
        self.players = []
        self.solution = []
        self.current_player = 0


    def print_board(self):
        locations = []
        p_map = {}
        for player in self.players:
            location = player.get_position()
            if type(location) == str:
                for position in self.room_positions[location]:
                    locations.append(position)
                    p_map[tuple(position)] = player.get_color()
            else:
                locations.append(location)
                p_map[tuple(location)] = player.get_color()
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if [i, j] not in locations:
                    square = self.board[i][j]

                    if list(square)[0] == "H":
                        print("#", end="")
                    elif list(square)[0] == "U":
                        print("↑", end="")
                    elif list(square)[0] == "D":
                        print("↓", end="")
                    elif list(square)[0] == "L":
                        print("←", end="")
                    elif list(square)[0] == "R":
                        print("→", end="")
                    elif list(square)[0] == "Z":
                        print(list(square)[1], end="")
                    else:
                        print(" ", end="")
                else:
                    print(p_map[tuple([i,j])], end="")
            print()

    def check_moves(self, player):
        moves = []
        location = player.get_position()

        blocked = []
        for p in self.players:
            p_location = p.get_position()
            if type(p_location) == str:
                for p_position in self.room_positions[p_location]:
                    blocked.append(p_position)
            else:
                blocked.append(p_location)

        # Convert rooms to positions
        if type(location) == str:
            if location in self.passages:
                moves.append(["Secret Passage", self.passages[location]])
            location = self.room_positions[location]
        else:
            location = [location]

        for position in location:
            # Handles movements out of rooms
            if list(self.board[position[0]][position[1]])[0] == "U" and [position[0]+1, position[1]] not in blocked:
                moves.append(["Down", [position[0]+1, position[1]]])
            elif list(self.board[position[0]][position[1]])[0] == "D" and [position[0]-1, position[1]] not in blocked:
                moves.append(["Up", [position[0]-1, position[1]]])
            elif list(self.board[position[0]][position[1]])[0] == "L" and [position[0], position[1]+1] not in blocked:
                moves.append(["Right", [position[0], position[1]+1]])
            elif list(self.board[position[0]][position[1]])[0] == "R" and [position[0], position[1]-1] not in blocked:
                moves.append(["Left", [position[0], position[1]-1]])
            else:

                # Handles Hall movements and movements into the rooms
                if position[0]-1 >= 0:
                    # Check for halls
                    if list(self.board[position[0]-1][position[1]])[0] == "H" and [position[0]-1, position[1]] not in blocked:
                        moves.append(["Up", [position[0]-1, position[1]]])

                    # Check for rooms
                    elif list(self.board[position[0]-1][position[1]])[0] == "U" and [position[0]-1, position[1]] not in blocked:
                        moves.append(["Up", self.rooms[list(self.board[position[0]-1][position[1]])[1]]])

                if position[0]+1 < len(self.board):
                    # Check for halls
                    if list(self.board[position[0]+1][position[1]])[0] == "H" and [position[0]+1, position[1]] not in blocked:
                        moves.append(["Down", [position[0]+1, position[1]]])

                    # Check for rooms
                    elif list(self.board[position[0]+1][position[1]])[0] == "D" and [position[0]+1, position[1]] not in blocked:
                        moves.append(["Down", self.rooms[list(self.board[position[0]+1][position[1]])[1]]])

                if position[1]-1 >= 0:
                    # Check for halls
                    if list(self.board[position[0]][position[1]-1])[0] == "H" and [position[0], position[1]-1] not in blocked:
                        moves.append(["Left", [position[0], position[1]-1]])

                    # Check for rooms
                    if list(self.board[position[0]][position[1]-1])[0] == "L" and [position[0], position[1]-1] not in blocked:
                        moves.append(["Left", self.rooms[list(self.board[position[0]][position[1]-1])[1]]])

                if position[1]+1 < len(self.board[0]):
                    # Check for halls
                    if list(self.board[position[0]][position[1]+1])[0] == "H" and [position[0], position[1]+1] not in blocked:
                        moves.append(["Right", [position[0], position[1]+1]])
                    
                    # Check for rooms
                    if list(self.board[position[0]][position[1]+1])[0] == "R" and [position[0], position[1]+1] not in blocked:
                        moves.append(["Right", self.rooms[list(self.board[position[0]][position[1]+1])[1]]])

        return moves
    
    def setup(self, player_count):
        # Selects characters for players
        characters = random.sample(self.characters, player_count)
        random.shuffle(characters)

        # Storing the card order to use in other functions
        temp_characters = self.characters.copy()
        temp_weapons = self.weapons.copy()
        temp_destinations = self.destinations.copy()

        # Selects solution cards and removes from the deck to be dealt
        self.solution.append(self.characters.pop(random.randint(0, len(self.characters)-1)))
        self.solution.append(self.weapons.pop(random.randint(0, len(self.weapons)-1)))
        self.solution.append(self.destinations.pop(random.randint(0, len(self.destinations)-1)))

        # Mixes cards to deal to players
        cards = self.characters + self.weapons + self.destinations
        random.shuffle(cards)

        # Splits cards for player hands
        cards = np.array_split(cards, player_count)
        cards = [card_set.tolist() for card_set in cards]
        
        # Assigns players and deals
        for i in range(player_count):
            self.players.append(Player(i+1, characters.pop(), cards[i]))

        # Add the solution cards back into the reference deck
        self.characters = temp_characters
        self.weapons = temp_weapons
        self.destinations = temp_destinations

    def next_player(self):
        self.current_player = self.current_player + 1
        if self.current_player >= len(self.players):
            self.current_player = 0

    def get_player_info(self):
        return self.players[self.current_player].get_info()
    
    def get_characters(self):
        return self.characters
    
    def get_weapons(self):
        return self.weapons
    
    def get_destinations(self):
        return self.destinations
    
    def get_players(self):
        return self.players
    
    def accuse(self, character, weapon, destination):
        if character in self.solution and weapon in self.solution and destination in self.solution:
            return True
        else:
            return False