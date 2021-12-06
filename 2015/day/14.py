with open('../input/14.txt') as f:
    reindeers = [[int(word) for word in line.split() if word.isdigit()]
                 for line in f]

time = 2503
print(max((time // (fly + rest)*fly + min(time % (fly + rest), fly)) * speed
          for speed, fly, rest in reindeers))

points = [0]*len(reindeers)
distance = [0]*len(reindeers)
flying = [fly-1 for _, fly, _ in reindeers]
for _ in range(time):
    for reindeer, (speed, fly, rest) in enumerate(reindeers):
        if flying[reindeer] >= 0:
            distance[reindeer] += speed

        elif flying[reindeer] <= -rest:
            flying[reindeer] = fly

        flying[reindeer] -= 1

    max_distance = max(distance)
    for reindeer in range(len(distance)):
        if distance[reindeer] == max_distance:
            points[reindeer] += 1

print(max(points))
