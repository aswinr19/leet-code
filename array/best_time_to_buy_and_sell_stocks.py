# Best Time to Buy and Sell Stocks (121, array, easy)

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a
# different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any
# profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def maxProfit(prices):

    lowest = prices[0]
    lowestIndex = 0
    highestProfit = 0

    for i in range(1, len(prices)):
        highest = 0

        if prices[i] < lowest and i != (len(prices) -1):
            lowest = prices[i]
            lowestIndex = i

        for j in range(lowestIndex, len(prices)):
            if prices[j] > highest and prices[j] > lowest:
                highest = prices[j]

        if highest - lowest > 0 and (highest - lowest ) > highestProfit :
            highestProfit = (highest - lowest)

    return highestProfit
