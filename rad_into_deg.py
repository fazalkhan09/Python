import math
#Creating Functions
def rad_into_deg(num):
    degrees=num*(180.0/math.pi)
    return degrees
def deg_into_rad(num):
    radians=num*(math.pi/180.0)
    return radians
#Testing the functions
print("Radian to Degree Conversion:")
angle_in_rad=float(input("Enter an angle in Radians: "))
print(rad_into_deg(angle_in_rad))
print("Degree to Radian Conversion:")
angle_in_deg=float(input("Enter an angle in Degrees: "))
print(deg_into_rad(angle_in_deg))

    