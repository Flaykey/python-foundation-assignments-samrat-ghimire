monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

sort_list = sorted(monthly_sales , reverse=True)
filtered = [x for x in monthly_sales if x > 100000]
tax = [(x + 0.13 * x) for x in monthly_sales ]
total = sum(monthly_sales)
average = total / len(monthly_sales)

print(sort_list)
print(filtered)
print(tax)
print(total)
print(average)