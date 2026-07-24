"""
Stock Portfolio Tracker
------------------------
A simple stock tracker that calculates total investment value based on
manually defined (hardcoded) stock prices.

Key concepts used: dictionary, input/output, basic arithmetic, file handling.
"""

import csv
from datetime import datetime

# Hardcoded dictionary of stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320,
}


def show_available_stocks():
    print("Available stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print()


def get_portfolio():
    """Prompt the user for stock names and quantities."""
    portfolio = {}

    print("Enter stock symbol and quantity (type 'done' as symbol to finish).\n")

    while True:
        symbol = input("Stock symbol: ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in the price list. Please choose from the available stocks.\n")
            continue

        try:
            quantity = int(input(f"Quantity of {symbol}: ").strip())
            if quantity < 0:
                print("Quantity cannot be negative. Try again.\n")
                continue
        except ValueError:
            print("Please enter a valid whole number for quantity.\n")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} shares of {symbol}.\n")

    return portfolio


def calculate_total(portfolio):
    """Calculate the value of each holding and the total investment."""
    breakdown = {}
    total = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        breakdown[symbol] = value
        total += value

    return breakdown, total


def display_summary(portfolio, breakdown, total):
    print("\n----- Portfolio Summary -----")
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = breakdown[symbol]
        print(f"{symbol}: {quantity} shares x ${price} = ${value}")
    print("------------------------------")
    print(f"Total Investment Value: ${total}\n")


def save_to_file(portfolio, breakdown, total):
    """Optionally save the results to a .txt or .csv file."""
    choice = input("Save results to a file? (y/n): ").lower().strip()

    if choice != "y":
        return

    file_format = input("Choose file format - txt or csv: ").lower().strip()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if file_format == "csv":
        filename = f"portfolio_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Value"])
            for symbol, quantity in portfolio.items():
                writer.writerow([symbol, quantity, STOCK_PRICES[symbol], breakdown[symbol]])
            writer.writerow([])
            writer.writerow(["Total Investment Value", "", "", total])
        print(f"Results saved to {filename}")

    elif file_format == "txt":
        filename = f"portfolio_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("----- Portfolio Summary -----\n")
            for symbol, quantity in portfolio.items():
                price = STOCK_PRICES[symbol]
                value = breakdown[symbol]
                f.write(f"{symbol}: {quantity} shares x ${price} = ${value}\n")
            f.write("------------------------------\n")
            f.write(f"Total Investment Value: ${total}\n")
        print(f"Results saved to {filename}")

    else:
        print("Unrecognized format. Skipping file save.")


def main():
    print("Welcome to the Stock Portfolio Tracker!\n")
    show_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    breakdown, total = calculate_total(portfolio)
    display_summary(portfolio, breakdown, total)
    save_to_file(portfolio, breakdown, total)


if __name__ == "__main__":
    main()
