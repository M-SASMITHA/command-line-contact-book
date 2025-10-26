import json
def load_contacts(filename="contacts.json"):
    try:
        with open(filename,"r") as file:
            contacts=json.load(file)
            return contacts
    except FileNotFoundError:
        print("No saved contacts from the file")
        return[]
    
def save_contact(contacts,filename="contacts.json"):
    with open(filename,"w") as file:
        json.dump(contacts,file,indent=4)

def display_menu():
    print("CONTACT BOOK")
    print("1)Add contact")
    print("2)View contact")
    print("3)Search contact")
    print("4)Delete contact")
    print("5)Exit")

def add_contact(contacts):
    name=input("Enter your full name: ")
    while True:
        phone=input("Enter your contact number: ")
        if phone.isdigit():
           break
        else:
            print("INVALID NUMBER!contact number should contain only number")
    email=input("Enter your email ID:")
    contact={"name":name,"phone":phone,"email":email}
    contacts.append(contact)
    save_contact(contacts)

def view_contact(contacts):
    if len(contacts)==0:
        print("NO CONTACTS SAVED!")
    else:
        print("CONTACT LIST")
        print("-"*40)
        for i,contact in enumerate(contacts,start=1):
            print(f"{i}.Name:{contact['name']}")
            print(f"Phone:{contact['phone']}")
            print(f"Email:{contact['email']}")
            print("-"*40)

def search_contact(contacts):
    name=input("Enter the contact name to be searched: ")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            print("CONTACT FOUND!")
            print(f"Name: {contact['name']}")
            print(f"Number: {contact['phone']}")
            print(f"Email: {contact['email']}")
            break
    else:
        print("NO CONTACTS FOUND!")

def delete_contact(contacts):
    name=input("Enter the contact name to be deteled: ")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            contacts.remove(contact)
            print("CONTACT DELETED SUCCESSFULLY!")
            print("-"*40)
            save_contact(contacts)
            break
    else:
        print("NO CONTACTS FOUND!")
        print("-"*40)

def main():
    contacts=load_contacts()
    while True:
          display_menu()
          choice=input("choose an option(1-5): ")
          if choice=="1":
            add_contact(contacts)
            print("CONTACTS SAVED SUCCESSFULLY")
            print("-"*40)
          elif choice=="2":
            view_contact(contacts)
          elif choice=="3":
            search_contact(contacts)
          elif choice=="4":
            delete_contact(contacts)        
          elif choice=="5":
            print("EXITING PROGRAM!")
            save_contact(contacts)
            break
          else:
            print("INVALID CHOICE!")
main()


    
