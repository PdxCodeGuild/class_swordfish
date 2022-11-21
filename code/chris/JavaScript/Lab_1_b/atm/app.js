class ATM {
    constructor(balance=200) {
        this.balance = parseInt(balance)
        this.interest = 0.01
        this.transactions_list = []
    }
    transactions() {
        return this.transactions_list
    }
    checkBalance() {
        let balance = `Your balance is $${this.balance}`
        return balance
    }
    deposit(deposit) {
        this.balance += parseInt(deposit)
        this.transactions_list.push('User deposited $' + deposit)
        deposit = `You deposited $${deposit}`
        return deposit
    }
    withdrawal(amount) {
        let sufficient
        if (this.balance >= parseInt(amount)) {
            this.balance -= parseInt(amount)
            this.transactions_list.push('User withdrew $' + amount)
            sufficient = `This is how much you withdrew $${amount}`
        } else {
            sufficient = `Insufficient Funds`
        }
        return sufficient
    }
    calc_interest() {
        let interest_message = `Your interest is $` + (this.balance * this.interest)
        return interest_message
    }
    exit() {
        let message = "Goodbye!"
        return message
    }
}

let atm = new ATM()

let checkBalanceButton = document.getElementById('check-balance')
let withdrawButton = document.getElementById('withdrawButton')
let depositButton = document.getElementById('depositButton')
let transactionsButton = document.getElementById('transactionsButton')
let intButton = document.getElementById('intButton')
let exitButton = document.getElementById('exitButton')

checkBalanceButton.addEventListener('click', function() {
    console.log('balance')
    let balance = atm.checkBalance()
    let p_results = document.getElementById('results')
    p_results.innerText = balance
})

withdrawButton.addEventListener('click', function() {
    console.log('withdrawal')
    let input_box = document.getElementById('withdrawing')
    console.log(input_box.value)
    let withdraw = atm.withdrawal(input_box.value)
    console.log(withdraw)
    let p_withdrawalresults = document.getElementById('withdrawalresults')
    p_withdrawalresults.innerText = withdraw
})

depositButton.addEventListener('click', function() {
    let deposit_box = document.getElementById('depositing')
    let deposit = atm.deposit(deposit_box.value)
    let p_depositresults = document.getElementById('depositresults')
    p_depositresults.innerText = deposit
})

transactionsButton.addEventListener('click', function() {
    let transaction = atm.transactions()
    let p_trans_results = document.getElementById('transresults')
    p_trans_results.innerText = transaction
})

intButton.addEventListener('click', function() {
    let interest = atm.calc_interest()
    let p_intresults = document.getElementById('intresults')
    p_intresults.innerText = interest
})

exitButton.addEventListener('click', function() {
    let exit = atm.exit()
    let p_exitm = document.getElementById('exitm')
    p_exitm.innerText = exit
})