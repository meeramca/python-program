from math import *
length = int(input("Enter length of cuboid"))
breadth = int(input("Enter breadth of cuboid"))
height = int(input("Enter height of cuboid"))
totalsurfacearea= 2*(length*breadth+length*height+breadth*height)

print("total surface area of cuboid  = ", totalsurfacearea)
perimetercuboid = 2*(length+breadth)
print("perimeter of cuboid = ",perimetercuboid)