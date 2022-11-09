const face_cards = {
    king: 10,
    queen: 10,
    jack: 10,
    10: 10,
    9: 9,
    8: 8,
    7: 7,
    6: 6,
    5: 5,
    4: 4,
    3: 3,
    2: 2,
    ace: 1,
}
let submit = document.getElementById('submit')

submit.addEventListener('click', function() {
    let card_one = document.getElementById('card_one').value.toUpperCase()
    let card_two = document.getElementById('card_two').value.toUpperCase()
    let card_three = document.getElementById('card_three').value.toUpperCase()
    let card_selection = [card_one, card_two, card_three]

    let card_score = [0]
    for (let card of card_selection) {     
        for (let key of Object.getOwnPropertyNames(face_cards)) { // cycles through all options to try to match
            if (key == card) {
                for (let i in total) { // increments each total score scenario, aka number in list
                    card_score[i] += face_cards[key]
                }
            }
        }
        
    }
    console.log(card_score)
})
