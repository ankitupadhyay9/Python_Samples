'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5
max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0
In this case, no transaction is done, i.e. max profit = 0.

'''
#Brute Force O(n*n)
def max_profit(arr):
  buy_price = 0
  sell_price = 0
  profit = 0
  for i in range(len(arr)):
    buy_price = arr[i]
    print "buy_price: " + str(buy_price)
    print "i:" + str(i)
    for j in range(i+1, len(arr)):
      print "j:" + str(j)
      if arr[j] > arr[i]:
        sell_price = arr[j]
        print "sell_price: " + str(sell_price)
        if profit < (arr[j] - arr[i]):
          profit = sell_price - buy_price
        print "profit" + str(profit)
  return profit

arr1 = [7, 6, 4, 3, 1]
print max_profit(arr1)

##Another approach O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = 999999999        
        profit = 0
        for i in range(len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            elif prices[i] - buy_price > profit:
                profit = prices[i] - buy_price
        return profit