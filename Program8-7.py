# Problem 1: Swap the first a last values of the following lists:
list1 = []
for num in range(10):
    list1.append(num+1)
list2 = ["pizza", "pasta", "calzone", "salad", "soup"]

list2.sort()
list1.reverse()


#Write your code here


print(list1) #should print [1, 9, 8, 7, 6, 5, 4, 3, 2, 10]
print(list2) #should print ["soup", "pasta", "pizza", "salad", "calzone"]



# Problem 2: Count the number of odd numbers in the list:

import random
randList = []
for lcv in range(10):
    randList.append(int(random.random()*100))

oddCount = 0;
#Write your code here



print(oddCount)

# Problem 3: Shift all items left 2. If the item would be outside the array, wrap it to the back.
wrapList = []
for num in range(20,30):
    wrapList.append(num)


#write your code here


print(wrapList)



# Problem 4: Use a loop to remove every element from the list except the middle element
removeList = []
for num in range(7):
    removeList.append(int(random.random()*100))
removeList[int(len(removeList)/2)] = 999

#Write your code here


print(removeList)
