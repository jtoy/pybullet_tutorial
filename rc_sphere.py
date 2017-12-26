#show how to create and control a sphere on the xy plane
import pybullet as p
import time
import random

p.connect(p.GUI)

p.setGravity(0,0,-10)
p.setRealTimeSimulation(0)

planeId = p.createCollisionShape(p.GEOM_PLANE)
planeUid = p.createMultiBody(0,planeId,0)
p.changeVisualShape(planeUid,-1,rgbaColor=[1,0.6,0.4,1])

cubeId = p.createCollisionShape(p.GEOM_SPHERE,halfExtents=[0.5,0.5,0.5])
p.changeVisualShape(cubeId,-1,rgbaColor=[1,0,0,1])
boxUid = p.createMultiBody(1,cubeId,-1)
cid = p.createConstraint(cubeId,-1,-1,-1,p.JOINT_FIXED,[0,0,0],[0,0,0],[0,0,1])

x,y,z = 0,0,0
while 1:
  keys = p.getKeyboardEvents()
  if len(keys) == 0:
    x += random.uniform(-0.1,0.1)
    y += random.uniform(-0.1,0.1)
  for k in keys:
    print(k)
    if k == 65297: #up
      y+=0.01
    elif k == 65298: #down
      y-=0.01
    elif k == 65295: #left
      x-=0.01
    elif k == 65296: #right
      x+=0.01
    elif 109: #m STOP
      pass
  time.sleep(.001)
  pivot=[x,y,z]
  orn = p.getQuaternionFromEuler([0,0,0])
  p.changeConstraint(cid,pivot,jointChildFrameOrientation=orn, maxForce=50)
  p.stepSimulation()
