my_dict = {'Pushkin' : 1977, 'Esenin' : 1895, 'Bunin' : 1870, 'Marshak' : 1887}
print(my_dict)
print(my_dict['Pushkin'])
my_dict['Phet'] = 1820
print(my_dict)
my_dict.update({'Turgenev' : 1818, 'Tolstoy' : 1828})
print(my_dict)
a = my_dict.pop('Pushkin')
print(my_dict)
print(a)
my_set = {1, 4, 5, 'Pushkin', 4, 6, True, 6}
print(my_set)
print(my_set.add('run'))
print(my_set)
print(my_set.add(8))
print(my_set)
print(my_set.discard(4))
print(my_set)