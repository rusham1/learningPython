python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

print('Arthur' and "Galahad"in holy_grail)
if "Arthur" not in life_of_brian:
    print('He\'s not in life_of_brian')

people={}
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(people)

people1={}
for i in (python,holy_grail,life_of_brian):
    people1.update(i)

print(people1)
