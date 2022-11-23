#Contact List

dictionary = {}
contact_list = []

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    headers_str = lines.pop(0)
    headers_list = headers_str.split(",")
    # print("lines", lines)
    # print("headers", headers_str)
    # print(headers_list[0])
  
    for line in lines:
        # print("before pop", line)
        line = line.split(",")
        # print("after pop", line)

        contact = {headers_list[0] :line[0], 'Age' :line[1], 'Color' :line[2]}
        contact_list.append(contact)

print(contact_list, 'before change')
       


def new_contact(contact_list):
    print("Add a new contact: ")
    contact = {}
    contact['Name'] = input("Add name: ")
    contact['Age'] = input("Add an age: ")
    contact['Color'] = input("Add a color: ")
    contact_list.append(contact)
    return contact_list
    


def retrieve_contact(contact_list):
    search_name = input("Enter a name: ")
    for contact in contact_list:
        #check if person at the key of name is == to contact
        if search_name == contact['Name']:
            return contact


def update_contact(contact_list):
    update_name = input("Update contact: ")
    for contact in contact_list:
        if update_name == contact['Name']:
            user = input(f"What do you want to change: {', '.join(list(contact.keys()))}? ")
            if user in list(contact.keys()):
                contact[user] = input("\n>>> ")
                print("accepted")
            else: 
                print("not accepted")
            
            return contact_list

def delete_contact(contact_list):
    user_delete = input("Enter the name of contact you wish to delete: ")
    confirm_deletion = input("Are you sure you want to delete? ")
    if confirm_deletion.lower() in ['yes']:
      for contact in contact_list:
          if user_delete == contact['Name']:
              contact_list.remove(contact)
              print(contact)
    print("Updated contact list: ",contact_list)          
          
def save(contact_list):
    with open('contacts.csv', 'w') as file:
        file.write(headers_str)
        file.write("\n")
        for contact in contact_list:
            file.write(",".join(list(contact.values())))
            file.write("\n")


keep_going = True
while keep_going:
    response = input("\nWhat would you like to do? Enter 'c' to create a new contact, 'r' to retrieve a contact record, 'u' to update an existing contact record, 'd' to delete an existing contact record, or 'exit' to exit: ").lower()
    print(response)

    if response == "exit":
        keep_going = False
        print("You've exited")
        save(contact_list)
        

    elif response == "c":
        contact_list = new_contact(contact_list)
        print(contact_list)

    elif response == "r":
        contact = retrieve_contact(contact_list)
        print(contact['Name'])
        print(contact['Age'])
        print(contact['Color'])

    elif response == "u":
        contact_list = update_contact(contact_list)
        print(contact_list)
       
    elif response == "d":
        delete_contact(contact_list)
        
        


   




    

