import pybullet as p
import random
p.connect(p.GUI)
p.setGravity(0,0,-0.001)
p.setRealTimeSimulation(0)
objects = {}
def create_snow():
  for i in range(50):
    objects[i] = p.createCollisionShape(p.GEOM_SPHERE)
    p.createMultiBody(random.randint(1,10),objects[i],-1,basePosition=[random.randint(-10,10),random.randint(-10,10),random.randint(2,5)])
    p.changeVisualShape(objects[i],-1,rgbaColor=[random.random(),random.random(),random.random(),1]) #changeVisualShape must come after createMultiBody
for i in range(1000000000):
  p.stepSimulation()
  if i % 100000 == 0: 
    create_snow()
