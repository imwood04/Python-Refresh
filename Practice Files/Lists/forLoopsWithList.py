# You’re making a shopping cart program.
#
# The shopping cart is declared as a list of prices, and you need to add functionality to apply a discount and output the total price.
#
# Take the discount percentage as input, calculate and output the total price for the shopping cart.
#
# Use a for loop to iterate over the list.
# Use the following formula to calculate the result of X% discount on $Y price: Y - (Y*X/100)

cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
price = 0
total = 0
i = 0
cartNum = 0

while i < len(cart):
    cartNum += cart[i]
    i = i + 1
else:
    pass

total = cartNum - (cartNum * discount / 100)

print(total)