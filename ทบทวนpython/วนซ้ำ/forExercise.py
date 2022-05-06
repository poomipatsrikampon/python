round_input = int(input("Please enter number : "))
sum = 0
for round in range(round_input):
    number_input = int(input("x"+str(round+1)+":"))
    sum += number_input
print(sum)