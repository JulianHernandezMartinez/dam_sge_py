# https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/


print("playgroung de accesos, \nasignaciones, borrados y troceados \nde tipos secuenciales, \ndesde el string al array,\npasando por las tuplas, listas, \nsets, diccionarios y RANGOS")


colors = ['red', 'green', 'blue', 'yellow', 'white', 'black']

#Asignacion (solo elementos con indice)
colors[5]="purple"
print(colors)
#Borrado
del(colors[0])
print(colors)

# Asignacion y borrado no aplicable 
# a tipos inmutables

#Slices
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90] #index 0 to 8
some_nums = nums[2:7]
print(nums)
print(some_nums)
print(nums[2:7])


#First elements in a list
print(nums)
firsts_nums=nums[:3]
print(firsts_nums)  # 10, 20, 30

#Last elements in a list
print(nums)
lasts_nums=nums[-3:] 
print(lasts_nums) # 70, 80, 90

#Excluding first and last
print(nums)
excl_first_amd_last_num = nums[1:-1] 
print(excl_first_amd_last_num)


# Slices are quite ranges of elements
# range concept (start, stop, step)

range_from2_to10_steps2=range(2,10,2)
print(range_from2_to10_steps2)
for element in range_from2_to10_steps2:
    print(element)

#Slices with range concept
#lsuof nums starting al index 2,
# stoping at index 7, with steps of 2

print(nums)
slice_of_list=nums[2:7:2] # with the same order
print(slice_of_list) # 30,50,70
print(nums)
slice_of_list_inverted=nums[-2:-7:-2] # with the inverted order
print(slice_of_list_inverted) #80,60,40

# aplica a todos los tipos secuenciales 
# "tipo array" desde el string hasta...
# ....
#  
a="como una cabra"
print("al revés", a[::-1])

