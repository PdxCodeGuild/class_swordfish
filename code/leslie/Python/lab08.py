with open('contacts.csv', 'r') as file:
    headers = file.readline().rstrip("\n").split(",") #splits off line one of contacts as header
    #print("Print headers: ", headers) #prints list of headers (keys) in a list
    number_of_rows = len(headers) #get variable for number of rows for looping?
    contacts_list = [] #final answer
    
    contacts_ = file.readlines() #splits the rest of the contacts by line

    
    rows_list = []
    for row in contacts_: # QUESTION: when I change it to range(len(contacts_)), I get an error. WHY?? Same as in 14.
        rows_list.append(row.rstrip("\n").split(",")) #split each contact into a list (rstrip() removed the "\n" characters)
    
    for i in rows_list: 
        zipped = dict(zip(headers,i)) #zip()combines 2 lists to make tuples, dict() made it a dictionary
        contacts_list.append(zipped)  #each value in rows_list was zipped with each header 

    print("Contacts List: ", contacts_list)