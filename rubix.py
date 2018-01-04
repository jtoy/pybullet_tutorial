import pybullet as p
import time
import random
p.connect(p.GUI)
p.setGravity(0,0,-10)
p.setRealTimeSimulation(0)
colors = [[0.98,0.41,0.12],[0.70,0,0],[1,1,0],[0,0,1],[0,0.64,0.37], [1,1,1]]
for x in range(-1,2):
    for y in range(-1,2):
        for z in range(-1,2):
            xyz = [x*2,y*2,z*2]
            cube = p.createCollisionShape(p.GEOM_BOX,halfExtents=[0.2,0.2,0.2])
            cubeMB = p.createMultiBody(1,cube,-1,basePosition=xyz)
            cuid = p.createConstraint(cube,-1,-1,-1,p.JOINT_FIXED,[0,0,0],[0,0,0],xyz)
            color = random.choice(colors)
            p.changeVisualShape(cube,-1,rgbaColor=[color[0],color[1],color[2],1])
            p.changeConstraint(cuid,[0,0,0], maxForce=20) #maxForce can only be applied in changeConstraint

while 1:
    time.sleep(0.001)
    p.stepSimulation()

