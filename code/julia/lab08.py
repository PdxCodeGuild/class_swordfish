#Contact List

#with open('contacts.csv', 'r') as file:
    #lines = file.read().split('\n')
    #print(lines)



dictionary = {}
with open("contacts.csv") as file:
    contact_list = []
    for line in file:
 
     contacts = line.split(",")
 

     dictionary = {'Name' :contacts[0], 'Age' :contacts[1], 'Color' :contacts[2],}
     contact_list.append(dictionary)
#print(contact_list)

def new_contact(contact_list):

    print("Add a new contact")
    name = input("Add name: ")
    age = input("Add an age: ")
    color = input("Add a color: ")

    user_dict = {}
    user_dict['Name'] = name
    user_dict['Age'] = age
    user_dict['Color'] = color

    contact_list.append(user_dict)
    return contact_list

#contact_list = new_contact(contact_list)

print(contact_list)
keep_going = True
while keep_going:
    response = input("Create new contact or find an existing contact or exit? ").lower()
    print(response)
    if response == "exit":
        keep_going = False
        print("You've exited")

    elif response == "create":
        contact_list = new_contact(contact_list)
        print(contact_list)

    elif response == len(contact_list):
        print(contact_list[0])
        

   

    

           
#print(contact_list)




    
# dictionary = {'Name' :contacts[0], 'Age' :contacts[1], 'Color' :contacts[2],}
# user_dict.append(dictionary)
# print(dictionary)

