def login():
    username_input = input("Username : ")
    password_input = input("Password : ")
    if username_input == 'admin' and password_input == '1234':
        return True
    else:
        return False

def showMenu():
    print("-----Shop----")
    print("1.VatCalculate")
    print("2.PriceCalculate")

def menuSelect():
    UserSelected = int(input(">>"))
    return UserSelected

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice+(totalPrice*(vat/100))
    return result

def priceCalculate():
    value_1 = int(input("enter first number: "))
    value_2 = int(input("enter second number: "))
    return vatCalculate(value_1 + value_2)

""""""
print(priceCalculate())