//Lab 8: Contact List

//contact Array of Objects
let contacts = [
    { name: 'Eryan', favoriteFruit: 'Strawberries', favoriteColor: 'Green' },
    { name: 'Salena', favoriteFruit: 'Blueberries', favoriteColor: 'Purple' },
    { name: 'Eryn', favoriteFruit: 'Apples', favoriteColor: 'Magenta' },
    { name: 'Slade', favoriteFruit: 'Raspberries', favoriteColor: 'Blue' },
    { name: 'Sarde', favoriteFruit: 'Pineapple', favoriteColor: 'Pink' },
]
console.log(contacts) //typeof Array

let theFirstPerson = contacts[0]
let theKeys = Object.keys(theFirstPerson)
//OBJECTS
// console.log(theFirstPerson)//{name: 'Sarde', favoriteFruit: 'Pineapple', favoriteColor: 'Pink'}
// console.log(theKeys)//['name', 'favoriteFruit', 'favoriteColor']





/*
Version2
-CREATE a record: ask the user for each attribute,
    -add a new contact to your contact list, with the attributes that the user entered
-RETRIEVE a record: ask the user for the contact's name
    -find the user with the given name, and display their information
-UPDATE a record: ask the user for the contact's name,
    -then for which attribute of they user they'd like to update
    -the value of the attribute they'd like to set
-DELETE a record: ask the user for the contact's name
    -remove the contact with the given name from the contact list

*/

//create a function that allows the user to create a contact
//add the created contact contacts
function createContact(theKeys, contacts) {
    //create a record
    // ask the user for name, favorite fruit, favorite color
    let userName = prompt('Enter your name')
    let userfavoriteFruit = prompt('Enter your favortie fruit')
    let userfavoriteColor = prompt('Enter your favorite color')
    // add what the user inputs to contacts
    let newContact = {
        name: userName,
        favoriteFruit: userfavoriteFruit,
        favoriteColor: userfavoriteColor
    }
    //use some method to add the newContact to contacts
    contacts.push(newContact)
    console.log(newContact)
    // alert(newContact)
    console.log(contacts)

    return contacts

}
createContact(theKeys, contacts)
// console.log(contacts)

//create a function where the user enters a contacts name, and then that name is logged for the user
function retrieveContact(contacts) {
    //ask the user for the name to search for
    let nameToSearchFor = prompt('Enter the contact\'s name you want to retrieve')
    //iterate over contacts
    contacts.forEach(function (contact) {
        // console.log(contact)
        let name = contact['name']
        //if the name entered by the user is in contacts
        //print that contact 
        if (name == nameToSearchFor) {
            // console.log(name)
            console.log(contact)
        }
        return contact
    });
}
retrieveContact(contacts)

//create a function where the user can update a contact
function updateContact(contacts) {
    //ask the user for the contacts name
    let nameToUpdate = prompt('Enter the contact\'s name you want to update')

    //iterate over the length of the contacts list
    for (let i = 0; i < contacts.length; i++) {
        //console.log(i, contacts[i])
        if (contacts[i]['name'] == nameToUpdate) {
            let inputAttribute = prompt('What do you want to update? "name", "favoriteFruit", "favoriteColor" ')
            let inputValue = prompt('What do you want to update it to?')
            contacts[i][inputAttribute] = inputValue
            // console.log(contacts)
        }
    }

    return contacts
}
updateContact(contacts)

function deleteContact(contacts) {
    //ask the user for the contact's name
    let nameToDelete = prompt('Enter the contact\'s name you want to delete')
    // iterate over the contacts
    for (let i = 0; i < contacts.length; i++) {
        if (contacts[i]['name'] == nameToDelete) {
            delete contacts[i]
        }
    }
    return contacts
}
deleteContact(contacts)

//REPL Loop
let stop = false
while (!stop) {
    let response = prompt('Enter a choice(q, c, r, u, d): ')
    if (response == 'q') {
        console.log('Person wants to quit')
        let stop = true
    } else if (response == 'c') {
        console.log('Person wants to create')
        let contact = createContact(theKeys, contacts)
        console.log(contact)
    } else if (response == 'r') {
        console.log('Person wants to retrieve')
        let contact = retrieveContact(contacts)
        console.log(contact)
    } else if (response == 'u') {
        console.log('Person wants to update')
        let contact = updateContact(contacts)
        console.log(contact)
    } else if (response == 'd') {
        console.log('Person wants to delete')
        let contact = deleteContact(contacts)
        console.log(contact)
    }
}
console.log(contacts)