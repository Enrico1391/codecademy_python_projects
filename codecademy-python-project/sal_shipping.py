# Input package weight
package_weight = float(input('\nPlease, input the weight of the package you want to ship.\n'))

# Ground Shipping Price Calculation
def ground_cost_package_weight():
  if package_weight <= 2:
    ground_cost = package_weight * 1.50 + 20
  elif package_weight <= 6:
    ground_cost = package_weight * 3.00 + 20
  elif package_weight <= 10:
    ground_cost = package_weight * 4.00 + 20
  else:
    ground_cost = package_weight * 4.75 + 20
  return ground_cost
  
ground_cost = ground_cost_package_weight()

# Ground Shipping Premium Price Calculation
ground_shipping_premium_price = "${}".format(125)

# Drone Shipping Price Calculation
def drone_cost_package_weight():
    if package_weight <= 2:
      drone_cost = package_weight * 4.50
    elif package_weight <= 6:
      drone_cost = package_weight * 9
    elif package_weight <= 10:
      drone_cost = package_weight * 12
    else:
      drone_cost = package_weight * 14.25
    return drone_cost

drone_cost = drone_cost_package_weight()

# Print the Three Shipping Prices
print('\nGround Shipping Cost: ${}' .format(ground_cost))
print('Ground Shipping Premium Cost:', ground_shipping_premium_price)
print('Drone Shipping Cost: ${}' .format(drone_cost), '\n')