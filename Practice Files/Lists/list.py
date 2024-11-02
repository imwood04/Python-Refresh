# Lists
# The seats in your ticketing program are stored in a 2D list. Each seat is assigned a letter code.
#
# Complete the program to take the seat row and column as input and output the corresponding code from the list (row and column indices start from 0).
#
# Sample Input
# 3
# 2
#
# Sample Output
# l
seats = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l']
]
row = int(input())
column = int(input())
print(seats[row][column])
