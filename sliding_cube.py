import pybullet as p
import time

p.connect(p.GUI)

p.setGravity(0,0,-10)
p.setRealTimeSimulation(0)

planeId = p.createCollisionShape(p.GEOM_PLANE)
planeUid = p.createMultiBody(0,planeId,0)
p.changeVisualShape(planeUid,-1,rgbaColor=[1,0.6,0.4,1])

cubeId = p.createCollisionShape(p.GEOM_BOX,halfExtents=[0.5,0.5,0.5])
p.changeVisualShape(cubeId,-1,rgbaColor=[1,0,0,1])
boxUid = p.createMultiBody(1,cubeId,-1)
cid = p.createConstraint(cubeId,-1,-1,-1,p.JOINT_FIXED,[0,0,0],[0,0,0],[0,0,1])

minv = -20
maxv = 20
xs = p.addUserDebugParameter("x",minv,maxv,0)
ys = p.addUserDebugParameter("y",minv,maxv,0)
zs = p.addUserDebugParameter("z",minv,maxv,0)
while 1:
	x = p.readUserDebugParameter(xs)
	y = p.readUserDebugParameter(ys)
	z = p.readUserDebugParameter(zs)
	time.sleep(.001)
	pivot=[x,y,z]
	orn = p.getQuaternionFromEuler([0,0,0])
	p.changeConstraint(cid,pivot,jointChildFrameOrientation=orn, maxForce=50)
	p.stepSimulation()

#p.removeConstraint(cid)
