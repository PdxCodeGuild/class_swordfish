with open('contacts.csv', 'r') as file:
    headers = file.readline().split(",") #splits off line one of contacts as header
    #print("Print headers: ", headers) #prints list of headers (keys) in a list
    number_of_rows = len(headers) #get variable for number of rows for looping?
    contacts_list = [] #final answer
    
    contacts_ = file.readlines() #splits the rest of the contacts by line
    rows_list = []
    for row in contacts_:
        rows_list.append(row.split(",")) #split each contact into a list
    print(rows_list)

    for data in rows_list:
        str(rows_list[0]).split()
        contacts_list.append(data)
    print(contacts_list)
    #loop through and add each thing to dict via index??
       
    """ 
    fc = dict(zip(headers,contacts_))
    print("fc: ",fc) """ #prints one dict  """
    
     
    
    """ 
    contacts_list.append(fc)
    print("contacts_list: ", contacts_list) #prints list of dictionary contacts_list
    print(fc)
   """