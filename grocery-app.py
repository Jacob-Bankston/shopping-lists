import decimal

shopping_lists = []

class ShoppingList:
    def __init__(self, title, address):
        self.title = title
        self.address = address
        self.grocery_list = []

    def displayList(self):
        grocery_list_formatting = ""
        complete_total_cost = 0
        if len(self.grocery_list) == 0:
            print(f"{self.title} - {self.address} - ${complete_total_cost}\n")
        else:
            for index in range(0, (len(self.grocery_list) -1)):
                grocery_list_formatting += self.grocery_list[index].title + ", "
            for index in range(0, (len(self.grocery_list))):
                complete_total_cost += self.grocery_list[index].price * self.grocery_list[index].quantity
            grocery_list_formatting += self.grocery_list[-1].title
            total_cost = round(complete_total_cost, 2)
            print(f"{self.title} - {self.address} - ${total_cost}\n{grocery_list_formatting}")

    def addGroceryItem(self):
        user_groceryitem_title = input("Please enter the name of the grocery item: ")
        while True:
            user_price = input("Please enter the price of the grocery item: $")
            try:
                user_groceryitem_price = decimal.Decimal(user_price)
                break
            except:
                print("Please enter an accurate price!")
        while True:
            user_quantity = input("Please enter the quantity of the grocery item: ")
            try:
                user_groceryitem_quantity = decimal.Decimal(user_quantity)
                break
            except:
                print("Please enter an accurate quantity!")
        grocery_item = GroceryItem(user_groceryitem_title, user_groceryitem_price, user_groceryitem_quantity)
        self.grocery_list.append(grocery_item)
        

class GroceryItem:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

def ask_for_user_shopping_list():
    user_shopping_list_title = input("Please enter the name of the store you would like to start a shopping list for: ")
    user_shopping_list_address = input("Please enter the address for the store location: ")
    shopping_list = ShoppingList(user_shopping_list_title, user_shopping_list_address)
    shopping_lists.append(shopping_list)

def add_grocery_items():
    while True:
        for index in range(0, len(shopping_lists)):
            print(f"{index + 1} - {shopping_lists[index].title}")
        sl_index = input("Please enter the number of the list you would like to add a grocery item to: ")
        try: 
            shopping_lists[int(sl_index) - 1].addGroceryItem()
            break
        except ValueError:
            print("Please enter a number on the list!")
        except IndexError:
            print("Please enter a number on the list!")


def del_shopping_lists():
    for index in range(0, len(shopping_lists)):
        print(f"{index + 1} - {shopping_lists[index].title}")
    while True:
        try:
            sl_index = input("Please enter the number of the shopping list you would like to delete: ")
            del shopping_lists[int(sl_index) - 1]
            break
        except ValueError:
            print("Please enter a number on the list!")
        except IndexError:
            print("Please enter a number on the list!")

def del_grocery_item():
    for index in range(0, len(shopping_lists)):
        print(f"\nOption {index + 1}")
        shopping_lists[index].displayList()
    while True:
        try:
            sl_index = input("Please enter the number of the shopping list you would like to remove a grocery item from: ")
            chosen_store = shopping_lists[int(sl_index) - 1]
            break
        except ValueError:
            print("Please enter a number on the list!")
        except IndexError:
            print("Please enter a number on the list!")
    if len(chosen_store.grocery_list) == 0:
        print("There are no items to remove from this shopping list!")
    else:
        for index in range(0, len(chosen_store.grocery_list)):
            print(f"{index + 1} - {chosen_store.grocery_list[index].title}")
        while True:
            try:
                gi_index = input("Please enter the number of the grocery item you would like to remove: ")
                del chosen_store.grocery_list[int(gi_index) -1]
                break
            except ValueError:
                print("Please enter a number on the list!")
            except IndexError:
                print("Please enter a number on the list!")

user_input = ""

welcome = print("WELCOME THE THE SHOPPING LIST APPLICATION!")

while user_input != "q":
    if len(shopping_lists) == 0:
        print("Please add a Shopping List to begin!")
        ask_for_user_shopping_list()
    else:
        print("Press 1 to add a new store's shopping list\nPress 2 to add a grocery item to a shopping list\nPress 3 to display your shopping lists\n"
            "Press 4 to delete a grocery item from a shopping list\nPress 5 to delete a store's shopping list\nPress 'q' to quit the application\n")
        user_input = input("Please enter the selection here: ")
        if user_input == "q":
            break
        try:
            if int(user_input) < 0 or int(user_input) > 5:
                print("Please enter a correct input!")
        except ValueError:
            print("Please select an option from the list")
        if user_input == "1":
            ask_for_user_shopping_list()
            print("New Shopping List Added!")
        if user_input == "2":
            add_grocery_items()
            print("New Grocery Item Added!")
        if user_input == "3":
            for lists in shopping_lists:
                lists.displayList()
        if user_input == "4":
            del_grocery_item()
            print("Grocery Item Removed!")
        if user_input == "5":
            del_shopping_lists()
            print("Shopping List Removed!")
        user_input = input("Press any key to continue, press 'q' to quit.\n")

