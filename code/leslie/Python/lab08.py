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
   
    def new_contact():
        new_user = [] #Where to put new user info
        new_name = input("Enter your name: ")
        new_user.append(new_name) #add name to list
        
        new_fruit = input("Enter your favorite fruit: ")
        new_user.append(new_fruit) #add fruit to list
        
        new_color = input("Enter your favorite color: ")
        new_user.append(new_color) #add color to list
        
        
        zipped_user = dict(zip(keys,new_user)) 
        contacts_list.append(zipped_user)
        #print("New user: ", new_user)
        #print(contacts_list)
    #new_contact()
    #print(contacts_list[0].keys())
    #print(contacts_list[3].values())   
    #print(contacts_list)            # 

    def find_user():
        search_name = input("enter name: ")
        for item in contacts_list:
            if item["Name"] == search_name:
                #print("Yay")
                print(item.items())
    (find_user()) 
    
    
    def update_record():
        contact_name = input("enter name: ")
        attribute_to_update = input("What would you like to update? Favorite fruit, or favorite color? ")
        new_value = input("What is the new value? ")
        for contact in contacts_list:
            if contact["Name"] == contact_name:
                