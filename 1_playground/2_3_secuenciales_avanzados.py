#https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/

#Slices
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90] #index 0 to 8

#Slice object with slice function

print(nums)
five_items_after_second = slice(2, 2 + 5)
nums_five_after_second= nums[five_items_after_second]
print(nums_five_after_second) #30,40,50,60,70
all_but_two_last = slice(None, -2) # start can be "None"

#substitutes
nums[:4] = [1,2,3,4] #substitutes 4 elements with 1, 2, 3 and 4 values
print (nums)

# replace and resize(bigger target)
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
nums[:4] = [1,2,3,4,5,6,7]
print(nums)

# replace and resize(smaller target)

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums)
nums[:4] = [1]
print(nums)

#replace every n-th element
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums)
nums[::2] = [1,1,1,1,1] # must exactly match the size
print(nums)

#slice deletion
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums)
del nums[3:7]
print(nums)

#slice deletion with steps
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums)
del nums[::2]
print(nums)





