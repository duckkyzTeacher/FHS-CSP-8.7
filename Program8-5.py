# Problem 1: Create and print a list
# Task: Create a list called `fruits` containing "apple", "banana", "orange", "grape", and "strawberry".
# Write a program that prints the entire list, then prints each fruit on a new line using a `for` loop.




# Problem 2: Update and modify the list
# Task: Start with the list from Problem 1. Update "banana" to "blueberry", remove "grape", 
# and add "watermelon" to the end of the list. Print the modified list.




# Problem 3: Inserting and sorting
# Task: Insert "mango" between "apple" and "blueberry". Sort the list alphabetically and print the result.




# Problem 4: List slicing
# Task: Given the list `numbers = [5, 10, 15, 20, 25, 30, 35, 40]`, print the following:
# - The first 4 elements
# - The last 3 elements
# - All elements except the first and last




# Problem 5: Fix the code
# The following code has a syntax error. Fix the error and make sure the program prints the expected output:
# Expected Output: "grape"

fruits = ["apple", "orange", "banana", "grape"]
print fruits[3



# Problem 6: Logic fix
# This code attempts to remove all instances of "banana" from a list but doesn’t work as intended. Fix the logic.
# Expected output: ["apple", "orange"]

fruits = ["banana", "apple", "banana", "orange", "banana"]
lcv = 1

while lcv < len(fruits):
    if fruits[lcv] != "banana":
        del fruits[lcv]
    lcv = lcv + 1
    
print(fruits)
