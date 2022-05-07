from unicodedata import name


name = input("first name : ").capitalize()
last_name = input("last name :").capitalize()
print("Hello ! %s %s"%(name,last_name))

text = "arm"
text_format = "Welcome %s"%(name)
print(text_format.center(20,"-"))
print(len(name))