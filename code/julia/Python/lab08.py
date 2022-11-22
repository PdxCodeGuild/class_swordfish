#Contact List

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    


dictionary = {}
contact_list = []
with open("contacts.csv") as file:
    lines = file.read().split("\n")
  
    for line in lines:
        line = lines.pop(0)
        line = line.split(",")

        contact = {'Name' :line[0], 'Age' :line[1], 'Color' :line[2]}
        contact_list.append(contact)

# print(contact_list, 'before change')
       


def new_contact(contact_list):
    print("Add a new contact: ")
    contact = {}
    contact['Name'] = input("Add name: ")
    contact['Age'] = input("Add an age: ")
    contact['Color'] = input("Add a color: ")
    return contact

 

def retrieve_contact(contact_list):
    search_name = input("Enter a name: ")
    for contact in contact_list:
        #check if person at the key of name is == to contact
        if search_name == contact['Name']:
            return contact_list



def update_contact(contact_list):
    update_name = input("Update contact: ")
    for contact in contact_list:
        if update_name == contact['Name']:
            user = input(f"What do you want to change: {', '.join(list(contact.keys()))}? ")
            contact[user] = input("\n>>> ")
            return contact

def delete_contact(contact_list):
    user_delete = input("Enter the name of contact you wish to delete: ")
    confirm_deletion = input("Are you sure you want to delete? ")
    if confirm_deletion.lower() in ['yes']:
        del contact_list[user_delete['Name']]
        return contact_list
    
    # for contact in contact_list:
    # del contact_list[user_delete]
        # contact['Name']:
            # contact.pop(user_delete)
    # return contact_list
            
    # contacts = contact_list(user_delete)
    # confirm_deletion = input(f"Are you sure you want to delete {contact[user_delete]['Name']}? ")
    # if confirm_deletion.lower() in ['yes']:
    #     contact.pop(contact_list[user_delete])
    # for contact in contact_list:
    #     if user_delete == contact['Name']:
    #         contact[user_delete] = input("\n>>>")
    #     return contact_list




print(contact_list)

keep_going = True
while keep_going:
    response = input("\nWhat would you like to do? Enter 'c' to create a new contact, 'r' to retrieve a contact record, 'u' to update an existing contact record, 'd' to delete an existing contact record, or 'exit' to exit: ").lower()
    print(response)

    if response == "exit":
        keep_going = False
        print("You've exited")
        

    elif response == "c":
        contact = new_contact(contact_list)
        contact_list.append(contact)
        print(contact_list)

    elif response == "r":
        retrieve = retrieve_contact(contact_list)
        print(retrieve)

    elif response == "u":
        update = update_contact(contact_list)
        print(update)
       
    elif response == "d":
        delete = delete_contact(contact_list)
        print(delete)
        


   


        # for key in range(len(contact_list)):
        #     print(contact_list[0])
        

   
    

           
# print(contact_list)




    

