import os

def track_portfolio():
    # Hardcoded pricing data
    prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "MSFT": 330.0,
        "GOOGL": 140.0
    }
    
    portfolio = {}
    print("Portfolio Tracker Initialized. Type 'DONE' to calculate total.")
    
    while True:
        stock_name = input("Enter stock ticker (e.g., AAPL): ").strip().upper()
        
        if stock_name == 'DONE':
            break
            
        if stock_name not in prices:
            print(f"Error: Ticker '{stock_name}' not found in pricing database.")
            continue
            
        qty_input = input(f"Enter quantity for {stock_name}: ").strip()
        
        # Edge Case Handling: Type checking and negative numbers
        try:
            quantity = float(qty_input)
            if quantity < 0:
                print("Error: Quantity cannot be negative.")
                continue
        except ValueError:
            print("Error: Invalid quantity. Please enter a numerical value.")
            continue
            
        # Accumulate if they enter the same stock twice
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    # Calculation
    total_value = sum(prices[ticker] * qty for ticker, qty in portfolio.items())
    
    print("\n--- Portfolio Summary ---")
    for ticker, qty in portfolio.items():
        value = prices[ticker] * qty
        print(f"{ticker}: {qty} shares @ ${prices[ticker]:.2f} = ${value:.2f}")
    print(f"Total Investment Value: ${total_value:.2f}")
    
    # File I/O: Context managers dictate we use 'with open()'
    save_path = "portfolio_summary.txt"
    with open(save_path, "w") as file:
        file.write(f"Total Investment Value: ${total_value:.2f}\n")
    print(f"Summary saved to {save_path}")

if __name__ == "__main__":
    track_portfolio()
