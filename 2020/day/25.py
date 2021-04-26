with open('../input/25.txt') as f:
    me, door = keys = set(map(int, f))

mod = 20201227
loop_size = 1
subject = 7
for loop_size in range(10**10):
    if (public := pow(subject, loop_size, mod)) in keys:
        print(pow(me if public == door else door, loop_size, mod))
        break
