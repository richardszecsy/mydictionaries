person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)
#name of 2nd child
print(person.get('children')[1])
print(person['children'][1])
#name of the cat
print(type(person['pets']))
print(person['pets']['cat'])
#use a loop to list each child
for i in person ['children']:
    print(i)
#print out pets
for i, j in person ['pets'].items():
    print('Type of pet:'), (i) ('name of pet:', (j))
    