# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example: prices = [7,1,5,3,6,4]  Return: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.


def buy_and_sell_stock(prices):
    max_sum = 0
    curr_sum = 0

    for i in range(len(prices) - 1):
        curr_sum = curr_sum + prices[i + 1] - prices[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return max_sum


prices = [7, 1, 5, 3, 6, 4]
result = buy_and_sell_stock(prices)
print(result)
