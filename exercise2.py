# Exercise 2
# The list, prices[1] is used for stock.
prices = {
    "banana": [4, 3],
    "apple": [2, 0],
    "orange": [1.5, 1],
    "pear": [3, 2],
}

for x, k in prices.items():
    print(x)
    print("price: ", k[0])
    print("stock: ", k[1], "\n")

total = 0
for x, k in prices.items():
    print("Stock x Price for", x, ": ", k[0] * k[1])
    total += k[0] * k[1]
print("Total: ", total)
