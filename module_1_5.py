immutable_var = 1, 'hello', [1, 2, 3], {'a': 10}, True
print(immutable_var)
#immutable_var[0] = 10
#print(immutable_var)
# TypeError: кортеж не поддерживает обращение по элементам
mutable_list = ([4, 5], 2)
print(mutable_list)
mutable_list[0][-1]=7
print(mutable_list)
