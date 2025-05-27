sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_sales=int(input("Enter new sales of week 2: "))
sales_w2.append(new_sales)
sales.extend(sales_w1)
sales.extend(sales_w2)
print(sales)
print("If profit per day is $1.5")
print("Highest sales in week 1: $", 1.5*max(sales_w1))
print("Highest sales in week 2: $", 1.5*max(sales_w2))
print("Total sales in week 1: $", 1.5*sum(sales_w1))
print("Total sales in week 2: $", 1.5*sum(sales_w2))
print("Total sales in both weeks: $", 1.5*sum(sales))