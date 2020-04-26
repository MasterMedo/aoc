def split_every_n(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

with open('../input/8.txt') as f:
    images = split_every_n(list(map(int, f.read()[:-1])), 25*6)

image = min(images, key=lambda image: image.count(0))
print(image.count(1) * image.count(2))

image = ''.join('#' if next(pixel for pixel in layer if pixel != 2) else ' '
                for layer in zip(*images))

print('\n'.join(split_every_n(image, 25)))
