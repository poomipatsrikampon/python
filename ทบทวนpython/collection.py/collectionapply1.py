menuList = []
priceList = []

def showBill():
    print("----My Food----")
    for list in range(len(menuList)):
        print(menuList[list],priceList[list])
    total = sum(priceList)
    print("ราคารวม",total,"THB")

while True:
    menu_name = input("Please enter menu :")
    if menu_name == 'exit':
        break
    else:
        menu_price = int(input("price : "))
        menuList.append(menu_name)
        priceList.append(menu_price)

showBill()