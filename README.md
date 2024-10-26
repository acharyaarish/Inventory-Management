# Inventory Management System 🛒

This Python-based Inventory Management System is designed for retail environments to help manage users, inventory, and orders. Users are assigned different roles with varying permissions: **Manager**, **Stock Clerk**, and **Cashier**. The system provides options for inventory control, order management, and user role-based access control.

---

## 📋 Table of Contents

- [Features](#features)
- [System Overview](#system-overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Login](#login)
  - [User Roles and Permissions](#user-roles-and-permissions)
  - [Menu Options](#menu-options)
- [Code Structure](#code-structure)
- [License](#license)

---

## ✨ Features

- **Role-Based Access**: Different user roles have distinct permissions to access and modify the inventory and order systems.
- **Inventory Management**: Add, delete, update, and search items. Alerts on low stock levels.
- **Order Management**: Create and fulfill orders based on available stock.
- **Real-Time System Date and Time Display**.

---

## 📊 System Overview

1. **User Roles**:
   - **Manager**: Full control over inventory and order creation.
   - **Stock Clerk**: Limited inventory management access.
   - **Cashier**: View-only access to inventory and orders.

2. **Inventory Operations**:
   - **Add** or **delete** items.
   - **Update** quantity and price of items.
   - **Search** for items by name.
   - **Low Stock Alert**: Detects items below a specified stock threshold.

3. **Order Operations**:
   - **Create** orders if stock is available.
   - **Fulfill** orders and mark them as completed.
   - **View** all existing orders.

---

## 🛠 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/Inventory-Management.git
   cd Inventory-Management
   ```

2. **Install Python 3.6 or Higher**: Ensure you have Python installed. You can download it from [Python's official site](https://www.python.org/downloads/).

3. **Run the System**:
   ```bash
   python Inventory_Management.py
   ```

---

## 🚀 Usage

### Login

Start the system and **log in** with one of the following credentials:

- **Manager**: `Username: manager`, `Password: manager`
- **Stock Clerk**: `Username: clerk`, `Password: clerk`
- **Cashier**: `Username: cashier`, `Password: cashier`

### User Roles and Permissions

| Role         | Add Item | Delete Item | Update Item | View Inventory | Create Order | Fulfill Order |
|--------------|----------|-------------|-------------|----------------|--------------|---------------|
| **Manager**  | ✔        | ✔           | ✔           | ✔              | ✔            | ✔             |
| **Stock Clerk** | ✘        | ✘           | ✘           | ✔              | ✘            | ✘             |
| **Cashier**  | ✘        | ✘           | ✘           | ✔              | ✘            | ✘             |

### Menu Options

Once logged in, you can choose from these options:

1. **Add Item**: (Managers only) Add a new item to the inventory.
2. **Delete Item**: (Managers only) Delete an item from the inventory.
3. **Update Item**: (Managers only) Modify item quantity or price.
4. **Search Item**: Find an item by name.
5. **Low Stock Alert**: View items below a stock threshold.
6. **Create Order**: (Managers only) Generate an order based on stock.
7. **Fulfill Order**: Complete an existing order.
8. **View Orders**: See all orders and their statuses.
9. **Logout**: Exit the system.

Example of a typical interaction:
```bash
Enter username: manager
Enter password: manager
Login successful! Welcome manager (manager)

Menu:
1. Add Item
2. Delete Item
...
Enter your choice (1-9): 1
```

---

## 🧩 Code Structure

- **Classes**:
  - `User` (Abstract Base Class) and its subclasses (`Manager`, `StockClerk`, `Cashier`): Handle user role differentiation and permissions.
  - `InventoryItem`: Defines the attributes of each item.
  - `Inventory`: Manages the item addition, deletion, and search functionalities.
  - `OrderManagement`: Manages order creation and fulfillment.
  - `InventoryManagementSystem`: The main interface for user interaction.

- **Functions**:
  - `display_system_time`: Displays the current system date and time.
  - `authorize`: Checks if a user has the necessary role for an operation.
  - `login`: Handles user authentication.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
