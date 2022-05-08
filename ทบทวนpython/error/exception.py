import sys

randon_list = ['a', 0, 2]

for entry in randon_list:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry")