series={
    'title':'Friends',
    'genre':['romance','comedy','friendship'],
    'characters':['Ross','Rachel','Monica','Chandler','Pheobe','Joey'],
    'no of seasons':10
}
series['title']='Riverdale'
series['cast']='Cole Sprouse'

print(series['title'])
print(series.get('cast'))
print(series.get('cast','not found'))
del series['cast']
poppedElement=series.pop('title')
print(poppedElement)
print(series.get('title'))
print(series.keys())
print(series.items())

for key,value in series.items():
    print(key,value)