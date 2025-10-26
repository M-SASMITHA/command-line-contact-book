A Simple contacts saving applicaion,here we can save the contacts,search the contact by contact name,delete the unwanted contacts and also we can view all the contacts saved in the file.
contacts are automatically loaded from the "contacts.json" file when the program starts.
Contacts are saved to "contacts.json" file when we exit the program
Phone number validation: We can only enter only number or else it prints invalid

#To run the program 
-make sure you have python3 installed
-save contact_book4.py to a folder
-run in the terminal
-a contacts.json file will be created automatically!

MY LEARNING JOURNEY
   The biggest challenge was to study about file handling methods,to add the search and delete options.
   Initially, when I deleted a contact, it disappeared only temporarily.
   After restarting the program, all the deleted contacts reappeared.
   This happened because I was removing the contact only from the list in memory and not updating the contacts.json file on the disk.

   How I Solved It:
   I analyzed the code and realized that after modifying the contact list (adding or deleting), I needed to save the updated list back to the JSON file.
   To fix the issue, I called the function save_contacts(contacts) immediately after any change (especially after deleting a contact).

   Although, I enjoyed the learning journey which taught me more new topics like,to handle the json file (which was a whole new topic for me )and to solve errors in the code.
   It was a great experience to work on this project and to explore things!  
