from django.forms import PasswordInput


user_name = input("Username : ")
password = input("Password : ")
if user_name == 'admin' and password == '12345':
    print("Welcome to arm shop")
    print("----Product List---")
    print("1.Apple 30 THB / 1 ")
    print("2.Coconut 20 THB / 1")
    print("3.Banana 15 THB / 1")
    select_product = input("Select Your Product (please type number of product) : ")
    if select_product == '1':
        print("Apple 30 THB / 1")
        quantity = int(input("Quantity : "))
        print("Apple 30 THB *",quantity,)
        print("Total Price = ",30*quantity,"THB")
    elif select_product == '2':
        print("2.Coconut 20 THB / 1")
        quantity = int(input("Quantity : "))
        print("Coconut 20 THB *",quantity,)
        print("Total Price = ",20*quantity,"THB")
    elif select_product == '3':
        print("3.Banana 15 THB / 1")
        quantity = int(input("Quantity : "))
        print("Banana 15 THB *",quantity,)
        print("Total Price = ",15*quantity,"THB")
    else:
        print("please enter product number")
else:
    print("Username of Password Incorrect")