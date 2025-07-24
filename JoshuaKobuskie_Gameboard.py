import random
import numpy as np
from JoshuaKobuskie_Player import Player
import time
import os
from JoshuaKobuskie_AI_Player import AI_Player

class CluedoBoard:
    def __init__(self):
        self.board = [
            ["ZX","X","X","X","X","X","X","X","X","H","X","X","X","X","H","X","X","X","X","X","X","X","X","ZO"],
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
            ["X","ZD","ZI","ZN","ZE","ZR","ZM","X","H","H","X","X","ZC","X","X","H","H","H","X","ZB","ZL","ZR","ZD","X"],
            ["X","X","X","X","X","X","X","LD","H","H","X","X","ZL","X","X","H","H","H","X","X","X","X","UE","X"],
            ["X","X","X","X","X","X","X","X","H","H","X","X","ZU","X","X","H","H","H","H","H","H","H","H","X"],
            ["X","X","X","X","X","X","X","X","H","H","X","X","ZE","X","X","H","H","H","X","X","DF","X","X","X"],
            ["X","X","X","X","X","X","UD","X","H","H","X","X","X","X","X","H","H","X","ZL","ZI","ZB","ZR","ZY","X"],
            ["X","H","H","H","H","H","H","H","H","H","X","X","X","X","X","H","H","RF","X","X","X","X","X","X"],
            ["H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","X","X","X","X","X","X","X"],
            ["X","H","H","H","H","H","H","H","H","X","X","DH","DH","X","X","H","H","H","X","X","X","X","X","X"],
            ["X","X","X","X","X","X","DG","H","H","X","X","X","X","X","X","H","H","H","H","H","H","H","H","H"],
            ["X","X","X","X","X","X","X","H","H","X","X","X","X","X","LH","H","H","H","H","H","H","H","H","X"],
            ["X","X","X","X","X","X","X","H","H","X","X","X","X","X","X","H","H","DI","X","X","X","X","X","X"],
            ["X","ZL","ZO","ZN","ZG","ZE","X","H","H","X","ZH","ZA","ZL","ZL","X","H","H","X","ZS","ZT","ZU","ZD","ZY","X"],
            ["X","X","X","X","X","X","X","H","H","X","X","X","X","X","X","H","H","X","X","X","X","X","X","X"],
            ["ZO","X","X","X","X","X","X","H","X","X","X","X","X","X","X","X","H","X","X","X","X","X","X","ZX"]
        ]
        self.rooms = {"A":"Kitchen", "B":"Ballroom", "C":"Conservatory", "D":"Dining Room", "E":"Billiard Room", "F":"Library", "G":"Lounge", "H":"Hall", "I":"Study"}
        self.passages = {"Kitchen":"Study", "Conservatory":"Lounge", "Study":"Kitchen", "Lounge":"Conservatory"}
        self.room_positions = {"Kitchen":[[6, 4]], "Ballroom":[[5, 8], [5, 15], [7, 9], [7, 14]], "Conservatory":[[4, 18]], "Dining Room":[[12, 7], [15, 6]], "Billiard Room":[[9, 18], [12, 22]], "Library":[[14, 20], [16, 18]], "Lounge":[[19, 6]], "Hall":[[18, 11], [18, 12], [20, 14]], "Study":[[21, 17]]}
        self.characters = ["Miss Scarlett", "Colonel Mustard", "Mrs. White", "Reverend Green", "Mrs. Peacock", "Professor Plum"]
        self.weapons = ["Candlestick Holder", "Knife", "Lead Pipe", "Revolver", "Rope", "Wrench"]
        self.destinations = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"]
        self.players = []
        self.solution = []
        self.current_player = 0
        self.play = True

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

            # Only block tiles, not rooms
            if type(p_location) != str:
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
        for i in range(player_count-1):
            self.players.append(Player(i+1, characters.pop(), cards[i]))

        # Add AI player
        self.players.append(AI_Player(player_count, characters.pop(), cards[player_count-1]))

        # Add the solution cards back into the reference deck
        self.characters = temp_characters
        self.weapons = temp_weapons
        self.destinations = temp_destinations
    
    def get_characters(self):
        return self.characters
    
    def get_weapons(self):
        return self.weapons
    
    def get_destinations(self):
        return self.destinations
    
    def get_players(self):
        return self.players
    
    def get_play(self):
        return self.play
    
    def next_player(self):
        self.current_player = self.current_player + 1
        self.current_player = self.current_player % len(self.players)

    def get_current_player(self):
        return self.players[self.current_player]
    
    def accuse(self, character, weapon, destination):

        # Check to see if all players have made an accusation and the game is over
        game_status = [p.get_accusation() for p in self.players]
        if not True in game_status:
            self.play = False
        
        # Check accusation validity
        if character in self.solution and weapon in self.solution and destination in self.solution:
            return True
        else:
            return False
        
    def disprove(self, suggestor_number, character_selection, destination_selection, weapon_selection):
        cur = self.current_player

        for i in range(len(self.players) - 1):
            cur += 1
            cur = cur % len(self.players)

            hand = self.players[cur].get_cards()
            if character_selection in hand or destination_selection in hand or weapon_selection in hand:
                player_number = self.players[cur].get_player_number()
                print("Player {} has a card that could disprove your suggestion! Please pass the device to Player {}.".format(player_number, player_number))
                time.sleep(10)
                os.system("cls" if os.name == "nt" else "clear")
                print("Player {} has suggested that it was {} in the {} with the {}.".format(suggestor_number, character_selection, destination_selection, weapon_selection))
                print("Please select a card to show to Player {} to disprove this suggestion:".format(suggestor_number))
                
                options = []
                for card in hand:
                    if card == character_selection or card == destination_selection or card == weapon_selection:
                        options.append(card)

                for i in range(len(options)):
                    print("Option {}: {}".format(i+1, options[i]))

                card_selection = ""
                while type(card_selection) != int:
                    try:
                        card_selection = input("Please enter an option number to reveal a card: ")
                        card_selection = int(card_selection)
                        if card_selection < 1 or card_selection > len(options):
                            print("Invalid selection: Please enter a value between 1 and {}".format(len(options)))
                            card_selection = ""
                        else:
                            card_selection -= 1
                    except ValueError:
                        print("Invalid selection: Please enter a value between 1 and {}".format(len(options)))
            
                os.system("cls" if os.name == "nt" else "clear")
                print("You will show the {} card to disprove Player {}'s suggestion. Please pass the device to Player {}.".format(options[card_selection], suggestor_number, suggestor_number))
                time.sleep(5)
                os.system("cls" if os.name == "nt" else "clear")
                return [True, self.players[cur].get_player_number(), options[card_selection]]
        
        return [False]