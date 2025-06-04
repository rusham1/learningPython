from clear_screen import clear

my_list = [1,5,3,7,2]
my_dict = {'car':4,'dog':2,'add':3,'bee':1}
my_tuple = ('d','c','e','a','b')
my_string = 'python'

print(my_list.sort())
print(my_list)

print(my_list,'original')
print(my_list.reverse())
print(my_list,'new')
print(sorted(my_list))

print(sorted(my_tuple))
print(my_tuple)

print(sorted(my_dict))
print(sorted(my_dict.items()))
print(sorted(my_dict.values() , reverse=True))
print(my_dict)

print(my_string,'original')
print(sorted(my_string))
print(my_string,'new')

my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_llist, key = lambda item :item[2]))


