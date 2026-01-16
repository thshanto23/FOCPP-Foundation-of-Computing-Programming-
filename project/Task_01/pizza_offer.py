# Beckett Pizza Plaza 4-for-3 Offer Program
# Author: Tanvir Hasan Shanto
# This program calculates the total price for 4 pizzas
# applying the "Four-for-Three" discount.

import sys

# Function to read pizza prices from a file if provided
def read_prices_from_file(filename):
    prices = []
    try:
        with open(filename, 'r') as file:
            # Read each line, convert to float
            for line in file:
                line = line.strip()  # remove whitespace
                if line:  # skip empty lines
                    price = float(line)
                    if price <= 0:
                        print(f"Invalid price in file: {price}")
                        continue
                    prices.append(price)
        return prices
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except ValueError:
        print("File contains invalid data. Make sure all lines are numbers.")
        return []

# Function to get pizza prices from user input
def get_pizza_prices():
    prices = []
    for i in range(1, 5):
        while True:
            try:
                price_input = input(f"Enter Price of Pizza #{i}: ")
                price = float(price_input)
                if price <= 0:
                    print("Please enter a valid price!")
                    continue
                prices.append(price)
                break
            except ValueError:
                print("Please enter a valid price!")
    return prices

# Function to calculate total price and discount
def calculate_total(prices):
    # Sort prices from lowest to highest
    sorted_prices = sorted(prices)
    # Discount = cheapest pizza
    discount = sorted_prices[0]
    # Total = sum of all prices minus discount
    total = sum(prices) - discount
    # Discount percentage
    discount_percent = (discount / sum(prices)) * 100
    return total, discount_percent

# Main program
def main():
    print("Beckett Pizza Plaza 4-for-3 Offer")
    print("=================================\n")

    # Check if a file is provided as command line argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        prices = read_prices_from_file(filename)
        if len(prices) < 4:
            print("Not enough valid prices in file. Switching to manual input.")
            prices = get_pizza_prices()
        elif len(prices) > 4:
            prices = prices[:4]  # Take first 4 prices only
    else:
        prices = get_pizza_prices()

    # Calculate total and discount
    total, discount_percent = calculate_total(prices)

    # Display results
    print(f"\nOrder Total is £{total:.2f}, a fabulous discount of {discount_percent:.0f}%!")

# Entry point
if __name__ == "__main__":
    main()
