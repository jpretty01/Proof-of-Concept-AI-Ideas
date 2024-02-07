# Jeremy Pretty Escape Room Ideas
# Feb 2024
import random
import difflib

class EscapeRoom:
    def __init__(self):
        self.player_name = None
        self.skill_level = None
        self.room = None
        self.ai = AI()
        self.badges = {"Beginner": False, "Intermediate": False, "Expert": False}  # Badges earned by the player
        self.points = 0  # Points earned by the player
        self.play_count = 0  # Number of times the player has played the game

    def start_game(self):
        # Initialize the game
        self.player_name = input("Welcome to the Escape Room! What's your name? ")
        self.skill_level = self.choose_skill_level()  # Prompt the player to choose skill level
        print(f"Hello, {self.player_name}! Let's begin.")
        self.room = Room(self.skill_level)  # Create a new room instance with chosen skill level
        self.room.display_room_info()  # Display room information
        self.play_game()  # Start the game loop

    def choose_skill_level(self):
        # Prompt the player to choose their skill level
        while True:
            level = input("Please choose your skill level (beginner, intermediate, expert): ").lower()
            if level in ["beginner", "intermediate", "expert"]:
                return level
            else:
                print("Invalid skill level. Please choose from 'beginner', 'intermediate', or 'expert'.")

    def play_game(self):
        # Main game loop
        self.play_count += 1
        while not self.room.is_solved():  # Continue until the room is solved
            action = input("\nWhat would you like to do? ").lower()
            if action == "hint":
                self.ai.offer_hint(self.room, self.skill_level)  # Offer hint to player
            elif action == "solve":
                self.room.solve_puzzle()  # Attempt to solve the puzzle
            else:
                item = self.room.find_item(action)
                if item:
                    print(f"You found: {item}")
                    self.points += 10  # Increment points when an item is found
                    self.check_badges()  # Check if player has earned any badges
                    if self.play_count > 1:
                        self.room.adapt_difficulty(self.points)  # Adapt puzzle difficulty based on points
                else:
                    print("Sorry, I don't understand that command.")
        print("Congratulations! You've escaped the room.")

    def check_badges(self):
        # Check if the player has earned any badges based on points
        if not self.badges["Beginner"] and self.points >= 50:
            self.badges["Beginner"] = True
            print("Congratulations! You've earned the Beginner badge.")
        elif not self.badges["Intermediate"] and self.points >= 100:
            self.badges["Intermediate"] = True
            print("Congratulations! You've earned the Intermediate badge.")
        elif not self.badges["Expert"] and self.points >= 150:
            self.badges["Expert"] = True
            print("Congratulations! You've earned the Expert badge.")

class Room:
    def __init__(self, skill_level):
        self.items = self.generate_items()  # Generate random items in the room
        self.item_information = self.generate_item_information()  # Generate information for each item
        self.puzzle_solved = False
        self.skill_level = skill_level

    def generate_items(self):
        # Generate random items in the room
        items = [
            "Key under the doormat", "Locked safe", "Mysterious painting", "Strange code written on the wall",
            "Hidden message in a book", "Locked chest", "Cryptic riddle", "Broken clock", "Strange potion", "Old map"
        ]
        num_items = random.randint(4, 10)  # Choose random number of items between 4 and 10
        return random.sample(items, num_items)

    def generate_item_information(self):
        # Generate random information for each item
        random_info = [
            "The key is rusty but still fits the door.", "The safe appears to have a combination lock.",
            "The painting depicts a mysterious figure in a dark forest.",
            "The code on the wall seems to be written in a strange language.",
            "The hidden message reveals a date: 1823.",
            "The chest is adorned with intricate carvings.",
            "The riddle reads: 'What has keys but can't open locks?'",
            "The clock's hands are frozen at midnight.", "The potion emits a faint, eerie glow.",
            "The map shows a marked location deep within the forest."
        ]
        return {item: random.choice(random_info) for item in self.items}

    def display_room_info(self):
        # Display room information
        print("You are in a mysterious room. There are several items scattered around the room.")
        print("To escape, you must find the items that will help you solve the puzzle.")
        print("Items in the room:")
        for item in self.items:
            print("-", item, "-", self.item_information[item])

    def find_item(self, input_text):
        # Find the closest matching item based on player input
        closest_match = difflib.get_close_matches(input_text, self.items, n=1, cutoff=0.6)
        if closest_match:
            return closest_match[0]
        else:
            return None

    def solve_puzzle(self):
        # Placeholder for solving the puzzle
        print("You attempt to solve the puzzle...")

    def is_solved(self):
        return self.puzzle_solved

    def adapt_difficulty(self, points):
        # Adapt puzzle difficulty based on player's points
        if points >= 100:
            print("The room seems to have rearranged itself, presenting new challenges.")
        elif points >= 50:
            print("You've become quite skilled at this! Let's make things a bit more challenging.")

class AI:
    def __init__(self):
        self.beginner_hints = [
            "Try looking around the room for clues.",
            "The solution might be simpler than you think. Check the obvious places first.",
            "Remember to interact with objects in the room. They might provide valuable hints."
        ]
        self.novice_hints = [
            "You're making good progress. Keep exploring!",
            "Think logically. Sometimes the answer is right in front of you.",
            "Remember, not everything is as it seems. Keep an eye out for hidden clues."
        ]
        self.expert_hints = [
            "You're doing great! Keep challenging yourself.",
            "Try to think outside the box. The solution might not be straightforward.",
            "Don't forget to revisit previous clues. Sometimes they become relevant later."
        ]

    def offer_hint(self, room, skill_level):
        # Offer hint based on player's skill level
        if skill_level == "beginner":
            hint = random.choice(self.beginner_hints)
        elif skill_level == "intermediate":
            hint = random.choice(self.novice_hints)
        else:
            hint = random.choice(self.expert_hints)
        print("AI: Here's a hint for you -", hint)

if __name__ == "__main__":
    escape_room_game = EscapeRoom()
    escape_room_game.start_game()
