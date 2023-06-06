class GameObject:    
    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    def look(self):
        return f"You examine the {self.name}. {self.appearance}\n"

    def touch(self):
        return f"You grab the {self.name}. {self.feel}"

    def sniff(self):
        return f"You smelled the {self.name}. {self.smell}"
    
class Room:
    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    def check_code(self, code):
        return self.escape_code == code
    
    def get_game_object_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names
        
class Game:
    def __init__ (self):
        self.attempts = 0
        objects = self.create_objects
        self.room = Room(731, objects)

    def create_objects(self):
        return [
            GameObject(
                "Sweater",
                "It's a blue sweater that had the number 12 switched on it.",
                "Someone has unstitched the second number, leaving only the 1.",
                "The sweater smells of laundry detergent."),
            GameObject(
                "Chair", 
                "It's a wooden chair with only 3 legs.",
                "Someone had deliberately snapped off one of the legs.",
                "It smells like old wood."),
            GameObject(
                "Journal",
                "The final entry states that time should be hours then minutes then seconds (H-M-S).",
                "The cover is worn and several pages are missing.",
                "It smells like musty leather."),
            GameObject(
                "Bowl of soup", 
                "It appears to be tomato soup.",
                "It has cooled down to room temperature.",
                "You detect 7 different herbs and spices."),
            GameObject(
                "Clock", 
                "The hour hand is pointing towards the soup, the minute hand towards the chair, and the second hand towards the sweater.",
                "The battery compartment is open and empty.",
                "It smells of plastic."),
        ]
    
    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = int(input(prompt))
        self.select_object(selection - 1)
        if selection >= 1 and selection <= 5:
            self.select_object(selection - 1)
            self.take_turn()
        else:
            is_code_correct = self.guess_code(selection)
            if is_code_correct:
                print("Congratulations, you've escaped The Room")
            else:
                if self.attempts == 3:
                    print("You've run out of guesses. You are trapped in the room for the rest of eternity. Destined never to leave.")
                else:
                    print(f"You've used {self.attempts} out of 3.")
                    self.take_turn()

    
    def get_room_prompt(self):
        prompt = "Enter the 3-Digit Passcode, or Choose an Item to interact with:\n"
        names = self.room_get_objects_names()
        index = 1
        for name in names:
            prompt += f"{index}. {name}\n"
            index += 1
        return prompt
    
    def select_object(self, index):
        selected_object = self.room.game_objects[index]
        prompt = self.get.object_interaction_string(selected_object.name)
        interaction = input(prompt)
        clue = self.interact_sith_object(selected_object, interaction)
        print(clue)
        return

    def get_object_interaction_string(self, name):
        return f"What would you like to do witht he {name}?\n1. Look at it\n2. Touch it\n3. Smell it\n"

    def interact_with_object(self, object, interaction):
        if interaction == "1":
            return object.look()
        elif interaction == "2":
            return object.feel()
        else:
            return object.smell()
        
    def guess_code(self, code):
        if self.room.check_code(code):
            return True
        else:
            self.attempts += 1
            return False
    
game = Game()
game.take_turn()