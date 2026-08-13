dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

unique_names = []
union = []
only_a = []
only_b = []
for i in dataset_a:
    if not i in dataset_b:
        unique_names.append(i)
        only_a.append(i)
    else:
        union.append(i)

for i in dataset_b:
    if not i in dataset_a:
        unique_names.append(i)
        only_b.append(i)
    

print(unique_names)
print(union)
print(only_a)
print(only_b)
