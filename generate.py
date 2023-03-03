import pyrosim.pyrosim as pyrosim
x=1
y=1
z=1
#def Create_World(x,y,z):
#pyrosim.Start_SDF("world.sdf")
pyrosim.Start_SDF("box.sdf")
#pyrosim.Send_Cube(name="Box",pos=[0,0,0.5] , size=[x,y,z]) #pos=[-1,1,0.5] , size=[x,y,z])
pyrosim.Send_Cube(name="box",pos=[0,0,0.5] , size=[x,y,z]) #pos=[-1,1,0.5] , size=[x,y,z])
pyrosim.End()
#Create_World(x,y,z)
#def Create_Robot(x,y,z):
  #pyrosim.Start_URDF("body.urdf")
  #pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[x,y,z])
  #pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
  #pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[x,y,z])
  #pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
  #pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[x,y,z])
  #pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0,0.5,0.5])
  #pyrosim.Send_Cube(name="Link3", pos=[0,0.5,0] , size=[x,y,z])
  #pyrosim.Send_Joint( name = "Link3_Link4" , parent= "Link3" , child = "Link4" , type = "revolute", position = [0,1,0])
  #pyrosim.Send_Cube(name="Link4", pos=[0,0.5,0] , size=[x,y,z])
  #pyrosim.Send_Joint( name = "Link4_Link5" , parent= "Link4" , child = "Link5" , type = "revolute", position = [0,0.5,-0.5])
  #pyrosim.Send_Cube(name="Link5", pos=[0,0,-0.5] , size=[x,y,z])
  #pyrosim.Send_Joint( name = "Link5_Link6" , parent= "Link5" , child = "Link6" , type = "revolute", position = [0,0,-1])
  #pyrosim.Send_Cube(name="Link6", pos=[0,0,-0.5] , size=[x,y,z])
  #pyrosim.End()
#Create_Robot(x,y,z)

#pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[x,y,z])
#Create_World(x,y,z)
#Create_Robot(x,y,z)


#for i in range(5):

    #for j in range(5):
     #   x=1
      #  y=1
       # z=1
        #z1=1+i*10+j

        #for k in range(10):
         #   pyrosim.Send_Cube(name="Box[i]", pos=[i*1.01,j*1.01,z1] , size=[x,y,z])
          #  x=0.9*x
           # y=0.9*y
            #z=0.9*z
            #z1=z1+1


