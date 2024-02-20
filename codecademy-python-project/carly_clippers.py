# Carly Hair Salon trends (carly_clippers.py)
# Practice loops to discover trends in the operation of the hair salon, Carly’s Clippers.

# Declare variables for names and prices of haircuts
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", 
              "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Declare variable for amount of haircuts sold last week
last_week_haircuts_sold = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculate the sum of all the prices and print it
total_price = sum(prices)
print('\nTotal Price: ${}' .format(total_price), '\n')

# Declare variable for the prices' average and print it
average_price = total_price / len(prices)
print('Average Haircut Price: ${}' .format(average_price), '\n')

# Create new list with lowered prices and print it
new_prices = ['${}'.format(price - 5) for price in prices]
print('Revised Prices:', new_prices, '\n')

# Calculate last week total revenue and print it
total_revenue = sum(price * cuts_sold for price, cuts_sold 
                    in zip(prices, last_week_haircuts_sold))
print('Total Revenue: ${}' .format(total_revenue), '\n')

# Calculate last week's daily revenue and print it
average_daily_revenue = int(total_revenue / 7)
print('Daily Revenue: ${}'.format(average_daily_revenue), '\n')

#Generate list of haircuts under $30 based on the new_prices list
cuts_under_30 = [(cuts, new_price) for cuts, new_price 
                 in zip(hairstyles, new_prices) 
                 if int(new_price.strip('$')) < 30]
print('Hairstyles under $30:', cuts_under_30, '\n')