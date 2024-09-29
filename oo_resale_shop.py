from typing import Dict, Optional
from computer import *

class ResaleShop: 
    #storing information about resale shop
    #What attributes will it need?
    itemID: int = 0
    inventory : list[computer]

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self, inventory: list):
        self.inventory = inventory
        self.itemID = len(inventory)

    # What methods will you need?
    """
    Takes in a Dict containing all the information about a computer,
    adds it to the inventory, returns the assigned item_id
    """   
    def buy(self, computer: computer):
        self.itemID += 1 # increment itemID
        self.inventory.append(computer)
        return self.itemID
    
    """
    Takes in an item_id and a new price, updates the price of the associated
    computer if it is the inventory, prints error message otherwise
    """
    
    def update_price(self, item_id: int, new_price: int):
     if item_id < self.itemID:
        self.inventory[item_id].price = new_price
        print("Computer is now $", new_price)
     else:
        print("Item", item_id, "not found. Cannot update price.")
    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    
    def sell(self, item_id: int):
        if item_id < self.itemID:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
         print("Item", item_id, "not found. Please select another item to sell.")
    """
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
        
    def print_inventory(self):
    # If the inventory is not empty
     if self.inventory:
        # For each item
        for i in range(len(self.inventory)):
            # Print its details
            print(f'Item ID: {i} : {self.inventory[i].description}')
     else:
        print("No inventory to display.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id < self.itemID:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")






def main():
   inventory: list[computer] = []
   resale_shop = ResaleShop(inventory)
#    resale_shop.buy("Mac Pro (Late 2013)",
#         "3.5 GHc 6-Core Intel Xeon E5",
#         1024, 64,
#         "macOS Big Sur", 2013, 1500)
#    resale_shop.print_inventory()

   my_computer = computer("Mac Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "macOS Big Sur", 2013, 1500)
   resale_shop.buy(my_computer)
#    resale_shop.print_inventory()

   bebe_computer = computer("Mac Air",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2023, 1500)
   resale_shop.buy(bebe_computer)
   resale_shop.print_inventory()

#    resale_shop.sell(1)
#    resale_shop.print_inventory()

   resale_shop.update_price(1, 1000)
   resale_shop.print_inventory()

   resale_shop.refurbish(1, "Microsoft Windows 10")
   resale_shop.print_inventory()

   resale_shop.sell(1)

   

   
main()

