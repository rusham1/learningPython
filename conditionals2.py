def num_days(month):

    if month == 'jan' or 'mar' or 'may' or 'jul' or 'aug' or 'oct' or 'dec':
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    else:
        print('number of days in',month,'is',30)

num_days('oct')