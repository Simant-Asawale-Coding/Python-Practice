speed=0
distance=100
dist_unit="km"
time=2
time_unit="hour"

speed=distance/time
print("speed:", speed,dist_unit,"per",time_unit) 
# the error with floating numbers
print(6-5.7) # the answeer should be 0.3, but instead it is aprrox 0.2999xx8 
#this is because of the way floating points are stored in computer systems causing them to have inaccuracies
x=6-5.7
print(round(x,2))
# type: ignore # type: ignore\

