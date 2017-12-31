import pybullet as p
import random
import time
p.connect(p.GUI)

p.setRealTimeSimulation(0)
p.addUserDebugText("x 3 y 3",[3,3,0])
moves = ["cameraDistance","cameraYaw","cameraPitch"]
step =0.0001
move = None
counter = 0

xyz= [ 0,2,0]
o=[0,1,0,1]
cy = p.createCollisionShape(p.GEOM_CYLINDER,radius=0.3)
cymb = p.createMultiBody(1,cy,-1,basePosition=xyz,baseOrientation=o)
p.changeVisualShape(cy,-1,rgbaColor=[1,0,0,1])
cid = p.createConstraint(cy,-1,-1,-1,p.JOINT_FIXED,[0,0,0],[0,0,0],xyz,childFrameOrientation=o)
while (1):
  p.stepSimulation()
  cam = p.getDebugVisualizerCamera()
  if counter %400==0:
    counter = 0
    move = random.choice(moves)
  if move == "cameraDistance":
    p.resetDebugVisualizerCamera(cameraDistance=cam[10]+step,cameraYaw=cam[8],cameraPitch=cam[9],cameraTargetPosition=cam[11])
  elif move == "cameraYaw":
    p.resetDebugVisualizerCamera(cameraDistance=cam[10],cameraYaw=cam[8]+step,cameraPitch=cam[9],cameraTargetPosition=cam[11])
  elif move == "cameraPitch":
    p.resetDebugVisualizerCamera(cameraDistance=cam[10],cameraYaw=cam[8],cameraPitch=cam[9]+step,cameraTargetPosition=cam[11])
  counter += 1
