total_rows = 2000
missing_rows = 120
duplicate_rows = 30

problematic_rows = missing_rows + duplicate_rows
problematic_percentage = (problematic_rows / total_rows) * 100


print(f"Total rows: {total_rows}")
print(f"Problematic rows: {problematic_rows}")
print(f"Problematic percentage: {problematic_percentage}")

if(problematic_percentage <= 2.0):
    print("Excellent")
elif(problematic_percentage <= 5):
    print("Acceptable")
else:
    print("Needs Cleaning")

