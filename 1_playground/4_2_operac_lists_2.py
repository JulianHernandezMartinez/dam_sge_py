print('OPERACIONES CON LISTAS -PARTE 2\n')
print('\n')

print('XXX---SLICING-LIST,TUPLAS,STRINGS--my_list[start:stop:step]XXXX')

a_alpha_list=['A','B','C','D','E','F','G','H','I','J','K']
print('una rebanada de los elementos de la lista conteniendo el elementos desde la C(index=2) hasta la I(index=-2), en pasos de a 2',a_alpha_list[2:-2:2])
print('La lista no se modifica, permanece igual', a_alpha_list)
print('otra rebanada hacia atras y de uno en uno',a_alpha_list[-2:-7:-1])
a_alpha_sublist=a_alpha_list[::-3]
print('la sublista de elementos en pasos de a 3', a_alpha_sublist)

print('XXXXXXXXXXXXXXXXXXX---REVERSE LIST in_place . reverse() and others XXXXXXXXXXXXXXXXXXX')



# In-place reverse
a_alpha_list.reverse()
print('Using list reverse:', a_alpha_list)
# Let's revert that...
a_alpha_list.reverse()

# Create a new, reversed list with slices descendant
a_alpha_list_reversed= a_alpha_list[::-1]
print('Reversed 2nd list: ', a_alpha_list_reversed)

# Or use a reversed iterator
rev = reversed(a_alpha_list)
print('Reversed iterator: ', list(rev))

print()
print('**************-------------**************')
print()
