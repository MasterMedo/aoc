with open('../input/14.txt') as f:
    raindeers = [[int(word) for word in line.split() if word.isdigit()]
                 for line in f]

time = 2503
print(max((time // (fly + rest)*fly + min(time % (fly + rest), fly)) * speed
          for speed, fly, rest in raindeers))

points = [0]*len(raindeers)
distance = [0]*len(raindeers)
flying = [fly-1 for _, fly, _ in raindeers]
for _ in range(time):
    for raindeer, (speed, fly, rest) in enumerate(raindeers):
        if flying[raindeer] >= 0:
            distance[raindeer] += speed

        elif flying[raindeer] <= -rest:
            flying[raindeer] = fly

        flying[raindeer] -= 1

    max_distance = max(distance)
    for raindeer in range(len(distance)):
        if distance[raindeer] == max_distance:
            points[raindeer] += 1

print(max(points))
