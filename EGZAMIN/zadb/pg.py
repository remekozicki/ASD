dict = {}
key1 = 1
key2 = 3
key3 = 0
key4 = 10

dict.update({f'{key1}' : 10})
dict.update(key2 = 0)
dict.update(key3 = 2)
dict.update(key4 = 12)

dict[key1] = dict.get(key1) + 1

print(dict[key1])
