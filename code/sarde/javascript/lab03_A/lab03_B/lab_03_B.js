let user_name = document.querySelector('#user_name');
let favorite_fruit = document.querySelector('#favorite_fruit')
let favorite_color = document.querySelector('#favorite_color');
let create_bt = document.querySelector('#create_bt');
let created_div = document.querySelector('#created_div');
// let retrieved_name = document.querySelector('#retrieved_name');
// let retrieve_bt = document.querySelector('#retrieve_bt');
// let retrieved_div = document.querySelector('#retrieved_div');
create_bt.onclick = function () {
    let contacts = [
        { name: 'Eryan', favoriteFruit: 'Strawberries', favoriteColor: 'Green' },
        { name: 'Salena', favoriteFruit: 'Blueberries', favoriteColor: 'Purple' },
        { name: 'Eryn', favoriteFruit: 'Apples', favoriteColor: 'Magenta' },
        { name: 'Slade', favoriteFruit: 'Raspberries', favoriteColor: 'Blue' },
        { name: 'Sarde', favoriteFruit: 'Pineapple', favoriteColor: 'Pink' },
    ]
    console.log(contacts) //typeof Array
    let name = user_name.value
    console.log('name:', name)
    let favoriteFruit = favorite_fruit.value
    console.log('favoriteFruit:', favoriteFruit)
    let favoriteColor = favorite_color.value
    console.log('favoriteColor:', favoriteColor)
    let newContact = {
        name: name,
        favoriteFruit: favoriteFruit,
        favoriteColor: favoriteColor
    }
    contacts.push(newContact)
    console.log(newContact)
    created_div.innerText = `${newContact}`
    console.log(created_div)
}

let retrieved_name = document.querySelector('#retrieved_name');
let retrieve_bt = document.querySelector('#retrieve_bt');
let retrieved_div = document.querySelector('#retrieved_div');
retrieve_bt.onclick = function () {
    let name = retrieved_name.value;
    console.log(name);
    // retrieved_div.innerText = `${name}`;
    // console.log(retrieved_div)
}