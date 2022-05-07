def vatCalculate(total_price):
    return total_price+(total_price*(7/100))

price = int(input("enter price : "))

print(vatCalculate(price))