# School gradebook (gradebook.py)
# Practice using Python lists by keeping track of grades in multiple school subjects.

# Declare variable for last semester subjects and grades
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Declare variable for this semester subjects and grades
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Merge the two lists into a 2-D List
gradebook = [[subject, grade] for subject, grade in zip(subjects, grades)]

# .append two new subjects and grades
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Add 5 points to visual arts grade
gradebook[-1][-1] += 5

# Remove poetry grade and .append a new one
gradebook[2].remove(85)
gradebook[2].append("Pass")

# Add the two semesters
full_gradebook = last_semester_gradebook + gradebook

# Print the outcome
print('\nThis year subjects and grades:\n', full_gradebook, '\n')
