import pyrosim.pyrosim as pyrosim
x=1
y=1
z=1
pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="box",pos=[0,0,0.5] , size=[x,y,z]) 
pyrosim.End()

