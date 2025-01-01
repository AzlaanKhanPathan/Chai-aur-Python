distance = 5

if distance < 3:
    transport = "walk"
elif distance <=15 :
    transport = "Bike"
else:
    transport = "Car"

print("AI recommends you the transport of ",transport)