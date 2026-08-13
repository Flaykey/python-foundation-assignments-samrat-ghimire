raw_values = [100, None, 250, "invalid", 300, None, 450]
new = []
for val in raw_values:
    if isinstance(val , int):
        new.append(val)

print(new)

list_compre = [ x for x in raw_values if isinstance(x,int)]

print(list_compre)