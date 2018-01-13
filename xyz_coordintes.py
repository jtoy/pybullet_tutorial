import pybullet as p
p.connect(p.GUI)
p.setGravity(0,0,-10)
p.setRealTimeSimulation(0)
p.addUserDebugText(("1,0,0"),[1,0,0]) 
p.addUserDebugText(("-1,0,0"),[-1,0,0]) 
p.addUserDebugText(("0,1,0"),[0,1,0]) 
p.addUserDebugText(("0,-1,0"),[0,-1,0]) 
p.addUserDebugText(("0,0,1"),[0,0,1]) 
p.addUserDebugText(("0,0,-1"),[0,0,-1]) 
p.addUserDebugText(("remember, RGB corresponds to XYZ"),[0,0,-2]) 
while (1):
    p.stepSimulation()
