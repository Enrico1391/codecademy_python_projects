# Lovely Loveseat (lovely_loveseat_catalog.py)
# Keep receipts for the furniture store, lovely loveseats.

# Declare variables for the first item itemization and price
lovely_loveseat_description = '''Lovely Loveseat. Tufted polyester blend on wood. 
32 inches high x 40 inches wide x 30 inches deep. Red or white.'''
lovely_loveseat_price = 254.00

# Declare variables for the second item itemization and price
stylish_settee_description = '''Stylish Settee. Faux leather on birch. 
29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'''
stylish_settee_price = 180.50

# Declare variables for the third item itemization and price
luxurious_lamp_description = '''Luxurious Lamp. Glass and iron. 
36 inches tall. Brown with cream shade.'''
luxurious_lamp_price = 52.15

# Sales tax rate
sales_tax = .088

# Declare variables for the first customer expenses
customer_one_total = 0
customer_one_itemization = ''

# Update total and itemization for the first item purchased by the first customer
customer_one_total += lovely_loveseat_price
customer_one_itemization += '\n' + lovely_loveseat_description

# Update total and itemization for the second item purchased by the first customer
customer_one_total += luxurious_lamp_price
customer_one_itemization += '\n' * 2 + luxurious_lamp_description

# Calculate sales tax for the first customer
customer_one_tax = customer_one_total * sales_tax

# Add sales tax to the first customer total
customer_one_total += customer_one_tax

# Add empty line for readability
print('\n')

# Print the items purchased by the first customer
print('Customer one Items:', customer_one_itemization, '\n')

# Print the total cost for the first customer
print('Customer One Total:', customer_one_total)

# Add empty line for readability
print('\n')
