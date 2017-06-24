# new_list = [3, 2, 5, 7]
# print('new list is', new_list)
# print('new_list[2] is', new_list[2])
# print('new_list[0:2] is', new_list[0:2])
# for item in new_list:
# 	print(item)
# new_list[1] = 4
# new_list[3] = 6
# print('new list:', new_list)
# print('new list[0:2] is', new_list[0:2])
# new_list.append(8)
# print('new list:', new_list)
# new_list.insert(4, 7)
# print('new list:', new_list)
# # new_list.reverse()
# try:
# 	new_list.remove(77)
# except ValueError:
# 	print('The value is not in the list!')
# print(new_list)

# example of list comprehension in python
# ex1:make a list of letter in a string
# print([letter for letter in 'hello,world'])

# ex2:add an exclamation point to every letter
# print([letter + '!' for letter in 'hello,world'])

# ex3:a multiplication table for the 9's
# print([9 * num for num in range(13)])

# Example 4: Make a list of letters in a string if they're not 'o'"
print([letter for letter in "Hello, World!" if letter != 'o'])
