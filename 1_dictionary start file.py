import random


phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}


print("Number of Key Value pairs:" {len(phonebook)})


#key always on the left always in text, value on the right
#list needs an index value, dict. needs a key value

print()
print('*****  start section 1 - print dictionary ********')
print()





print()
print('*****  end section 1 ********')
print()




print()
print('*****  start section 2 - search dictionary ********')
print()

name = "Chris"

if name in phonebook:
    print(phonebook[name])
else:
    print()

print(phonebook["chris"])





print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook['Chris'] = '555-444'

phonebook['Jon'] = '555-0123'

print(phonebook)



print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()




print()
print('*****  end section 4 ********')
print()

print(phonebook)
del phonebook["Chris"]



print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:
    print('The key is:'(key) 'and the value is '(phonebook[key]))

for value in phonebook.values():
    print(value)
for k, v in phonebook.items():
    print('The key is :' (k) ' and the value is:'(v))

for ph_tuple in phonebook.items():
    print(ph_tuple)




print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()

name = "Chris"
phone = phonebook.get(name, 'key not found')

print(phone)

phonebook.clear()

print(phonebook)



print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

remove = phonebook.pop("Chris" , "not found")

print(remove)
print(phonebook)



print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

a = phonebook.popitem()
print(a)
print(phonebook)





print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
random_key = random.choice(list_of_keys)
print(random_key)
print(phonebook(random_key))




print()
print('*****  end section 9 ********')
print()








