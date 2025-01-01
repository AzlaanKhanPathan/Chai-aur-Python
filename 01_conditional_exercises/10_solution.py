pet = input("What pet do you have ? ")
pet_age = int(input("What is age of your pet ? "))
pet_food = None

if pet == "Dog":
    if pet_age < 2:
        pet_food = "Puppy Food"
    elif pet_age >= 2:
        pet_food = "Senior Dog Food"

elif pet == "Cat":
    if pet_age < 2:
        pet_food = "Kitten Food"
    elif pet_age >= 2:
        pet_food = "Senior Cat Food"

if pet_food:
    print(pet_food)
else: 
    print("Sorry , i don't have food recommendation")