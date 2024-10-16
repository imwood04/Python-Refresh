ticketPrice = 100
total = 0
i = 5

while i >= 1:
    age = int(input())
    if age >= 4:
        total += ticketPrice
        i -= 1
    elif age <= 3:
        i -= 1
        continue

print(total)