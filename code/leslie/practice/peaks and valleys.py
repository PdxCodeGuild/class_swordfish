data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks_list = []
    i=0
    for i in range(len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks_list.append(i)
            i+1
            
            #return data[i] # prints 7
            #return i # prints 6
    print("Peaks: ", peaks_list)       
peaks(data)

#Do I need a return statement^^? It prints without one, but do I need one in order to be able to access peaks_list outside of the function?

#This is including 0 index in list. Trying to figure out how to get rid of it.
def valleys(data):
    valleys_list = []
    i=0
    for i in range(len(data)-1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            valleys_list.append(i)
            i+1
    print("Valleys: ", valleys_list)
valleys(data)    
#To combine the 2 lists, I have to be able to access them outside of the functions
