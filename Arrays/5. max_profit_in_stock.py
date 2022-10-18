''' Find the maximum profit that can be obtained from buying and then selling the stocks
from the list of stock price represented in a list in a daywise format '''

def find_max_profit(arr):
    min_price = float('inf')
    max_profit = 0

    for i in range(len(arr)):
        if arr[i] < min_price:
            min_price = arr[i]
        elif arr[i] - min_price > max_profit:
            max_profit = arr[i] - min_price
    return  max_profit        


stock_prices = [7,7,6,3,5,4,9]
max_profit = find_max_profit(stock_prices)
print(max_profit)
