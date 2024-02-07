# List is a flexible data structure in which items can be added and deleted easily

shopping = ["Bread", "Coffee", "Sugar"]

# print(shopping) -> print the list as ["Bread", "Coffee", "Sugar"]

# adding an item at the end of the list
shopping.append("Curd")

for items in shopping:
    print(items)

# manipulation in the list
shopping[1] = "Oil"
print("not buying coffee and now buying" ,shopping[1])

shopping.append("Shampoo")

# insert an item at a given index 
shopping.insert(2, "Peanut Butter")

for items in shopping:
    print(items)

# function for finns the length of the list 
print(len(shopping))