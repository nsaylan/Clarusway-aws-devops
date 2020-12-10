def buy_and_sell(stock_price):
    max_profit_val, current_max_val = 0, 0 
    for price in reversed(stock_price):                       
        current_max_val = max(current_max_val, price)          
        potential_profit = current_max_val - price          
        max_profit_val = max(potential_profit, max_profit_val)

    return max_profit_val

print(buy_and_sell([75,73,60,100,120,130]))
print(buy_and_sell([10,20,23,22,17,30]))
print(buy_and_sell([1,6,19,59,30,60]))