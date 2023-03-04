import pyrosim.pyrosim as pyrosim
x=1
y=1
z=1
def Create_World(x,y,z):
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-1,1,0.5] , size=[x,y,z])
    pyrosim.End()
Create_World(x,y,z)
def Create_Robot(x,y,z):
  pyrosim.Start_URDF("body.urdf")
  pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[x,y,z])
  pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
  pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[x,y,z])
  pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
  pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[x,y,z])
  pyrosim.End()
Create_Robot(x,y,z)
