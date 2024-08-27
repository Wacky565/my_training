my_dict = {'oleg': 1998, 'Maks': 2000}
print(my_dict)
print(my_dict['Maks'])
print(my_dict.get('vladimir'))
my_dict['slavik'] = 1955
my_dict['petya'] = 2020
print(my_dict)
a = my_dict.pop('petya')
print(my_dict)
print(a)
print(my_dict)
my_set = {1, 2, 3, 1, 2, 3, 'string', 'string', 42.12}
lest = [1, 2, 3]
lest = set(my_set)
print(my_set)
my_set.update([4, 7])
print(my_set.discard(1))
print(my_set)


