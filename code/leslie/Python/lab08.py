with open('contacts.csv', 'r') as file:
    keys = file.readline().rstrip("\n").split(",") #splits off line one of contacts as header
    #print("Print keys: ", keys) #prints list of keys in a list
    number_of_rows = len(keys) #get variable for number of rows for looping?
    contacts_list = [] #final answer
    
    contacts_ = file.readlines() #splits the rest of the contacts by line

    
    rows_list = []
    for row in contacts_: # QUESTION: when I change it to range(len(contacts_)), I get an error. WHY?? Same as in 14.
        rows_list.append(row.rstrip("\n").split(",")) #split each contact into a list (rstrip() removed the "\n" characters)
    
    for i in rows_list: 
        zipped = dict(zip(keys,i)) #zip()combines 2 lists to make tuples, dict() made it a dictionary
        contacts_list.append(zipped)  #each value in rows_list was zipped with each header 

print("Contacts List: ", contacts_list)
while True:
    
    def new_contact():
        new_user = [] #Where to put new user info
        new_name = input("Enter new contact's name: ")
        new_user.append(new_name) #add name to list
        
        new_fruit = input("Enter new contact's favorite fruit: ")
        new_user.append(new_fruit) #add fruit to list
        
        new_color = input("Enter new contact's favorite color: ")
        new_user.append(new_color) #add color to list
        
        zipped_user = dict(zip(keys,new_user)) 
        contacts_list.append(zipped_user)
        print("Updated contacts list: ", contacts_list)    
    #new_contact()

    def retrieve_record():
        search_name = input("enter name to look up: ")
        for item in contacts_list:
            if item["name"] == search_name:
                #print("Yay")
                print(item.items())
                break
    retrieve_record()
    


    def update_record():
        contact_name = input("enter name to update: ")
        for contact in contacts_list:
            if contact["name"] == contact_name:
                attribute_to_update = input("What would you like to update? Favorite fruit, or favorite color? ")
                if attribute_to_update == "favorite fruit":
                    new_value = input("What is the new value? ")
                    #new_fruit = {"favorite_fruit": new_value}
                    contact['favorite fruit'] = new_value
                elif attribute_to_update == "favorite color":
                    new_value = input("What is the new value? ")
                    contact["favorite color"] =  new_value
    update_record() 
    
    def delete_record():
        name = input("enter name: ")
        for contact in contacts_list:
            if contact['name'] == name:
                contacts_list.remove(contact)
                
                print(contacts_list)
                    
    #delete_record()
