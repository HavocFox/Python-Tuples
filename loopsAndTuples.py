stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("AAPL", "2021-01-03", 135.0),
    ("AAPL", "2021-01-04", 134.0),
    ("AAPL", "2021-01-05", 136.0),
    ("MSFT", "2021-01-02", 225.0),
    ("MSFT", "2021-01-03", 230.0),
    ("MSFT", "2021-01-04", 228.0),
    ("AAPL", "2021-01-06", 138.0),
    ("AAPL", "2021-01-07", 136.5),
    ("AAPL", "2021-01-08", 137.8),
    ("MSFT", "2021-01-05", 232.0),
    ("MSFT", "2021-01-06", 235.0),
    ("MSFT", "2021-01-07", 238.0),
]

def find_average(chosen_stock):
    average = 0
    total_of_stock = 0
    total_price = 0
    found = False
    for stock in stock_data:
        if chosen_stock == stock[0]:
            found = True
            total_price = total_price + stock[2]
            total_of_stock = total_of_stock + 1

        else:
            pass
    if found == False:
        print("That stock is not present in the data. ")
    average = total_price / total_of_stock
    print(f'The average closing price of the stock {chosen_stock} was', '$%.2f' % average, ".")
    


while True:
    stock_choice = input("Please enter the stock you would like to find the average closing price for. ")
    find_average(stock_choice)
    end_choice = input("Would you like to compute another stock? Y or N. ").upper()
    if end_choice == 'N':
        break
    else:
        pass
