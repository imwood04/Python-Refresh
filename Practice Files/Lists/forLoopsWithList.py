# You’re making a shopping cart program.
#
# The shopping cart is declared as a list of prices, and you need to add functionality to apply a discount and output the total price.
#
# Take the discount percentage as input, calculate and output the total price for the shopping cart.
#
# Use a for loop to iterate over the list.
# Use the following formula to calculate the result of X% discount on $Y price: Y - (Y*X/100)

cart = [15, 42, 120, 9, 5, 380]

###########################################################################
# Remembered this was a thing after doing everything else to get the sum
# cartPrice = sum(cart)
# Could of just uses cartPrice and used the formula with the input for the discount to get the total rather than adding everything up
###########################################################################
# Another thing I see I could have done better was doing for x in cart rather than looping threw with i and checking to make sure it's not over the limit of things inside
###########################################################################
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
