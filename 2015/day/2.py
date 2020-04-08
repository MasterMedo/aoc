with open("../input/2.txt") as f:
  edges = [list(map(int, line.split('x'))) for line in f.readlines()]

print(sum(2 * (x*y + y*z + z*x) + min(x*y, y*z, z*x) for x, y, z in edges))
print(sum(2 * sum(sorted([x, y, z])[:2]) + x*y*z for x, y, z in edges))
