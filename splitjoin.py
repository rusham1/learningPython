
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = (','.join(",".join(csv.split(";")).split(":")).split(','))
print("By split and join method",friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise
print("By replacing method, ",csv.replace(';',',').replace(':',',').split(","))