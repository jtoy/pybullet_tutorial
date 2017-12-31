import pybullet as p
p.connect(p.GUI)

p.setRealTimeSimulation(0)
for x in range(-3,3):
  for y in range(-3,3):
    for z in range(-3,3):
      p.addUserDebugText(("x "+str(x)+" y "+str(y)+ " z "+str(z) ),[x,y,z])
while (1):
  p.stepSimulation()
