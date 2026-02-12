class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def get_total_price(self):
        return self.quantity * self.price

class Shop:
    def __init__(self):
        self.items = []
        
#ADD ITEM    
    def add_item(self, name, quantity, price):
        for item in self.items:
            if item.name.lower() == name.lower():
                print(f"\nItem '{name}' already exists!")
                return
        self.items.append(Item(name, quantity, price))
        print(f"\n'{name}' added!")

#UPDATE QUANTITY    
    def update_quantity(self, name, new_quantity):
        for item in self.items:
            if item.name.lower() == name.lower():
                item.quantity = new_quantity
                print(f"'{name}' updated to {new_quantity}!")
                return
        print(f"\n'{name}' not found!")

#DISPLAY ITEMS    
    def display_items(self):
        if not self.items:
            print("\nEmpty inventory!")
            return
        print("\n--- INVENTORY ---")
        for item in self.items:
            print(f"{item.name}: Qty={item.quantity}, Price=${item.price:.2f}, Total=${item.get_total_price():.2f}")
        print()

#CALCULATE TOTAL INVENTORY VALUE    
    def calculate_total_inventory_value(self):
        return sum(item.get_total_price() for item in self.items)

shop = Shop()
while True:
    print("\n1. Add Item" +  
          "\n2. Update Item" + 
          "\n3. Show Inventory" 
          + "\n4. Total Inventory Value" 
          + "\n5. Exit")
    choice = input("\nEnter your choice: ")
    
    if choice == '1':
        name = input("Item: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        shop.add_item(name, qty, price)
    elif choice == '2':
        name = input("Item: ")
        qty = int(input("New quantity: "))
        shop.update_quantity(name, qty)
    elif choice == '3':
        shop.display_items()
    elif choice == '4':
        print(f"Total: ${shop.calculate_total_inventory_value():.2f}\n")
    elif choice == '5':
        break