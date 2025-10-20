# Measure some strings:
grocery_list = {"milk":"first aile","bread":"second aile","hankerchiefs":"third aile","cheese":"fourth aile"}
for food, place in grocery_list.copy().items(): #here we make a copy of the dictionary to iterate over and delete some keys and values
    if place == "fourth aile":
        del grocery_list[food]
        print ("Food items in aile four are too far away.")
print(grocery_list)
        
    