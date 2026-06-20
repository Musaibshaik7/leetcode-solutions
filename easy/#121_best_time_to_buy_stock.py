prices=[7,1,5,3,6,4]
min_prices=prices[0]
max_profit=0
for price in prices:
    if price<min_prices:
        min_prices=price
    profit=price-min_prices
    if(profit>max_profit):
        max_profit=profit
print(max_profit)