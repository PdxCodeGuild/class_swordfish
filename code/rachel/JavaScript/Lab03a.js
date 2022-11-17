//Rot 13//
let keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];

let inputPhrase = prompt ("Enter a string of letters to encypher: ");
let workingString = "";
var indexPos;
var position2;
// console.log(inputPhrase);

// let indexPos = keys.indexOf(inputPhrase);
function getIndex(inputPhrase) {
    indexPos = keys.indexOf(inputPhrase);
    return indexPos;
}

// console.log(indexPos);

for (let i in inputPhrase) {
// for (let i = 0; i < inputPhrase.length; i++) {
// for (let i = 0; i <= inputPhrase.length; i++) {
    indexPos = getIndex(inputPhrase);
    if (indexPos >= 13) {
        let position2 = indexPos - 13;
        let newLetter = keys[position2];
        console.log (newLetter);
    } else {
        position2 = indexPos + 13;
        newLetter = keys[position2];
        console.log (newLetter);
    }
    workingString += newLetter;
    // workingString.push(newLetter);
    break;
}
console.log (workingString);

// for (let i = position1; i = i+13;) {
//     let position1 = indexValue()

//     if (position1 >= 13) {
//         position2 = position1 - 13
//         new_letter = keys[position2]
//     } else {
//         positition2 = position1 + 13 
//         new_letter = keys[positition2]
//     }
// }
//     working_string += new_letter

// alert (working_string)


//Python version//
// keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
// input_phrase = input("Enter a string of letters to encypher: ")
// def index_value():
//     position1 = keys.index(i)
//     return position1
// working_string = ""
// for i in input_phrase:
//     position1 = index_value()
//     if position1 >= 13:
//         position2 = position1 - 13
//         new_letter = keys[position2]
//     else:
//         positition2 = position1 + 13 
//         new_letter = keys[positition2]
//     working_string += new_letter
// print(working_string)

//Flask version//
// keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
// @app.route('/', methods=['GET', 'POST'])
// def index():
//     if request.method =="POST":
//         user_word = request.form["user_word"]
//         #print(user_word)
//         working_string = ""
//         for i in user_word:
//             position1 = keys.index(i) #i has to be inside loop or it will return an "i is not defined" error
//             if position1 >= 13:
//                 position2 = position1 - 13
//                 new_letter = keys[position2]
//             else:
//                 position2 = position1 + 13 
//                 new_letter = keys[position2]
//             working_string += new_letter
//         return render_template('lab05.html', answer=working_string) 
//     return render_template('lab05.html')

