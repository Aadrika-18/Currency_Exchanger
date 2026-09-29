from datetime import datetime

history = []

# Registration function
def registration():

    print("\n--------- Registration ---------")

    username = input("Create username = ")
    password = input("Create password = ")

    print("Registration successful!")
    print("Please login to continue.")

    return username, password


# Login function
def login(username, password):

    print("\n--------- Login ---------")

    entered_username = input("Enter username = ")
    entered_password = input("Enter password = ")

    if entered_username == username and entered_password == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False


def initial_currency():

    i = input(
        'Enter the currency which you have with you = '
    ).upper()

    return i


def currencies():

    print('\nAvailable currencies are')
    print('USD - US Dollar')
    print('INR - Indian Rupee')
    print('GBP - British Pound')
    print('EUR - Euro')
    print('YEN - Japanese Yen')
    print('YUAN - Chinese Yuan')


def get_amount():

    amount = float(input('Enter the amount = '))

    return amount


def end_currency():

    n = input(
        'Enter the currency which you want = '
    ).upper()

    return n


def exchange_rates(i, n):

    rates = {

        ("USD", "INR"): 88.0,
        ("USD", "EUR"): 0.85,
        ("USD", "GBP"): 0.75,
        ("USD", "YEN"): 144.26,
        ("USD", "YUAN"): 7.00,

        ("INR", "USD"): 0.01136,
        ("INR", "EUR"): 0.00966,
        ("INR", "GBP"): 0.00847,
        ("INR", "YEN"): 1.64,
        ("INR", "YUAN"): 0.0699,

        ("EUR", "USD"): 1.18,
        ("EUR", "INR"): 103.0,
        ("EUR", "GBP"): 0.88,
        ("EUR", "YEN"): 169.72,
        ("EUR", "YUAN"): 8.24,

        ("GBP", "USD"): 1.33,
        ("GBP", "INR"): 118.0,
        ("GBP", "EUR"): 1.14,
        ("GBP", "YEN"): 193.0,
        ("GBP", "YUAN"): 9.37,

        ("YEN", "USD"): 0.00693,
        ("YEN", "INR"): 0.61,
        ("YEN", "EUR"): 0.00589,
        ("YEN", "GBP"): 0.00518,
        ("YEN", "YUAN"): 0.0485,

        ("YUAN", "USD"): 0.1429,
        ("YUAN", "INR"): 14.30,
        ("YUAN", "EUR"): 0.1214,
        ("YUAN", "GBP"): 0.1067,
        ("YUAN", "YEN"): 20.61
    }

    return rates.get((i, n))


def converter(amount, rate):

    result = amount * rate

    return result


def result(result, i):

    print(
        'Converted amount =',
        round(result, 2),
        i
    )


# Store conversion history
def conversion_history(i, n, amount, converted):

    date_time = datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )

    record = (
        str(amount) + " " + i +
        " = " +
        str(round(converted, 2)) +
        " " + n +
        " | " +
        date_time
    )

    history.append(record)


# Display conversion history
def show_history():

    print("\n--------- Conversion History ---------")

    if len(history) == 0:

        print("No conversion history available.")

    else:

        for x in range(len(history)):

            print(
                x + 1,
                ".",
                history[x]
            )


# Repeat conversion function
def repeat_conversion():

    while True:

        print("\nWhat do you want to do?")
        print("1. Make another conversion")
        print("2. Show conversion history")
        print("3. Exit")

        choice = input(
            "Enter your choice = "
        )

        if choice == "1":

            return True

        elif choice == "2":

            show_history()

        elif choice == "3":

            return False

        else:

            print(
                "Invalid choice. Please try again."
            )


def main():

    print("======================================")
    print("       CURRENCY EXCHANGE PROGRAM")
    print("======================================")

    # Registration
    username, password = registration()

    # Login loop
    while True:

        if login(username, password):
            break

        print("Please try logging in again.")

    print("\nWelcome to Currency Converter!")

    # Currency conversion loop
    while True:

        currencies()

        i = initial_currency()

        amount = get_amount()

        n = end_currency()

        rate = exchange_rates(i, n)

        if rate is None:

            print(
                "Currency conversion not available."
            )

        else:

            converted = converter(
                amount,
                rate
            )

            result(
                converted,
                n
            )

            conversion_history(
                i,
                n,
                amount,
                converted
            )

        if not repeat_conversion():

            print(
                "\nThank you for using "
                "Currency Converter!"
            )

            break


main()