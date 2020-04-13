import math
with open('../input/14.txt') as f:
    raindeers = [[int(w) for w in words if w.isdigit()]
                    for raindeer, *words in map(str.split, f)]

time = 2503
print(max((time//(duration+rest)*duration + min(time %(duration+rest),duration)) * speed for speed, duration, rest in raindeers))

points = [0]*len(raindeers)
distance = [0]*len(raindeers)
flying = [duration-1 for _, duration, _ in raindeers]
for i in range(time):
    for raindeer, (speed, duration, rest) in enumerate(raindeers):
        if   flying[raindeer] >= 0:
            distance[raindeer] += speed

        elif flying[raindeer] <= -rest:
            flying[raindeer] = duration

        flying[raindeer] -= 1

    max_distance = max(distance)
    for raindeer in range(len(distance)):
        if distance[raindeer] == max_distance:
            points[raindeer] += 1

print(max(points))
