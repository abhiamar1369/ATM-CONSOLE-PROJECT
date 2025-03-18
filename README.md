# ATM System Simulation in Python

This is a simple ATM-like system built in Python that allows users to perform various actions such as withdrawal, deposit, balance inquiry, PIN generation, and viewing mini statements. The system uses a dictionary to store user account details, and the users interact with it through a text-based interface.

## Features

- **Withdrawal**: Users can withdraw money from their accounts (if the correct PIN is entered and sufficient funds are available).
- **Deposit**: Users can deposit money into their accounts.
- **Check Balance**: Users can check their current account balance.
- **PIN Generation**: Users can generate or change their PIN (if it hasn't been set already).
- **Mini Statement**: Users can view their account details, including their name, date of birth, and account balance.

## How It Works

1. **Accounts**: The system has a predefined set of accounts with account numbers, user names, dates of birth, balances, and PINs. Some accounts don't have a PIN set initially.
2. **Interaction**: The system offers a menu with multiple options. Users can choose an option by entering the corresponding number.
3. **PIN Security**: PINs are required for actions like withdrawals and balance checks to simulate a secure ATM experience.
4. **Continuous Operation**: The system runs in a loop, allowing users to perform multiple actions until they choose to exit.

## Example Options
- **1. WITHDRAWAL**: Enter account number and PIN to withdraw money from the account.
- **2. DEPOSIT**: Enter account number to deposit money into the account.
- **3. REMAINING BALANCE**: View the current account balance.
- **4. PIN GENERATION**: Set or change the PIN for an account.
- **5. MINI STATEMENT**: View the account details, including name, date of birth, and balance.
- **6. EXIT**: Exit the program.

## Requirements

- Python 3.x or higher.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/atm-system.git
