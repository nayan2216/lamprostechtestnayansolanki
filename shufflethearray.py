#importing random 
import random 
# Assign  the array 
arr = [1, 2, 3, 4, 5, 6]
 
# print original array
print("Original List: ", arr)
 
# get the len of the list
n = len(arr)
 
# for loop 

for i in range(n):
    #select an index randomly 
    j = random.randint(0, n-1)
    # elete the element at that index.
    element=arr.pop(j)
    # now append the deleted element
    arr.append(element)
print("Shuffled List: ",arr)
