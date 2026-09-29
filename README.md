# Currency Exchange Program

## Overview

The Currency Exchange Program is a command-line application written in Python that converts money between six major currencies: USD, INR, GBP, EUR, YEN and YUAN.

Before using the converter, a user must register and log in. After logging in, the user enters the currency they have, the amount, and the currency they want. The program looks up a predefined exchange rate, calculates the converted amount and displays it rounded to two decimal places. Every successful conversion is saved with a date and time, and the user can view this history or make more conversions until they choose to exit.

The project was built to practise core Python concepts: functions, dictionaries, lists, loops, conditionals and the `datetime` module.

## Features

- **User registration and login:** the converter is only accessible after successful login; failed logins can be retried
- **Six supported currencies:** USD, INR, GBP, EUR, YEN, YUAN
- **30 currency pairs:** conversion between any two different supported currencies
- **Case-insensitive input:** `usd`, `Usd` and `USD` are all accepted
- **Conversion history:** each conversion is stored with the amount, result and timestamp
- **Menu-driven loop:** make another conversion, view history, or exit
- **Error messages:** clear messages for invalid login, unsupported currency pairs and invalid menu choices

### Supported Currencies

| Code | Currency |
|------|----------|
| USD | US Dollar |
| INR | Indian Rupee |
| GBP | British Pound |
| EUR | Euro |
| YEN | Japanese Yen |
| YUAN | Chinese Yuan |

## Technologies / Tools Used

| Tool | Purpose |
|------|---------|
| Python 3.6+ | Programming language |
| `datetime` module (standard library) | Timestamps for conversion history |
| Terminal / Command Prompt | Running the program |
| VS Code / IDLE / any text editor | Writing and editing the code (any editor works) |
| Git and GitHub (optional) | Version control and sharing |

No external libraries or `pip install` steps are needed.

## Steps to Install & Run

### 1. Install Python

Download Python 3.6 or later from [python.org](https://www.python.org/downloads/). During installation on Windows, tick **"Add Python to PATH"**.

Check the installation:

```bash
python --version
```


### 2. Get the project

Either download the file directly, or clone the repository:

```bash
git clone https://github.com/Aadrika-18/Currency_Exchanger
cd  Currency_Exchanger
```

Make sure the program file is named `currency_converter.py`.

### 3. Run the program

Open a terminal in the project folder and run:

```bash
python currency_converter.py
```

### 4. Use the program

1. Register with a username and password.
2. Log in with the same details.
3. Enter the currency you have, the amount, and the currency you want.
4. Choose from the menu: `1` convert again, `2` view history, `3` exit.

## Instructions for Testing

The program is tested manually by running it and entering the inputs below. Complete registration and login first (for example, username `test` and password `1234`).

### Test Cases

| # | Test | Input | Expected Output |
|---|------|-------|-----------------|
| 1 | Successful login | Correct username and password | `Login successful!` |
| 2 | Failed login | Wrong password | `Invalid username or password.`, then login is asked again |
| 3 | USD to INR | `USD`, `100`, `INR` | `Converted amount = 8800.0 INR` |
| 4 | INR to USD | `INR`, `1000`, `USD` | `Converted amount = 11.36 USD` |
| 5 | EUR to GBP | `EUR`, `50`, `GBP` | `Converted amount = 44.0 GBP` |
| 6 | GBP to YEN | `GBP`, `100`, `YEN` | `Converted amount = 19300.0 YEN` |
| 7 | Lowercase input | `usd`, `10`, `inr` | `Converted amount = 880.0 INR` |
| 8 | Unsupported currency | `USD`, `100`, `ABC` | `Currency conversion not available.` |
| 9 | Same currency | `USD`, `100`, `USD` | `Currency conversion not available.` |
| 10 | History with records | After tests 3 to 5, choose `2` | Three numbered records with date and time |
| 11 | History when empty | Choose `2` before any successful conversion | `No conversion history available.` |
| 12 | Invalid menu choice | Enter `9` at the menu | `Invalid choice. Please try again.` |
| 13 | Exit | Choose `3` | `Thank you for using Currency Converter!` and the program ends |

### Testing with piped input (optional)

You can run the whole flow at once by feeding inputs from the terminal. On Linux or macOS:

```bash
printf "test\n1234\ntest\n1234\nUSD\n100\nINR\n2\n3\n" | python3 currency_converter.py
```

### Known limitation

Entering text instead of a number for the amount (for example `abc`) crashes the program with a `ValueError`. This can be fixed by wrapping `float(input(...))` in a `try / except` block.

### Sample Output

```
======================================
       CURRENCY EXCHANGE PROGRAM
======================================

--------- Registration ---------
Create username = test
Create password = 1234
Registration successful!
Please login to continue.

--------- Login ---------
Enter username = test
Enter password = 1234
Login successful!

Welcome to Currency Converter!

Available currencies are
USD - US Dollar
INR - Indian Rupee
GBP - British Pound
EUR - Euro
YEN - Japanese Yen
YUAN - Chinese Yuan
Enter the currency which you have with you = usd
Enter the amount = 100
Enter the currency which you want = inr
Converted amount = 8800.0 INR

What do you want to do?
1. Make another conversion
2. Show conversion history
3. Exit
Enter your choice = 2

--------- Conversion History ---------
1 . 100.0 USD = 8800.0 INR | 29-09-2026 14:30

What do you want to do?
1. Make another conversion
2. Show conversion history
3. Exit
Enter your choice = 3

Thank you for using Currency Converter!
```

## Project Structure

```
project-folder/
├── currency_converter.py
├── README.md
└── screenshots/        (optional)
```

## Limitations and Future Improvements

- Exchange rates are fixed in the code; live rates could be fetched from an API
- Account and history are stored only in memory and are lost when the program closes
- Passwords are stored as plain text; hashing (for example `hashlib`) would be safer
- Only one account can be registered per run
- Amount input needs `try / except` validation
- A GUI (Tkinter) could replace the command-line interface
