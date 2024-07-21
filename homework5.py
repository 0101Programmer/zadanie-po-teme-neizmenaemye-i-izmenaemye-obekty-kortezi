immutable_var = 1, 'apple', 8, True, [1, 8, 9]
print('Immutable tuple:', immutable_var)

print('Immutable tuple:', immutable_var * 3)
immutable_var[4][1] = False
print('Immutable tuple:', immutable_var)

# immutable_var[0] = 6
# print(immutable_var) # таким способом нельзя изменить т.к. сами кортежи не изменяемые

mutable_list = [1, 'two', 'кабанчик', False]
print('Mutable list:', mutable_list)
mutable_list[0] = 'hello'
mutable_list[3] = 'bye'
print('Mutable list:', mutable_list)