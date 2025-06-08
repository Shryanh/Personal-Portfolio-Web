import yfinance as yf
from tabulate import tabulate


portfolio = {}

def add_stock(symbol, shares):
    if symbol in portfolio:
        portfolio[symbol] += shares
    else:
        portfolio[symbol] = shares
    print(f"✅ Added {shares} shares of {symbol}")

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"🗑️ Removed {symbol} from portfolio")
    else:
        print("❌ Stock not found in portfolio")

def view_portfolio():
    if not portfolio:
        print("⚠️ Portfolio is empty.")
        return

    total_value = 0
    table = []
    for symbol, shares in portfolio.items():
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        price = data['Close'][0]
        value = price * shares
        total_value += value
        table.append([symbol, shares, f"${price:.2f}", f"${value:.2f}"])
    
    print(tabulate(table, headers=["Symbol", "Shares", "Price", "Total Value"], tablefmt="fancy_grid"))
    print(f"\n💰 Portfolio Total Value: ${total_value:.2f}")

def main():
    while True:
        print("\n📊 Stock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol)
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            print("👋 Exiting Portfolio Tracker.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
