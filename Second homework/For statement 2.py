grocery_list = {"milk":"first aile","bread":"second aile","hankerchiefs":"third aile","cheese":"fourth aile"}
modified_grocery_list = {} 
for food, place in grocery_list.items():
    if place != "fourth aile":
        modified_grocery_list[food] = place
    else:
        print ("The",food,"is aile four and therefore too far away.")
print(modified_grocery_list)