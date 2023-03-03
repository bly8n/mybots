import pyrosim.pyrosim as pyrosim
x=1
y=1
z=1
pyrosim.Start_SDF("boxes.sdf")
for i in range(5):

    for j in range(5):
        x=1
        y=1
        z=1
        z1=1+i*10+j

        for k in range(10):
            pyrosim.Send_Cube(name="Box[i]", pos=[i*1.01,j*1.01,z1] , size=[x,y,z])
            x=0.9*x
            y=0.9*y
            z=0.9*z
            z1=z1+1
pyrosim.End()
