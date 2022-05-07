
menuList = []
def showBill():

    total = 0
    
    print("----My Food----")
    for list in range(len(menuList)):
        print(menuList[list][0],menuList[list][1],"THB")
        total += menuList[list][1]
    
    print("ราคารวม",total,"THB")

while True:
    menu_name = input("Please enter menu :")
    if menu_name == 'exit':
        break
    else:
        menu_price = int(input("price : "))
        menuList.append([menu_name,menu_price])

showBill()