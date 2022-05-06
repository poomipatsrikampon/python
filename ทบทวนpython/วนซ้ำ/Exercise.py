"""
input           output
5                *
                ***
               *****
              *******
             *********

row = input = 5
left_space = [4,3,2,1,0] = right_space
"*" = [1,3,5,7,9]
"""
row = int(input("Enter number : "))
for space in range(row):
    row -= 1
    star = 2*(space + 1) - 1
    print(" "*row,"*"*star)

    
