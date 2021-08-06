groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08,
}

#print(groceries)
#print(groceries["Baby Spinach"])

groceries["Avocado"] = 1.00 #Add an item
del groceries["Bacon"]

for item in groceries:
    print(f"{item}: ${groceries[item]}")

for item,price in groceries.items():
    print(f"{item}: ${price}")

print(groceries)

