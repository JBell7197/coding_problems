#getting inputs on the same line
number_of_soldiers = int(input("How many soldiers: "))

weapons_storage = []
for i in range(number_of_soldiers):
    number_of_weapons = int(input("How many weapons: "))
    weapons_storage.append(number_of_weapons)
    even_counter = 0
    odd_counter = 0
    
for weapons in weapons_storage:
    if weapons % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

if even_counter > odd_counter:
    print("Ready for battle")
else:
    print("Not Ready")