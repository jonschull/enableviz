from vpython import *
from time import clock

N = 10

scene.title = "{} by {} by {} = {} rotating boxes".format(N,N,N,N**3)
##sphere()
##scene.pause()

boxes = []

L = 6
scene.range = L
length = 0.6*L/N
height = 0.4*L/N

for x in range(N):
    for y in range(N):
        for z in range(N):
            b = box(color=vector(x/N,y/N,z/N),
                pos=vector(L*(x/(N-1)-.5),L*(y/(N-1)-.5),L*(z/(N-1)-.5)),
                size=vector(length,height,length))
            boxes.append(b)

t = 0
dt = 0.01
loops = 0
ctime = 0
start = clock()
N = 200

while True:
    if loops == N:
        s = '{:0.1f} millisecond computation per loop'.format(1000*ctime/loops)
        s += '\n{:3.0f} loops per second'.format(loops/(clock()-start))
        scene.caption = s
        ctime = 0
        loops = 0
        start = clock()
    rate(N)
    t += dt
    ct = clock()
    v = length*vector(sin(t), 0, cos(t))
    for b in boxes:
        b.axis = v
    ctime += clock()-ct
    loops += 1
