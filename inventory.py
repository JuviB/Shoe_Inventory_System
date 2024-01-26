#========The beginning of the class==========
# Create the shoe class
class Shoe:

    # Create the constructor method with country, code, product, cost, quantity as parameters
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    
    # Create the get_cost method to retreive the cost of the shoe item
    def get_cost(self):
        return self.cost

    # Create the get_quantity method to retreive the quantity 
    def get_quantity(self):
        return self.quantity

    # Create a method that returns a string representation of a class
    def __str__(self):
        return f'''
    Country: {self.country}, 
    Code: {self.code}, 
    Product: {self.product}, 
    Cost: {self.cost}, 
    Quantity: {self.quantity}'''

#=============Shoe list===========
# Stores a list of objects of shoes.
shoe_list = []

#==========Functions outside the class==============
# Function created to open the file inventory.txt and read the data from this file
def read_shoes_data():

    # try and except used for error handling, such as FileNotFoundError
    try: 
        # Clear the existing shoe list, if there is any
        shoe_list.clear()

        with open('inventory.txt', 'r') as file:
            next(file)
            for line in file:
                data = line.strip().split(',')
                
                country = data[0]
                code = data[1]
                product = data[2]
                cost = float(data[3])  
                quantity = int(data[4]) 
                
                # A shoes object was created with the data from the file
                shoe = Shoe(country, code, product, cost, quantity)
                
                # Object was appended to the empty shoe_list
                shoe_list.append(shoe)

    except FileNotFoundError:
        print("File 'inventory.txt' not found.")

# The read_shoes_data() function is called so that as soon as the program is run, the list is already appended with the shoes data
read_shoes_data()
        

# Function created to allow a user to capture data about a shoe
def capture_shoes():
    shoe_country = input("Please enter the country of the shoe: ")
    shoe_code = input("Please enter the code of the shoe: ")
    shoe_product = input("Please enter the name of the shoe product: ")
    shoe_cost = int(input("Please enter the cost of the shoe: "))
    shoe_quantity = int(input("Please enter the available quantity of the shoe: "))

    # Used this data to create a shoe object 
    shoe = Shoe(shoe_country, shoe_code, shoe_product, shoe_cost, shoe_quantity)

    # Append this object inside the shoe list
    shoe_list.append(shoe)

    # Append the new captured shoe data into the existing file
    with open("inventory.txt", "a") as shoe_file:
        # Write the data for the newly added shoe
        shoe_file.write(f"\n{shoe_country},{shoe_code},{shoe_product},{shoe_cost},{shoe_quantity}")

    print("Shoe details have been captured successfully!")


# This function will iterate over the shoe list and print the details of the shoes returned from the __str__ function
def view_all():
    for shoe in shoe_list:
        print(shoe)
        

# This function will find the shoe object with the lowest quantity, which are the shoes that need to be re-stocked.
def re_stock():

    # Variable created to find the lowest quantity using the min() function, the lambda function is utilised as a custom function used to compare all quantities of shoes
    lowest_qty_shoe = min(shoe_list, key=lambda shoe: shoe.get_quantity())
    print(f"The shoe with the lowest quantity is: {lowest_qty_shoe}")
    
    # try and exccept used for invalid user inputs
    try:

        #  Ask the user if they want to add this quantity of shoes and then update it.
        restock = input("Do you want to restock this product type? Yes or No: ").lower()
        if restock == "yes":
            restock_amount = int(input("Please input the quantity at which you want to restock: "))
            lowest_qty_shoe.quantity += restock_amount
            print(f"The shoe with the lowest quantity has been restocked to {lowest_qty_shoe.quantity} successfully.\n")
        
        elif restock == 'no':
            print(f"The lowest quantity shoe remains unchanged at {lowest_qty_shoe.quantity}")
            
        else: 
            print("Invalid input. Please enter a valid option!")
        
    except ValueError:
            print("Invalid input. Please enter a valid quantity!")
                
                
    # This quantity is updated on the file for this shoe.
    with open("inventory.txt", "w") as shoe_file:
        shoe_file.write("Country,Code,Product,Cost,Quantity")
        
        for shoe in shoe_list:
            shoe_file.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")


# This function will search for a shoe from the list using the shoe code and return this object so that it will be printed
def search_shoe():
    shoe_code = input("Enter the code of the shoe you want to search for: ")
    
    # Iterate through the list to find the shoe code and print its details
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            print(f"Found Shoe: {shoe.country}, {shoe.code}, {shoe.product}, {shoe.cost}, {shoe.quantity}")
            break  # Exit the loop when the shoe is found

    # If shoe code is not found the else statement wiull trigger 
    else:
        print(f"Shoe code {shoe_code} not found.")

# This function will calculate the total value for each item
def value_per_item():
    for shoe in shoe_list:
        total_value = shoe.cost * shoe.quantity

        # Prints this information on the console for all the shoes.
        print(f"{shoe.product}: Total Value = {total_value}")
    

# Determines the product with the highest quantity
def highest_qty():

    # Variable created to find the maximum quantity using the max() function, the lambda function is utilised as a custom function used to compare all quantities of shoes
    max_quantity_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)

    # Prints this shoe as being for sale
    print(f"The shoe with the highest quantity is {max_quantity_shoe.product} with {max_quantity_shoe.quantity} units, these shoes will be put on sale.")


#==========Main Menu=============
# while loop initiated to continuosly display the menu requesting the user to input a menu option
while True:
    print("\nMenu")
    menu_options = input('''
1. Display shoes data from 'inventory.txt' file
2. Capture shoes data
3. Display all updated shoes data
4. Restock low quantity shoes
5. Search for shoe using shoe code
6. Calculate total value per item for all shoes
7. Shoes on sale (highest quantity)
8. Quit application

Please choose one of the following options: ''')
    
    if menu_options == '1':
        view_all()
        
    elif menu_options == '2':
        capture_shoes()
        
    elif menu_options == '3':
        view_all()
        
    elif menu_options == "4":
        re_stock()
        
    elif menu_options == "5":
        search_shoe()
        
    elif menu_options == "6":
        value_per_item()
        
    elif menu_options == "7":
        highest_qty()
        
    elif menu_options == "8":
        print("Exiting application, goodbye...")
        break
        
        