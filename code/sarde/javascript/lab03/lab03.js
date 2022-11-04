//Lab 8: Contact List

//contact Array of Objects
let contacts = [
    { name: 'Sarde', favoritefruit: 'Pineapple', favoritecolor: 'Pink' },
    { name: 'Eryan', favoritefruit: 'Strawberries', favoritecolor: 'Green' },
    { name: 'Salena', favoritefruit: 'Blueberries', favoritecolor: 'Purple' },
    { name: 'Eryn', favoritefruit: 'Apples', favoritecolor: 'Magenta' },
    { name: 'Slade', favoritefruit: 'Raspberries', favoritecolor: 'Blue' }
]
console.log(contacts) //typeof Array

let theFirstPerson = contacts[0]
let theKeys = Object.keys(theFirstPerson)
//OBJECTS
console.log(theFirstPerson)//{name: 'Sarde', favoritefruit: 'Pineapple', favoritecolor: 'Pink'}
console.log(theKeys)//['name', 'favoritefruit', 'favoritecolor']


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
function createContact(theKeys, contacts) {
    //create a record
    // ask the user for name, favorite fruit, favorite color
    let userName = prompt('Enter your name')
    let userFavoriteFruit = prompt('Enter your favortie fruit')
    let userFavoriteColor = prompt('Enter your favorite color')
    // add what the user inputs to contacts
    let newContact = {
        'theKeys[0]': userName,
        'theKeys[1]': userFavoriteFruit,
        'theKeys[2]': userFavoriteColor
    }
    //use some method to add the newContact to contacts
    contacts.push(newContact)
    console.log(newContact)
    // alert(newContact)

    return contacts

}
createContact(theKeys, contacts)