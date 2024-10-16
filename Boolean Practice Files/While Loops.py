import random

points = 100
i = 1
while i <= 4:
    random_number = random.randint(1,4)
    if random_number == 4:
        i = i + 1
        print('miss')
        points = points - 20
    else:
        i = i + 1
        print('hit')
        points = points + 10

print(points)