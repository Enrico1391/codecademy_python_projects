# Design software to handle operations for a chain of restaurants (basta_fazoolin.py)

# Define a class representing the restaurant menus.
class Menu:
  def __init__(self, name, items, start_time, end_time):
    """
      Initialize a Menu object.

      Args:
          name (str): Name of the menu.
          items (dict): Contains menu items as keys and their prices as values.
          start_time (int): Starting time of menu availability in 24-hour format.
          end_time (int): Ending time of menu availability in 24-hour format.
    """
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    self.time_display()
    print(f'{self.name}:')

# Define a method to adjust the time display of menus to a 12-hour format 
# and determine whether to display 'am' or 'pm' suffixes.
  def time_display(self):
    start_suffix = 'am' if self.start_time < 12 else 'pm'
    end_suffix = 'am' if self.end_time < 12 else 'pm'
    start_time_12hr = self.start_time % 12 if self.start_time % 12 != 0 else 12
    end_time_12hr = self.end_time % 12 if self.end_time % 12 != 0 else 12
    if self.start_time == 0:  # Correcting midnight display
        start_time_12hr = 12
    if self.end_time == 0:  # Correcting midnight display
        end_time_12hr = 12
    self.start_suffix = start_suffix
    self.end_suffix = end_suffix
    self.start_time_12hr = start_time_12hr
    self.end_time_12hr = end_time_12hr  

# Define a method to calculate the total price of an order based on purchased items.
  def calculate_bill(self, purchased_items):
    total_price = sum(self.items[item] for item in purchased_items 
                      if item in self.items)
    return total_price

# Define a string representation method to describe the availability of the menus.
  def __repr__(self):
    return (f'Menu available from '
            f'{self.start_time_12hr}{self.start_suffix} to '
            f'{self.end_time_12hr}{self.end_suffix}.')

# Define brunch items.
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 
    'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

# Create the brunch menu instance.
brunch_menu = Menu('Brunch', brunch_items, 11, 16)

# Print the brunch menu.
print(brunch_menu,'\n')

# Define early bird menu items.
early_bird_items = {
    'salumeria plate': 8.00, 'pizza with quattro formaggi': 9.00, 
    'salad and breadsticks (serves 2, no refills)': 14.00, 'duck ragu': 17.50, 
    'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
}

# Create the early bird menu instance.
early_bird_menu = Menu('Early Bird', early_bird_items, 15, 18)

# Print the early bird menu.
print(early_bird_menu,'\n')

# Define dinner menu items.
dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 
    'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
}

# Create the dinner menu instance.
dinner_menu = Menu('Dinner', dinner_items, 17, 23)

# Print the dinner menu.
print(dinner_menu,'\n')

# Define kids menu items.
kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 
    'apple juice': 3.00
}

# Create the kids menu instance.
kids_menu = Menu('Kids', kids_items, 11, 21)

# Print the kids menu.
print(kids_menu,'\n')

# Calculate bill for one brunch order.
brunch_purchased_items = ['pancakes', 'home fries', 'coffee']
print(f'Bill No.1: ${brunch_menu.calculate_bill(brunch_purchased_items)}' 
      f' for {', '.join(brunch_purchased_items)}.\n')

# Calculate bill for one early_bird order.
early_bird_purchased_items = ['salumeria plate', 'mushroom ravioli (vegan)']
print(f'Bill No.2: ${early_bird_menu.calculate_bill(early_bird_purchased_items)}'
      f' for {', '.join(early_bird_purchased_items)}.\n')

# Define a class for the expansion of the franchise, introducing a new restaurant. 
class Franchise:
  def __init__(self, addresses, menus):
    """
      Initialize a Franchise object.

      Args:
          addresses (str): Addresses of the flagship and the new restaurant.
          menus (list): Contains the menu instances of the Menu class.
    """
    self.addresses = addresses
    self.menus = menus

# Define a method to let customers know which menu is available at what time.
  def available_menus(self, time):
    available_menus = [menu.name for menu in self.menus 
                       if menu.start_time <= time <= menu.end_time]
    return available_menus

# Define a string representation method to print the restaurants' addresses.
  def __repr__(self):
    return self.addresses

# Create the restaurants instances.

# Make a list containing the menus instances.
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

# Create the flagship store instance.
flagship_store = Franchise('1232 West End Road', menus)

# Print the flagship store address.
print(f'Flagship Store Address:\n{flagship_store}\n')

# Create the new restaurant instance.
new_restaurant = Franchise('12 East Mulberry Street', menus)

# Print the new restaurant address
print(f'New Installment Address:\n{new_restaurant}\n')

# Print which menu is available in the restaurants.
# Assuming the given time is in 24-hour format, convert it to 12-hour format.

import random
random_hr = random.randint(0, 23)

time = random_hr
if time == 0:
    time_12hr = 12
elif time <= 12:
    time_12hr = time
else:
    time_12hr = time % 12

suffix = 'am' if time < 12 or time == 24 else 'pm'

print(f'Available Menus at {time_12hr}{suffix}: '
      f'{', '.join(new_restaurant.available_menus(time))} \n')

# Define a class to manage the operations of the expanding restaurant chain.
class Business:
  def __init__(self, name, franchises):
    """
      Initialize a Business object.

      Args:
          name (str): Name of the business.
          franchises (list): Contains the instances of the two restaurants.
    """
    self.name = name
    self.franchises = franchises

# Create the business instance.
basta_fazoolin = Business('Basta Fazoolin\' with my Heart',
                           [flagship_store, new_restaurant])

# Create a menu instance for a new restaurant.

# Define the menu items.
arepas_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 
    'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

# Create the arepas menu instance.
arepas_menu = Menu('Take a\' Arepa', arepas_items, 10, 20)

# Print the arepas menu.
print(arepas_menu,'\n')

# Create the arepas franchise instance.
arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)

# Print the arepas restaurant address.
print(f'Take a\' Arepa Address:\n{arepas_place}\n')
  
# Create the new Business instance for Take a' Arepa.
take_a_arepa = Business('Take a\' Arepa', [arepas_place])