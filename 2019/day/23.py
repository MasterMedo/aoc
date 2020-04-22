from collections import defaultdict
from threading import Thread
from queue import Queue
from time import sleep
intcode = __import__('9').intcode

def reciever(i):
    yield i
    while True:
        if queue[i].empty():
            yield -1
        else:
            x, y = queue[i].get()
            yield x
            yield y

def run(computer, i):
    global NAT
    for destination in computer:
        package = (x := next(computer), y := next(computer))
        if destination == 255:
            if not NAT:
                print(y) # part 1
            # print(f'{i} sending {package} to NAT')
            NAT = package
            continue
        queue[destination].put(package)
        # print(f'{i} sending {package} to {destination}')

with open('../input/23.txt') as f:
    tape = dict(enumerate(map(int, f.read().split(','))))

queue = [Queue() for _ in range(50)]
last_y = NAT = None
for i in range(50):
    computer = intcode(defaultdict(int, tape), reciever(i))
    t = Thread(target=run, args=(computer, i), daemon=True)
    t.start()

while True:
    if all(q.empty() for q in queue):
        sleep(2)
        if any(not q.empty() for q in queue):
            continue
        if last_y == NAT[1]:
            print(last_y) # part 2
            break
        queue[0].put(NAT)
        last_y = NAT[1]
