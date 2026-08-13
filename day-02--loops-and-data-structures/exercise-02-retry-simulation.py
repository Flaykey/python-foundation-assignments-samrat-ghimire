attempt = 1
max_attempts = 3
operation_successful = False

while (attempt <= max_attempts):
    if(attempt == 2):
        operation_successful = True
        break
    attempt+=1

if( operation_successful == True):
    print("Operation completed successfully")
else:
    print("Operation failed after three attempts")