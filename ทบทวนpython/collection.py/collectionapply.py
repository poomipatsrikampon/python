system_menu = {'ข้าวหมกไก่':80,'ข้าวมันไก่':70,'ข้าวมันไก่ผสม':100}

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
        menuList.append([menu_name,system_menu[menu_name]])

showBill()