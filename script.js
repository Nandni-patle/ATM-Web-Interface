let balance = 1000;  // Initial balance
let transactionHistory = [];  // Store transaction history
let action = "";  // Track current action (deposit or withdraw)

function checkBalance() {
    document.getElementById('display').innerHTML = `<p>Your current balance is ₹${balance}</p>`;
    transactionHistory.push(`Checked balance: ₹${balance}`);
}

function deposit() {
    action = "deposit";
    document.getElementById('input-section').style.display = 'block';
}

function withdraw() {
    action = "withdraw";
    document.getElementById('input-section').style.display = 'block';
}

function viewHistory() {
    let history = transactionHistory.length ? transactionHistory.join('<br>') : 'No transactions yet.';
    document.getElementById('display').innerHTML = `<p>${history}</p>`;
}

function submitTransaction() {
    let amount = parseFloat(document.getElementById('amount').value);
    
    if (isNaN(amount) || amount <= 0) {
        document.getElementById('display').innerHTML = `<p>Invalid amount. Please enter a positive number.</p>`;
        return;
    }
    
    if (action === "deposit") {
        balance += amount;
        document.getElementById('display').innerHTML = `<p>Deposited: ₹${amount}</p>`;
        transactionHistory.push(`Deposited: ₹${amount}`);
    } else if (action === "withdraw") {
        if (amount <= balance) {
            balance -= amount;
            document.getElementById('display').innerHTML = `<p>Withdrew: ₹${amount}</p>`;
            transactionHistory.push(`Withdrew: ₹${amount}`);
        } else {
            document.getElementById('display').innerHTML = `<p>Insufficient funds. Cannot withdraw ₹${amount}</p>`;
        }
    }
    
    document.getElementById('amount').value = '';  // Clear the input field
    document.getElementById('input-section').style.display = 'none';  // Hide input section
}

function exitATM() {
    document.getElementById('display').innerHTML = `<p>Thank you for using the ATM!</p>`;
    transactionHistory.push('Exited ATM');
}
