# Write a function that takes a string and a letter as its arguments and returns the count of the letter in the string.
#
# Sample Input
# hello, how are you?
# o
#
# Sample Output
# 3
#
# Explanation: The letter o appears 3 times in the given text.

def letter_count(text, letter):
    count = 0
    for character in text:
        if character == letter:
            count += 1
    return count


text = input()
letter = input()

print(letter_count(text, letter))
