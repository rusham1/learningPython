names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman' , 'TERRY', 'terry jones']
for i in range (len(names)):
    names[i] = names[i].title()
names1=[name.title() for name in names1]
print(names)
addedName=input('Enter a name to add: ')
addedName2=input('Enter a second name to add: ')
names.append(addedName.title())
names.append(addedName2.title())
print(names)
for i in range(len(names)):
    print(names[i],", You are invited to the party on Saturday!")

for i in range(len(names1)):
    print(names1[i],", You are invited to the party on Saturday!")