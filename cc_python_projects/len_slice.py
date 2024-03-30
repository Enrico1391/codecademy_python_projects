# List of pizzas (len_slice.py)
# Practice using Python lists to organize some pizza data.

# List to record the types of pizzas offered
toppings = ['pepperoni','pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# List to record the prices of each pizza's slice
prices = [2, 6, 1, 3, 2, 7, 2]

# Declare variable to count the number of occurrences of 2 in the prices list
num_two_dollar_slices = prices.count(2)

# Declare variable to find the length of the toppings list
num_pizzas = len(toppings)

# Print how many types of pizza are being offered
print('\nWe sell', num_pizzas, 'different kinds of pizza!\n')

# Merge the two lists
pizza_and_prices = [[price, topping] for price, topping in zip(prices, toppings)]

# Print the pizzas names and prices
print(pizza_and_prices, '\n')

# Declare variable to store the prices in an ascending order
pizza_and_prices_ordered = sorted(pizza_and_prices)

# Print the ordered list
print(pizza_and_prices_ordered, '\n')

# Declare variable to store the cheapest pizza slice
cheapest_pizza_slice = pizza_and_prices_ordered[:1]

# Print the cheapest pizza slice
print(cheapest_pizza_slice, '\n')

# Declare variable to store the priciest pizza slice
priciest_pizza_slice = pizza_and_prices_ordered[-1:]

# Print the priciest pizza slice
print(priciest_pizza_slice, '\n')

# Remove the priciest pizza
pizza_and_prices_ordered.pop()

# Print the new pizzas list without the priciest pizza
print(pizza_and_prices_ordered, '\n')

# Add new topping in place of the one removed
pizza_and_prices_ordered.insert(-2, [2.5, "peppers"])

# Print new pizzas list
print(pizza_and_prices_ordered, '\n')

# Declare a variable to store the three cheapest pizzas slices
three_cheapest_slices = pizza_and_prices_ordered[:3]

#Print the three cheapest pizzas slices
print(three_cheapest_slices, '\n')

