from JoshuaKobuskie_Player import Player
import os
import random
import time

class AI_Player(Player):
    def __init__(self, player_number, character, cards, player_count):

        # Create player
        super().__init__(player_number, character, cards)

        self.player_count = player_count

        self.accuse_character = None
        self.accuse_weapon = None
        self.accuse_room = None
        
        # Create knowledge base
        # Clue solution is player 0
        self.possible_characters = {"Miss Scarlett":[i for i in range(self.player_count+1)], "Colonel Mustard":[i for i in range(self.player_count+1)], "Mrs. White":[i for i in range(self.player_count+1)], "Reverend Green":[i for i in range(self.player_count+1)], "Mrs. Peacock":[i for i in range(self.player_count+1)], "Professor Plum":[i for i in range(self.player_count+1)]}
        self.possible_weapons = {"Candlestick Holder":[i for i in range(self.player_count+1)], "Knife":[i for i in range(self.player_count+1)], "Lead Pipe":[i for i in range(self.player_count+1)], "Revolver":[i for i in range(self.player_count+1)], "Rope":[i for i in range(self.player_count+1)], "Wrench":[i for i in range(self.player_count+1)]}
        self.possible_rooms = {"Kitchen":[i for i in range(self.player_count+1)], "Ballroom":[i for i in range(self.player_count+1)], "Conservatory":[i for i in range(self.player_count+1)], "Dining Room":[i for i in range(self.player_count+1)], "Billiard Room":[i for i in range(self.player_count+1)], "Library":[i for i in range(self.player_count+1)], "Lounge":[i for i in range(self.player_count+1)], "Hall":[i for i in range(self.player_count+1)], "Study":[i for i in range(self.player_count+1)]}

        # Remove already known cards from the AI knowledge base
        for card in self.cards:
            if card in self.possible_characters:
                self.possible_characters[card] = [self.player_number]
            elif card in self.possible_weapons:
                self.possible_weapons[card] = [self.player_number]
            elif card in self.possible_rooms:
                self.possible_rooms[card] = [self.player_number]

        # Remove cards AI knows that it doesnt have
        for character, candidates in self.possible_characters.items():
            if candidates != [self.player_number]:
                self.possible_characters[character].remove(self.player_number)

        for weapon, candidates in self.possible_weapons.items():
            if candidates != [self.player_number]:
                self.possible_weapons[weapon].remove(self.player_number)

        for room, candidates in self.possible_rooms.items():
            if candidates != [self.player_number]:
                self.possible_rooms[room].remove(self.player_number)

        self.check_solution()

    def remove_suggestion(self, disprover, card, other_1, other_2):
        # If disprover is the same player, then the card must be in the solution or AI hand

        current_player = self.player_number + 1
        current_player = current_player % (self.player_count+1)

        # Remove people who could not disprove and therefore dont have one of the other cards asked for
        while current_player < disprover:

            if current_player != 0:
                # Update characters
                if other_1 in self.possible_characters and current_player in self.possible_characters[other_1]:
                    self.possible_characters[other_1].remove(current_player)
                if other_2 in self.possible_characters and current_player in self.possible_characters[other_2]:
                    self.possible_characters[other_2].remove(current_player)

                # Update weapons
                if other_1 in self.possible_weapons and current_player in self.possible_weapons[other_1]:
                    self.possible_weapons[other_1].remove(current_player)
                if other_2 in self.possible_weapons and current_player in self.possible_weapons[other_2]:
                    self.possible_weapons[other_2].remove(current_player)

                # Update rooms
                if other_1 in self.possible_rooms and current_player in self.possible_rooms[other_1]:
                    self.possible_rooms[other_1].remove(current_player)
                if other_2 in self.possible_rooms and current_player in self.possible_rooms[other_2]:
                    self.possible_rooms[other_2].remove(current_player)
            
            current_player += 1
            current_player = current_player % (self.player_count+1)
            

        # Update the known card holder
        if card in self.possible_characters:
            self.possible_characters[card] = [disprover]
        elif card in self.possible_weapons:
            self.possible_weapons[card] = [disprover]
        elif card in self.possible_rooms:
            self.possible_rooms[card] = [disprover]
            
        self.check_solution()

    def check_player_card_count():
        # This should implement the logic to reduce the selection size
        # If the maximum number of player cards has been reached for a player, they cant have any more cards here so they can be eliminated from the other options
        return 0

    def infer_suggestion(self, suggestor, disprover, card):
        # This is going to be considered if two other players make a suggestion and disprove it without involving the AI
        self.check_solution()
        return 0

    def check_solution(self):
        for card, candidates in self.possible_characters.items():
            if candidates == [0]:
                self.accuse_character = card
        
        for card, candidates in self.possible_weapons.items():
            if candidates == [0]:
                self.accuse_weapon = card
        
        for card, candidates in self.possible_rooms.items():
            if candidates == [0]:
                self.accuse_room = card

        # If we are confident on the solution, make the final accusation
        if self.accuse_character and self.accuse_weapon and self.accuse_room:
            print("ACCUSATION LOGIC HERE")

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
            print("The AI has already made an incorrect accusation! It has has lost the game!")
        else:
            print("The AI has rolled a {}".format(self.moves))
            print("Steps remaining: {}".format(self.moves))
            print("Current position: {}".format(self.position))

        # Handle getting pulled to a new room
        possible_moves = []
        if self.position != self.prior_position:
            possible_moves.append(["Stay", self.position])
        
        while self.moves > 0:

            # Determine open squares
            possible_moves.extend(board.check_moves(self))

            # Determine the best room to visit in order to pick the next movement
            # Only search rooms where the solution may be
            candidate_rooms = [room for room, candidates in self.possible_rooms.items() if 0 in candidates]
                
            # Select closest room from candidates
            best_room = None
            best_distance = float("inf")
            for room in candidate_rooms:
                distance = self.distance_to_room(self.position, board, room)
                if distance < best_distance:
                    best_distance = distance
                    best_room = room

            # The best room with the shortest distance has been found and the move to get there now can be selected
            best_distance = float("inf")
            for i in range(len(possible_moves)):
                distance = self.distance_to_room(possible_moves[i][1], board, best_room)
                if distance < best_distance:
                    best_distance = distance
                    selection = i
            
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
            possible_moves = []
        
        # CHANGE AFTER HERE AS WELL

        # Make a suggestion after entering a room
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
                self.revealed.append(disprove[2])
            else:
                print("No one was able to disprove your suggestion!")

            self.prior_position = self.position
        elif type(self.position) == str and self.position == self.prior_position:
            print("You have reentered the {} and cannot make another suggestion in this room until you visit another room.".format(self.position))

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
        super().get_info()
        print("Player {} is an AI".format(self.player_number))

    def distance_to_room(position, board, room):
        min_distance = float("inf")
        doors = board.get_doors()
        target_doors = doors[room]
        
        if type(position) == str:
            # If in a room, use its doors as starting points
            current_doors = doors[position]
            for current_door in current_doors:
                for target_door in target_doors:
                    distance = abs(current_door[0]-target_door[0]) + abs(current_door[1]-target_door[1])
                    min_distance = min(min_distance, distance)
        else:
            # In hallway
            for target_door in target_doors:
                distance = abs(position[0]-target_door[0]) + abs(position[1]-target_door[1])
                min_distance = min(min_distance, distance)
                
        return min_distance

test = AI_Player(3, "Miss Scarlett", ['Mrs. Peacock', 'Candlestick Holder', 'Wrench', 'Kitchen', 'Colonel Mustard', 'Rope', 'Lead Pipe', 'Dining Room', 'Hall'], 3)
print(test.possible_characters)
print(test.possible_rooms)
print(test.possible_weapons)
test.remove_suggestion(2, "Knife", "Mrs. White", "Ballroom")
print()
print(test.possible_characters)
print(test.possible_rooms)
print(test.possible_weapons)