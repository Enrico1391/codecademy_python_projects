# Block Letters (initials.py)
# Display your initials on the screen in block letters and create an ASCII art.

# Enrico Rinaudo
# Fun Fact: I like dumb things.

# Add empty line for readability
print("\n")
print("\n")

# Attempt 1
# Define variables for rows of "E"
e_row_1_7 = "E" + "E" + "E" + "E" + "E" 
e_row_2_3_5_6 = "E"
e_row_4 = "E" + "E" + "E"

# Define variables for rows of "R"
r_row_1_4 = "R" + "R" + "R" + "R" 
r_row_2_3 = "R" + " " + " " + " " + "R"
r_row_5 = "R" + " " + "R"
r_row_6 = "R" + " " + " " + "R"
r_row_7 = "R" + " " + " " + " " + "R"

# Print "E" and "R" rows
print((e_row_1_7) + " " + (r_row_1_4))
print((e_row_2_3_5_6) + " " + " " + " "+ " " + " " + (r_row_2_3))
print((e_row_2_3_5_6) + " " + " " + " "+ " " + " " + (r_row_2_3))
print((e_row_4) + " " + " " + " " + (r_row_1_4))
print((e_row_2_3_5_6) + " " + " " + " " + " "+ " " + (r_row_5))
print((e_row_2_3_5_6) + " " + " " + " " + " "+ " " + (r_row_6))
print((e_row_1_7) + " " + (r_row_7))

# Add empty line for readability
print("\n")
print("\n")

# Attempt 2
# Define variables for "E" and "R"
e_r_row_1 = "E" + "E" + "E" + "E" + "E" + " " + "R" + "R" + "R" + "R"
e_r_row_2_3 = "E" + " " + " " + " "+ " " + " " + "R" + " " + " " + " " + "R"
e_r_row_4 = "E" + "E" + "E" + " " + " " + " " + "R" + "R" + "R" + "R"
e_r_row_5 = "E" + " " + " " + " " + " " + " " + "R" + " " + "R"
e_r_row_6 = "E" + " " + " " + " " + " " + " " + "R" + " " + " " + "R"
e_r_row_7 = "E" + "E" + "E" + "E" + "E" + " " + "R" + " " + " " + " " + "R"

# Print "E" and "R" rows
print(e_r_row_1)
print(e_r_row_2_3)
print(e_r_row_2_3)
print(e_r_row_4)
print(e_r_row_5)
print(e_r_row_6)
print(e_r_row_7)

# Add empty line for readability
print("\n")
print("\n")

# Attempt 3
# Print "E" and "R" rows using triple quotes for multiline strings
print("""EEEEE RRRR 
E     R   R
E     R   R
EEE   RRRR 
E     R R   
E     R  R 
EEEEE R   R""")

# Add empty line for readability
print("\n")
print("\n")

# Attempt 4
# E + R rows print
print("EEEEE RRRR")
print("E     R   R")
print("E     R   R")
print("EEE   RRRR")
print("E     R R")
print("E     R  R")
print("EEEEE R   R")

# Add empty line for readability
print("\n")
print("\n")

# Attempt 5
# E + R rows variables
row_1 = "EEEEE RRRR"
row_2_3 = "E     R   R"
row_4 = "EEE   RRRR"
row_5 = "E     R R"
row_6 = "E     R  R"
row_7 = "EEEEE R   R"

# E + R rows print
print(row_1)
print(row_2_3)
print(row_2_3)
print(row_4)
print(row_5)
print(row_6)
print(row_7)

# Add empty line for readability
print("\n")
print("\n")

# Attempt 6
# Define variables for rows of "E" and "R"
e_row_1_7 = "E" * 5
e_row_2_3_5_6 = "E"
e_row_4 = "E" * 3

r_row_1_4 = "R" * 4
r_row_2_3 = "R  R"
r_row_5 = "R R"
r_row_6 = "R  R"
r_row_7 = "R" + " " * 3 + "R"

# Print "E" and "R" rows
print(e_row_1_7 + " " +r_row_1_4)
print(e_row_2_3_5_6 + " " + " " + " "+ " " + " " + r_row_2_3)
print(e_row_2_3_5_6 + " " + " " + " "+ " " + " " + r_row_2_3)
print(e_row_4 + " " + " " + " " + r_row_1_4)
print(e_row_2_3_5_6 + " " + " " + " " + " "+ " " + r_row_5)
print(e_row_2_3_5_6 + " " + " " + " " + " "+ " " + r_row_6)
print(e_row_1_7 + " " + r_row_7)

# Add empty line for readability
print("\n")
