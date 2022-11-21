class ATM {
    constructor(balance=200) {
        this.balance = parseInt(balance)
        this.interest = 0.01
        this.transactions_list = []
    }
    transactions() {
        return this.transactions_list
    }
    check_balance() {
        return this.balance
    }
    deposit(deposit) {
        this.balance += parseInt(deposit)
        this.transactions_list.push('user deposited ' + deposit)
        return deposit
    }
    withdrawal(amount) {
        if (this.balance >= parseInt(amount)) {
            this.balance -= parseInt(amount)
            this.transactions_list.push('user withdrew ' + amount)
            alert('This is how much you withdrew ' + amount)
        } else {
            alert('Insufficient Funds')
        }
        return amount
    }
    calc_interest() {
        return (this.balance * this.interest)
    }
}

let atm = new ATM()
// console.log('The ATM', atm) // test in developer
// console.log(`The ATM ${atm}`)  // presents in developer as object, object

// atm.deposit(50)   // testing deposit function
// atm.withdrawal(355) // testing withdrawal function
// alert(atm.calc_interest())  // testing interest calc function

// console.log(atm.balance)
// alert(atm.transactions())

while (true) {
    command = prompt('Enter a command: ')
    if (command === 'balance') {
        alert('This is your balance ' + atm.check_balance())
    } else if (command === 'deposit') {
        deposit = prompt('How much would you like to deposit? ')
        console.log('the deposit' + deposit)
        atm.deposit(deposit)
        alert('This is how much you deposited ' + deposit)
    } else if (command === 'withdraw') {
        amount = prompt('How much would you like to withdraw? ')
        atm.withdrawal(amount)
    } else if (command === 'interest') {
        alert('This is your interest on your current balance: ' + atm.calc_interest())
    } else if (command === 'transactions') {
        alert('This is your list of transactions ' + atm.transactions())
    } else if (command === 'exit') {
        break
    } else alert('Please try again')
}