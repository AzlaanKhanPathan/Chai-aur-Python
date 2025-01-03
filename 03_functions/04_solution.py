import math

def circle_status(radius):
    area = math.floor(math.pi)* radius **2
    circumference = 2 * math.floor(math.pi) * radius
    return area, circumference

a , c = circle_status(3)

print("Area: ", a, "Circumference: ", c)