def display_menu():
    print("CONTACT BOOK")
    print("1.Add contact")
    print("2.View Contacts")
    print("3.Exit")

def add_contact(contacts):
    name=input("Enter your full Name: ")
    phone=input("Enter your contact number: ")
    email=input("Enter your email ID: ")
    contact=[name,phone,email]
    contacts.append(contact)
    print("Contacts added successfully")

def view_contact(contacts):
    print("CONTACT LIST")
    if len(contacts)==0:
       print("No contacts found")
    else:
        i=1
        for person in contacts:
            print(f"{i}.Name:{person[0]}\nPhone no:{person[1]}\n Email id:{person[2]}")

def main():
    contacts=[]
    while True:
        display_menu()
        choice=input("choose an option (1,2,3): ")
        if choice=="1":
            add_contact(contacts)
        elif choice=="2":
            view_contact(contacts)
        elif choice=="3":
            print("Exiting contact book!")
            break
        else: 
            print("INAVLID CHOICE")  
main()                               