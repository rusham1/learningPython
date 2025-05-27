friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
print('Eric' in friends)
print('John' in friends)
print('Eric' in friends and 'John' in friends)
print (friends.union(my_friends)) #union
print (friends | (my_friends)) #union
print (friends.intersection(my_friends)) #intersection
print(friends.difference(my_friends)) #difference
print(friends - my_friends) #difference
print(friends.symmetric_difference(my_friends)) 
print(friends ^ my_friends) #symmetric difference
setCars = list(set(cars)) 
print(setCars)