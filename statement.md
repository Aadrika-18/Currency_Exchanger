# Currency Exchange Program: Project Statement

## Problem Statement

People who travel, study abroad, shop from international websites or deal with foreign payments regularly need to know what an amount in one currency is worth in another. Doing this by hand means finding the exchange rate, multiplying, and rounding the result every time, which is slow and easy to get wrong. Past conversions are also rarely recorded, so people cannot easily look back at what they calculated earlier.

This project addresses the problem by providing a simple command-line program, written in Python, that lets a registered user convert money between popular world currencies quickly and accurately, and keeps a timestamped record of every conversion made during the session.

## Scope of the Project

### In scope

- User registration and login before the converter can be used
- Conversion between six currencies: USD, INR, GBP, EUR, YEN and YUAN (30 currency pairs)
- Predefined, fixed exchange rates stored inside the program
- Display of the converted amount rounded to two decimal places
- In-session conversion history with date and time
- A menu that lets the user convert again, view history or exit
- Clear messages for wrong login details, unsupported currency pairs and invalid menu choices

### Out of scope

- Live or real-time exchange rates from the internet
- Permanent storage of accounts and history (data is lost when the program closes)
- Multiple user accounts (one account per run)
- Password encryption or advanced security
- Graphical user interface (the program runs in the terminal)
- Currencies other than the six listed above

## Target Users

- **Students** learning Python who want a practical example of functions, dictionaries, lists and loops
- **Travellers** who need a quick estimate of money in another currency
- **Casual users** who want a simple tool for everyday conversions without opening a website
- **Instructors and evaluators** reviewing the project as a beginner-level programming assignment

## High-Level Features

- **Registration and login:** access to the converter is protected by a username and password, with retry on failed login
- **Multi-currency conversion:** convert between any two different supported currencies
- **Flexible input:** currency codes are accepted in any letter case
- **Automatic calculation and rounding:** the result is calculated from the stored rate and shown to two decimal places
- **Conversion history:** each successful conversion is saved with the amount, result and timestamp, and can be viewed at any time
- **Repeat and exit options:** the user can make unlimited conversions in one session and exit whenever they choose
- **User-friendly messages:** clear feedback for invalid credentials, unavailable conversions and wrong menu choices
