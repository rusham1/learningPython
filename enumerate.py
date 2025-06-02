print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
for afriend in friends:
    print(afriend)
    
for num,afriend in enumerate(friends,20):
    print(num, afriend)
