import pybullet as p
import time
import random
import numpy as np
p.connect(p.GUI)
p.setGravity(0,0,-10)
start_co = 0
end_co = 2
p.setRealTimeSimulation(0)
for x in range(start_co,end_co):
  for y in range(start_co,end_co):
    for z in range(start_co,end_co):
      xyz = [x,y,z]
      cube = p.createCollisionShape(p.GEOM_BOX,halfExtents=[0.2,0.2,0.2])
      cubeMB = p.createMultiBody(1,cube,-1,basePosition=xyz)
      cuid = p.createConstraint(cube,-1,-1,-1,p.JOINT_FIXED,[0,0,0],[0,0,0],xyz)
      p.changeVisualShape(cube,-1,rgbaColor=[random.random(),random.random(),random.random(),1])
      p.changeConstraint(cuid,xyz, maxForce=50) #maxForce can only be applied in changeConstraint

xyz=[1,1,0]
o=[0,1,0,1]
cyl = p.createCollisionShape(p.GEOM_CYLINDER,radius=0.2,height=0.1)
cylmb = p.createMultiBody(1,cyl,-1,basePosition=xyz,baseOrientation=o)
p.changeVisualShape(cyl,-1,rgbaColor=[1,0,0,1])
cid = p.createConstraint(cyl,-1,-1,-1,p.JOINT_FIXED,[0,0,0],[0,0,0],xyz,childFrameOrientation=o)
p.changeConstraint(cid,xyz,jointChildFrameOrientation=o, maxForce=50) #maxForce can only be applied in changeConstraint

aspect = 1
camTargetPos = [0,0,0]
yaw = 40
pitch = 10.0
roll=0
upAxisIndex = 2
camDistance = 4
pixelWidth = 320
pixelHeight = 240
nearPlane = 0.0001
farPlane = 0.022
lightDirection = [0,1,0]
lightColor = [1,1,1]#optional
fov = 50  #10 or 50
minmaxv = 20
adp = p.addUserDebugParameter("a",0,2,1)
upadp = p.addUserDebugParameter("upa",0,2,2)
xs = p.addUserDebugParameter("x",-minmaxv,minmaxv,xyz[0])
ys = p.addUserDebugParameter("y",-minmaxv,minmaxv,xyz[1])
zs = p.addUserDebugParameter("z",-minmaxv,minmaxv,xyz[2])
xos = p.addUserDebugParameter("xo",0,1,0)
yos = p.addUserDebugParameter("yo",0,1,1)
zos = p.addUserDebugParameter("zo",0,1,0)
wos = p.addUserDebugParameter("wo",0,1,1)
offsets = p.addUserDebugParameter("offset",-5,5,0.02)
pms = p.addUserDebugParameter("plusminus 0- 1+",0,1,1)
step = 0
texts = []
while 1:
  step +=1
  x = p.readUserDebugParameter(xs)
  y = p.readUserDebugParameter(ys)
  z = p.readUserDebugParameter(zs)
  xo = p.readUserDebugParameter(xos)
  yo = p.readUserDebugParameter(yos)
  zo = p.readUserDebugParameter(zos)
  wo = p.readUserDebugParameter(wos)
  o = [xo,yo,zo,wo]
  xyz = [x,y,z]
  p.changeConstraint(cid,xyz,jointChildFrameOrientation=o, maxForce=100) #maxForce can only be applied in changeConstraint
  offset = 0.02
  offset = p.readUserDebugParameter(offsets)
  link_state = p.getBasePositionAndOrientation(cyl)
  if step%50==0:
    print("orientation"+str(np.around(link_state[1],2)))
    print("xyz"+str(np.around(link_state[0],2)))
  link_p = link_state[0]
  link_o = link_state[1]
  handmat = p.getMatrixFromQuaternion(link_o)

  axisX = [handmat[0],handmat[3],handmat[6]]
  axisY = [-handmat[1],-handmat[4],-handmat[7]] # Negative Y axis
  axisZ = [handmat[2],handmat[5],handmat[8]]
  axiss = [axisX,axisY,axisZ]
  if step %100 == 0:
    if len(texts) != 0:
      for i in texts:
        p.removeUserDebugItem(i)
      texts = []
      #p.removeUserDebugItem(yt)
      #p.removeUserDebugItem(zt)
    texts.append(p.addUserDebugText(("axisx"+str(np.around(axisX,3)) ),axisX))
    texts.append(p.addUserDebugText(("axisy"+str(np.around(axisY,3)) ),axisY))
    texts.append(p.addUserDebugText(("axisz"+str(np.around(axisZ,3)) ),axisZ))
    texts.append(p.addUserDebugText(("linkp"+str(np.around(link_p,3)) ),link_p))
  a = 2
  a = int(p.readUserDebugParameter(adp))
  upa = int(p.readUserDebugParameter(upadp))
  up = axiss[upa] # Up is Z axis

  l = 1.2
  def pm(v1,v2,v):
    if v == 0:
      return v1 -v2
    else:
      return v1 +v2
  v = int(p.readUserDebugParameter(pms))
  eye_pos    = [pm(link_p[0],offset*axiss[a][0],v),pm(link_p[1],offset*axiss[a][1],v),pm(link_p[2],offset*axiss[a][2],v)]
  #eye_pos    = [link_p[0],offset*axiss[a][0],link_p[1]+offset*axiss[a][1],link_p[2]+offset*axiss[a][2]]
  target_pos = [pm(link_p[0],axiss[a][0],v),pm(link_p[1],axiss[a][1],v),pm(link_p[2],axiss[a][2],v)] # target position based by axisY, not X
  #target_pos = [link_p[0]+axiss[a][0],link_p[1]+axiss[a][1],link_p[2]+axiss[a][2]] # target position based by axisY, not X
  #target_pos = [link_p[0]-l,link_p[1]+y*axiss[2][1],link_p[2]+z*axisY[2]] # target position based by axisY, not X
  viewMatrix = p.computeViewMatrix(eye_pos,target_pos,up)
  p.addUserDebugLine(link_p,[link_p[0]-0.1*axiss[a][0],link_p[1]-0.1*axiss[a][1],link_p[2]-0.1*axiss[a][2]],[1,0,0],2,0.2)
  #p.addUserDebugLine(link_p,[link_p[0]-l-x,link_p[1]+y*axiss[a][1],link_p[2]+z*axiss[a][2]],[1,0,0],2,0.2)
  projectionMatrix = p.computeProjectionMatrixFOV(fov,aspect,nearPlane,farPlane)
  w,h,img_arr,depths,mask = p.getCameraImage(200,200, viewMatrix,projectionMatrix, lightDirection,lightColor,renderer=p.ER_TINY_RENDERER)

  p.stepSimulation()

