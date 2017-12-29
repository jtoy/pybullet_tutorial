import pybullet as p
p.connect(p.GUI)
p.setGravity(0,0,-0.005)
p.setRealTimeSimulation(0)

plane = p.createCollisionShape(p.GEOM_PLANE,planeNormal=[0,0.5,0.5])
planeMBId = p.createMultiBody(0,plane,0,basePosition=[0,0,0])
p.changeVisualShape(plane,-1,rgbaColor=[1,0.6,0.4,1])

sxyz = [-2,-2,3]
sphere = p.createCollisionShape(p.GEOM_SPHERE,halfExtents=[0.5,0.5,0.5])
p.createMultiBody(1,sphere,-1,basePosition=sxyz)
p.changeVisualShape(sphere,-1,rgbaColor=[1,0,0,1])
#scid = p.createConstraint(sphere,-1,-1,-1,p.JOINT_FIXED,[0,0,0],[0,0,0],sxyz)

box = p.createCollisionShape(p.GEOM_BOX,halfExtents=[0.3,0.3,0.3])
p.createMultiBody(1,box,-1,basePosition=[0,0.1,3])
p.changeVisualShape(box,-1,rgbaColor=[1,0,1,1])
#rbscid = p.createConstraint(box,-1,-1,-1,p.JOINT_FIXED,[0,0,0],[0,0,0],[0,0,1])

cylinder = p.createCollisionShape(p.GEOM_SPHERE,halfExtents=[0.5,0.5,0.5])
p.createMultiBody(1,cylinder,-1,basePosition=[0,4,2])
p.changeVisualShape(cylinder,-1,rgbaColor=[1,1,0,1])
#ccid = p.createConstraint(cylinder,-1,-1,-1,p.JOINT_FIXED,[0,0,0],[0,0,0],[0,0,1]) #dont move

cy = p.createCollisionShape(p.GEOM_CYLINDER,height=1,radius=0.1)
xyz=[1,1.98,2]
cymb= p.createMultiBody(1,cy,-1,basePosition=xyz,baseOrientation=[0,1,0,1])
p.changeVisualShape(cy,-1,rgbaColor=[0,1,0,1])

#you must set xyz in both createMultiBody and createConstraint at same time to not get unexpected collision issues
xyz=[1,2,0.4]
cy2 = p.createCollisionShape(p.GEOM_CYLINDER,height=1,radius=0.1)
cymb2= p.createMultiBody(1,cy2,-1,basePosition=xyz,baseOrientation=[0,1,0,1])
p.changeVisualShape(cy2,-1,rgbaColor=[1,1,0,1])
ccid = p.createConstraint(cy2,-1,-1,-1,p.JOINT_FIXED,[0,0,0],[0,0,0],xyz,childFrameOrientation=[0,1,0,1])

while 1:
  p.stepSimulation()
