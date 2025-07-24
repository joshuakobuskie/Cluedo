from JoshuaKobuskie_Player import Player

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

    def remove_suggestion(self, disprover, card):
        # If disprover is the same player, then the card must be in the solution or AI hand
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


test = AI_Player(2, "Miss Scarlett", ['Mrs. Peacock', 'Candlestick Holder', 'Wrench', 'Kitchen', 'Colonel Mustard', 'Rope', 'Lead Pipe', 'Dining Room', 'Hall'], 3)
print(test.possible_characters)
print(test.possible_rooms)
print(test.possible_weapons)
test.remove_suggestion(1, "Knife")
print(test.possible_weapons)