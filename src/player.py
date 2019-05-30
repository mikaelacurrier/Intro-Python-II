# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return str(self.__dict__)
    
    def action_input(self, decision):
        error = "\nTHERE IS NO ROOM HERE. PLEASE TRY AGAIN.\n"
        if decision == 'n':
            if self.current_room.n_to is not None:
                self.current_room = self.current_room.n_to
            else:
                print(error)
        elif decision == 's':
            if self.current_room.s_to is not None:
                self.current_room = self.current_room.s_to
            else:
                print(error)
        elif decision == 'e':
            if self.current_room.e_to is not None:
                self.current_room = self.current_room.e_to
            else:
                print(error)
        elif decision == 'w':
            if self.current_room.w_to is not None:
                self.current_room = self.current_room.w_to
            else:
                print(error)
        elif decision == 'i':
            if self.inventory is not None:
                self.drop_item()
            else:
                print('Your inventory is empty')
        else:
            print("Oops, that wasn't quite right...")
    def if_player_sees_item(self):
        if self.current_room.items:
                pick_up = input (f"There's an item here ({self.current_room.items.name}), would you like to pick it up? (y/n)")
                current_item = self.current_room.items
                self.pick_up_item(pick_up)
    # Pick up item if user says yes
    def pick_up_item(self, decision):
        if decision == 'y':
            # add item to player's inventory
            self.inventory.append(self.current_room.items)
            # remove item from room
            print(f"~~~~~{self.name}, you've picked up {self.current_room.items.name}~~~~~")
            self.current_room.items = None
            for i, item in enumerate(self.inventory):
                print(f"{item.name} -- {item.description}")
                
        elif decision == 'n':
            print("moving on...")

    # Called when player goes into Item Action
    def drop_item(self):
        for i, item in enumerate(self.inventory):
            print(f"{item.name} -- {item.description}")
        drop = input("Would you like to drop any items from your inventory?(input item name to drop)")
        # if drop in self.inventory:
            # removes item from player's inventory
        for i, item in enumerate(self.inventory):
            print(f"{item.name}")
            if item.name == drop:
                del self.inventory[i]
        # else:
        #     print("You aren't carrying that item")

    def display_room(self):
        print(f'Current Room: {self.current_room.name}\n \n{self.current_room.description}\n\n')
        if len(self.inventory) > 0:
            for i, item in enumerate(self.inventory):
                print(f"Inventory: {item.name}")
        print("***********         *******************         ***********")