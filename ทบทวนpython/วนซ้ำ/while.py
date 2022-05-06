"""
ทำงานไปเรื่อยๆตราบใดที่ค่าความจริง เป็น จริง
"""
correct_number = 17
user_guess = 0
while user_guess != correct_number:
    user_guess = int(input("please guess a number : "))
    if user_guess > correct_number:
        print("Too Large")
    elif user_guess < correct_number:
        print("Too small")
    elif user_guess == correct_number:
        print("Correct !!")
    

