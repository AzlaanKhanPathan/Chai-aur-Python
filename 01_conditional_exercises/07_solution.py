order_size = "Medium"
extra_shot = False

if extra_shot:
    coffee = order_size + "coffee with extra shot"
else: 
    coffee = order_size + " coffee "

print("Order: ", coffee)