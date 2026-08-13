contact = dict()
run = True

def display_menu():
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")

def add():
    print("Enter Name: ")
    name = input()
    print("Enter Number: ")
    number = int(input())
    print("Enter Email: ")
    email = input()

    contact[name] = {
        "Number" : number,
        "Email"  : email
    }


def search():
    print("Enter Name you want to search: ")
    name = input()
    if( name in contact):
        print(contact[name])
    

def delete():
    print("Enter Name you want to delete: ")
    name = input()
    if( name in contact):
        contact.pop(name)

def display():
    print(contact)


while run:
    display_menu()
    opt = int(input())

    match opt:
        case 1:
            add()
        case 2:
            search()
        case 3:
            delete()
        case 4:
            display()
        case 5:
            run = False
            