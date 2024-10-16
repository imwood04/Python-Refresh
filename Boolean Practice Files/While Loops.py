import random

hitMiss = {"miss", "hit"}
hitMiss_list = list(hitMiss)
points = 100
i = 1
while i <= 4:
    hit = random.choice(hitMiss_list)
    if hit == 'miss':
        i = i + 1
        print('miss')
        points = points - 20
    else:
        i = i + 1
        print('hit')
        points = points + 10

print(points)
