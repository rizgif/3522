#https://book.pythontips.com/en/latest/map_filter.html
print("Squaring a list of number using a for loop and two lists")
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
print(squared)

print("\nPerform same operation as above, but using filter and map")
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)