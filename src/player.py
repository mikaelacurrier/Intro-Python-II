# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return str(self.__dict__)
    
    def move_player(self, direction):
        error = "\nThere is no room here, please try again\n"
        if direction == 'n':
            if self.current_room.n_to is not None:
                self.current_room = self.current_room.n_to
            else:
                print(error)
        elif direction == 's':
            if self.current_room.s_to is not None:
                self.current_room = self.current_room.s_to
            else:
                print(error)
        elif direction == 'e':
            if self.current_room.e_to is not None:
                self.current_room = self.current_room.e_to
            else:
                print(error)
        elif direction == 'w':
            if self.current_room.w_to is not None:
                self.current_room = self.current_room.w_to
            else:
                print(error)
        elif direction == 'i':
            if self.inventory is not None:
                drop_item()
        else:
            print("Oops, that wasn't quite right...")
    def if_player_sees_item(self):
        if self.current_room.items:
                pick_up = input (f"There's an item here ({self.current_room.items}), would you like to pick it up? (y/n)")
                current_item = self.current_room.items
                self.pick_up_item(pick_up)
                print(f"~~~~~{self.name}, you've picked up {current_item}~~~~~")
    # Pick up item if user says yes
    def pick_up_item(self, decision):
        if decision == 'y':
            # add item to player's inventory
            self.inventory.append(self.current_room.items)
            # remove item from room
            self.current_room.items = None

    # Called when player goes into Item Action
    def drop_item(self):
        drop = input("Would you like to drop any items from your inventory?(input item name to drop)")
        # removes item from player's inventory
        self.inventory.remove(drop)
        