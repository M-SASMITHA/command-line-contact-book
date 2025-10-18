contacts=[]
def display_menu():
    print("CONTACT BOOK")
    print("1)Add contact")
    print("2)View contact")
    print("3)Exit")

def add_contact():
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
    print("CONTACT SAVED SUCCESSFULLY")

def view_contact():
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

def main():
    while True:
          display_menu()
          choice=input("choose an option(1-3): ")
          if choice=="1":
              add_contact()
          elif choice=="2":
              view_contact()
          elif choice=="3":
              print("EXITING PROGRAM!")
          else:
              print("INVALID CHOICE!")
main()


    

            