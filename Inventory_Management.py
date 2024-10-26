import time
from abc import ABC, abstractmethod  # Importing Abstract Base Class and abstractmethod decorator

# Function to display system date and time
def display_system_time():
    """
    Displays the current system date and time.
    """
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nSystem Date and Time: {current_time}")

# Abstract base class representing a general user in the system
class User(ABC):
    """
    Abstract base class for a user in the inventory system.
    Subclasses must implement additional role-based methods.
    """

    def __init__(self, username, password):
        """
        Initializes a user with a username and password.
        This is a base class for other specific user roles.
        """
        self.username = username
        self.password = password

    @abstractmethod
    def get_role(self):
        """
        Abstract method to get the role of the user.
        Must be implemented by subclasses.
        """
        pass


# Subclass representing a manager in the system
class Manager(User):
    """
    Manager class inheriting from User. Managers have full access to the system.
    """

    def __init__(self, username, password):
        """
        Initializes a manager with a username and password.
        """
        super().__init__(username, password)

    def get_role(self):
        """
        Returns the role of the user, which is 'manager' for this subclass.
        """
        return "manager"


# Subclass representing a stock clerk in the system
class StockClerk(User):
    """
    StockClerk class inheriting from User. Stock clerks have limited access to manage inventory.
    """

    def __init__(self, username, password):
        """
        Initializes a stock clerk with a username and password.
        """
        super().__init__(username, password)

    def get_role(self):
        """
        Returns the role of the user, which is 'stock_clerk' for this subclass.
        """
        return "stock_clerk"


# Subclass representing a cashier in the system
class Cashier(User):
    """
    Cashier class inheriting from User. Cashiers can view inventory and orders but cannot modify them.
    """

    def __init__(self, username, password):
        """
        Initializes a cashier with a username and password.
        """
        super().__init__(username, password)

    def get_role(self):
        """
        Returns the role of the user, which is 'cashier' for this subclass.
        """
        return "cashier"


# Class representing an item in the inventory
class InventoryItem:
    """
    Represents an inventory item with an ID, name, quantity, and price.
    """

    def __init__(self, item_id, name, quantity, price):
        """
        Initializes an inventory item with its ID, name, quantity, and price.
        """
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        """
        Returns a formatted string for displaying the item's details.
        The price is displayed with 10% GST.
        """
        return f"Item ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Price (with GST): ${self.price * 1.10:.2f}"


# Class to manage the inventory system
class Inventory:
    """
    Manages the inventory, allowing the addition, deletion, updating, and searching of items.
    """

    def __init__(self):
        """
        Initializes an empty inventory.
        The inventory is stored as a dictionary with item_id as the key.
        """
        self.items = {}

    def add_item(self, item):
        """
        Adds an item to the inventory.
        """
        self.items[item.item_id] = item
        print(f"Item '{item.name}' added to inventory.")

    def delete_item(self, item_id):
        """
        Deletes an item from the inventory based on its item ID.
        """
        if item_id in self.items:
            del self.items[item_id]
            print(f"Item with ID '{item_id}' deleted from inventory.")
        else:
            print(f"Error: Item with ID '{item_id}' not found.")

    def update_item(self, item_id, quantity, price):
        """
        Updates an item's quantity and price in the inventory.
        """
        if item_id in self.items:
            self.items[item_id].quantity = quantity
            self.items[item_id].price = price
            print(f"Item with ID '{item_id}' updated.")
        else:
            print(f"Error: Item with ID '{item_id}' not found.")

    def search_item(self, name):
        """
        Searches for an item in the inventory by name.
        """
        found_items = [item for item in self.items.values() if item.name.lower() == name.lower()]
        if found_items:
            for item in found_items:
                print(item)
        else:
            print(f"No items found with name '{name}'.")

    def low_stock_alert(self, threshold=5):
        """
        Alerts when any item in the inventory is below the stock threshold.
        """
        low_stock_items = [item for item in self.items.values() if item.quantity < threshold]
        if low_stock_items:
            print("Low stock alert for the following items:")
            for item in low_stock_items:
                print(item)
        else:
            print("All items have sufficient stock.")


# Class to manage orders in the system
class OrderManagement:
    """
    Manages orders, allowing creation, fulfillment, and displaying of orders.
    """

    def __init__(self):
        """
        Initializes an empty list of orders.
        """
        self.orders = {}

    def create_order(self, order_id, item, quantity):
        """
        Creates a new order for an item with the specified quantity.
        """
        if quantity <= item.quantity:
            item.quantity -= quantity
            self.orders[order_id] = {"item": item, "quantity": quantity, "status": "Created"}
            print(f"Order '{order_id}' created for {quantity} units of '{item.name}'.")
        else:
            print(f"Error: Not enough stock for '{item.name}'. Only {item.quantity} units available.")

    def fulfill_order(self, order_id):
        """
        Marks an order as fulfilled.
        """
        if order_id in self.orders:
            self.orders[order_id]["status"] = "Fulfilled"
            print(f"Order '{order_id}' has been fulfilled.")
        else:
            print(f"Error: Order with ID '{order_id}' not found.")

    def display_orders(self):
        """
        Displays all current orders and their statuses.
        """
        if self.orders:
            for order_id, order_info in self.orders.items():
                item = order_info["item"]
                quantity = order_info["quantity"]
                status = order_info["status"]
                print(f"Order ID: {order_id}, Item: {item.name}, Quantity: {quantity}, Status: {status}")
        else:
            print("No orders available.")


# Class representing the Inventory Management System with user interaction and menu
class InventoryManagementSystem:
    """
    The main system that handles user interactions, manages inventory and orders.
    """

    def __init__(self):
        """
        Initializes the system with predefined users and an empty inventory.
        """
        self.users = [
            Manager("manager", "manager"), # Username, Password 
            StockClerk("clerk", "clerk"),
            Cashier("cashier", "cashier")
        ]
        self.inventory = Inventory()  # Initialize the inventory system
        self.order_management = OrderManagement()  # Initialize the order management system

    def authorize(self, user, required_role):
        """
        Authorizes the user to perform specific actions based on their role.
        """
        if user.get_role() == required_role:
            return True
        else:
            print(f"Access denied: {user.get_role()}s are not authorized to perform this operation.")
            return False

    def login(self):
        """
        Handles the login process for the user.
        """
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in self.users:
            if user.username == username and user.password == password:
                print(f"Login successful! Welcome {user.username} ({user.get_role()})")
                return user
        print("Invalid username or password.")
        return None

    def run(self):
        """
        Runs the main loop of the Inventory Management System.
        """
        user = self.login()
        if not user:
            return  # Exit if login fails

        while True:
            display_system_time()  # Display the system date and time
            print("\nMenu:")
            print("1. Add Item")
            print("2. Delete Item")
            print("3. Update Item")
            print("4. Search Item")
            print("5. Low Stock Alert")
            print("6. Create Order")
            print("7. Fulfill Order")
            print("8. View Orders")
            print("9. Logout")

            choice = input("Enter your choice (1-9): ")

            if choice == '1':
                if self.authorize(user, "manager"):  # Only managers can add items
                    item_id = input("Enter item ID: ")
                    name = input("Enter item name: ")
                    quantity = int(input("Enter item quantity: "))
                    price = float(input("Enter item price (before GST): "))
                    item = InventoryItem(item_id, name, quantity, price)
                    self.inventory.add_item(item)

            elif choice == '2':
                if self.authorize(user, "manager"):  # Only managers can delete items
                    item_id = input("Enter item ID: ")
                    self.inventory.delete_item(item_id)

            elif choice == '3':
                if self.authorize(user, "manager"):  # Only managers can update items
                    item_id = input("Enter item ID: ")
                    quantity = int(input("Enter new quantity: "))
                    price = float(input("Enter new price (before GST): "))
                    self.inventory.update_item(item_id, quantity, price)

            elif choice == '4':
                name = input("Enter item name to search: ")
                self.inventory.search_item(name)

            elif choice == '5':
                self.inventory.low_stock_alert()  # Check for low stock items

            elif choice == '6':
                if self.authorize(user, "manager"):  # Only managers can create orders
                    order_id = input("Enter order ID: ")
                    item_id = input("Enter item ID to order: ")
                    if item_id in self.inventory.items:
                        quantity = int(input("Enter quantity to order: "))
                        self.order_management.create_order(order_id, self.inventory.items[item_id], quantity)
                    else:
                        print(f"Error: Item with ID {item_id} not found.")

            elif choice == '7':
                order_id = input("Enter order ID to fulfill: ")
                self.order_management.fulfill_order(order_id)

            elif choice == '8':
                self.order_management.display_orders()

            elif choice == '9':
                print("Logging out!")
                break  # Exit the loop to log out

            else:
                print("Invalid choice. Please try again.")


# Run the system
if __name__ == "__main__":
    system = InventoryManagementSystem()
    system.run()
