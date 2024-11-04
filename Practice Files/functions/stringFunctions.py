# print(", ".join(["spam", "eggs", "ham"]))
# #prints "spam, eggs, ham"
#
# print("Hello ME".replace("ME", "world"))
# #prints "Hello world"
#
# print("This is a sentence.".startswith("This"))
# # prints "True"
#
# print("This is a sentence.".endswith("sentence."))
# # prints "True"
#
# print("This is a sentence.".upper())
# # prints "THIS IS A SENTENCE."
#
# print("AN ALL CAPS SENTENCE".lower())
# #prints "an all caps sentence"
#
# print("spam, eggs, ham".split(", "))
# #prints "['spam', 'eggs', 'ham']"

# Your friend is sending you a text message, however his caps lock is broken and the whole message is in uppercase.
# Noone likes being shouted at, plus uppercase text is hard to read, so you decide to write a program to convert the text to lowercase and output it.
#
# Take a string as input and output it in lowercase.

text = input()
print(text.lower())
