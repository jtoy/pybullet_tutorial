import pybullet as p
p.connect(p.GUI)
p.setGravity(0,0,-0.005)
p.setRealTimeSimulation(0)
p.startStateLogging(p.STATE_LOGGING_VIDEO_MP4, "video.mp4")
xyz = [-2,-2,3]
sphere = p.createCollisionShape(p.GEOM_SPHERE,halfExtents=[0.5,0.5,0.5])
p.createMultiBody(1,sphere,-1,basePosition=xyz)
for i in range(20000):
    p.stepSimulation()
