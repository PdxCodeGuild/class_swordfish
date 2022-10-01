#Contact List

#with open('contacts.csv', 'r') as file:
    #lines = file.read().split('\n')
    #print(lines)



dictionary = {}
with open("contacts.csv") as file:
    contact_list = []
    lines = file.read().split("\n")
    
    for line in lines:
        line = line.split(",")

        contact = {'Name' :line[0], 'Age' :line[1], 'Color' :line[2]}
        contact_list.append(contact)


def new_contact():
    print("Add a new contact")
    contact = {}
    contact['name'] = input("Add name: ")
    contact['age'] = input("Add an age: ")
    contact['color'] = input("Add a color: ")
    return contact

def retrieve(contact, c_list):
    for person in c_list:
       
        #check if person at the key of name is == to contact
        print(person)






print(contact_list)
keep_going = True
while keep_going:
    response = input("\nWhat would you like to do? Enter 'c' to create a new contact, 'r' to retrieve a contact record, 'u' to update an existing contact record, 'd' to delete an existing contact record, or 'exit' to exit: ").lower()
    print(response)
    if response == "exit":
        keep_going = False
        print("You've exited")

    elif response == "c":
        contact = new_contact()
        contact_list.append(contact)
        print(contact_list)

    elif response == "r":
        contact = input('Enter a name')
        print(retrieve(contact, contact_list))




    elif response == len(contact_list):
        print(contact_list[0])
        

   

    

           
print(contact_list)




    

