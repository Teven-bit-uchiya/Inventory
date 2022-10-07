from tabulate import tabulate
import csv


# Create a class.

# Create a init method
class Shoes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return int(self.quantity)

    def set_quantity(self, new_quantity):
        self.quantity = str(new_quantity + int(self.quantity))
        # Print out the result.

    def __repr__(self):
        return f"Country: {self.country}\n" \
               f"Code: {self.code}\n" \
               f"Product: {self.product}\n" \
               f"Cost: {self.cost}\n" \
               f"Quantity: {self.quantity}\n\n"


shoe_list = []


# Open the file and read it.
# Check for the header.

# Read each line in the file.
def read_shoe_data():
    # Strip the line.
    try:
        # Store the file in the object.
        with open("inventory.txt", "r") as fh:
            # Append the object in a list.
            check_fh = fh.readlines()[1:]
            # If the file does not exist.
            for f in check_fh:
                fx = f.strip("\n").split(",")
                shoes_fh = Shoes(fx[0], fx[1], fx[2], fx[3], fx[4])
                shoe_list.append(shoes_fh)
    except FileNotFoundError:
        print("Sorry the file does not exist.Please try again.")


# Recalling function.
# Ask user to enter in the information they want to store.
read_shoe_data()


# Ask user to enter in information.


def capture_shoes():
    # Create a object and store it in a list.
    country_choice = input("From which country is the shoe from?\n").capitalize()
    code_choice = input("Enter the code of the shoe here:\n").upper()
    product_choice = input("What is the make of the Nike shoe?\n").capitalize()
    cost_choice = int(input("How much does the shoe cost?\n"))
    quantity_choice = input("How many shoes do you want?\n")

    # Create a object.
    shoe_choices = Shoes(country_choice, code_choice, product_choice, cost_choice, quantity_choice)
    # Append the object in a list.
    shoe_list.append(shoe_choices)
    with open("inventory.txt", "a+") as f:
        f.write(f"\n{country_choice},{code_choice},{product_choice},{cost_choice},{quantity_choice}")
    
    
    # Print out the list.


def view_all():
    reader = csv.reader(open("inventory.txt", "r"))
    inventory = []
    for row in reader:
        inventory.append(row)

    header = inventory.pop(0)

    def fixed_lenght(text, length):
        if len(text) > length:
            text = text[:length]
        elif len(text) < length:
            text = (text + " " * length)[:length]
        return text

    print("#" * 126)
    print("# ", end=" ")
    for column in header:
        print(fixed_lenght(column, 20), end="  #  ")
    print()
    print("#" * 126)

    for row in inventory:
        print("# ", end=" ")
        for column in row:
            print(fixed_lenght(column, 20), end="  #  ")
        print()
    print("#" * 126)


# Restock


def re_stock():
    lowest_shoe = shoe_list[0]
    for shoe in shoe_list:
        if shoe.get_quantity() <= lowest_shoe.get_quantity():
            lowest_shoe = shoe
        #  Assign the lowest quantity to the shoe.
    print(lowest_shoe)
    # Ask user to enter in the quantity.
    new_quantity = int(input("Quantity of new Stock:\n"))
    # Add to the current quantity.
    lowest_shoe.set_quantity(new_quantity)
    # Print out the result.
    print(lowest_shoe)
    with open("inventory.txt", "w+") as f:
        f.write("Country,Code,Product,Cost,Quantity")
        for shoe in shoe_list:
            f.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
    # print(shoe_list[6].product)

    # print(shoe_list)
    # Print out the result.
    # Search through the list and print out the result.


def search_shoe(code):
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            # Create a empty list to store cost of items.
            break


# Print out the value of each item.
def value_per_item():
    values_items = []
    # Print out the list.
    for v in shoe_list:
        cost_of_item = v.cost
        item_quantity = v.quantity
        va = int(cost_of_item) * int(item_quantity)
        values_items.append(f"The value of {v.product} is R {va}")

    for val in values_items:
        print(val)  # Print out the value of the items.

    # Create a dictionary and store the information in there.


def highest_quantity():
    most_shoes = {}
    for most in shoe_list:
        shoe_make = most.product

        # Print out the result.
        quantity_shoes = most.quantity
        most_shoes[int(quantity_shoes)] = shoe_make
        most_valued = max(most_shoes.keys())
    print(f"The shoes that is on sale is: {most_shoes[most_valued]}")


# Use while loop to print the menu over and over again and ask user to enter input.
while True:
    shoe_menu = input('''Welcome to our shoe shop! Please select one of the following options:
    Capture Shoes - cs
    View Shoe - va
    Restock - r
    Search Shoe - ss
    Item Value - iv
    Sale - s
    Exit - e
    :\n''').lower()

    # Use if statements to help with the decision making of the user. Each menu will call different function.
    # To Exit the program the user enter e
    if shoe_menu == "cs":
        capture_shoes()
    elif shoe_menu == "va":
        view_all()
    elif shoe_menu == "r":
        re_stock()
    elif shoe_menu == "ss":
        # Ask user to the code and print the result.
        shoe_code = input("Enter the code of the shoe that you are looking for here:\n").upper()
        search_shoe(shoe_code)
    elif shoe_menu == "iv":
        value_per_item()
    elif shoe_menu == "s":
        highest_quantity()
    elif shoe_menu == "e":
        print("Thank you for visiting our shoe shop! Enjoy your day.")
        # To exit the program.
        exit()
