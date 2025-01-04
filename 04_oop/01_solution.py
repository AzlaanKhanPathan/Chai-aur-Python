class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    # Encapsulation
    def get_brand(self):
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    # Polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"
    
    # Static method
    @staticmethod
    def general_description(self):
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    # Polymorphism
    def fuel_type(self):
        return "Electric charge"


my_electric_car = ElectricCar("Tesla", "Model S", "85kWh")

# isinstance method 
# print(isinstance(my_electric_car, Car))
# print(isinstance(my_electric_car, ElectricCar))

# print(my_electric_car.full_name())
# print(my_electric_car.fuel_type())

# Static method which allows only class to access but not to the instance
# print(Car.general_description())

safari = Car("Tata", "Safari")
safariThree = Car("Tata", "Nexon")
# safari.model = "City"
# print(safari.model)
# print(safari.fuel_type())

# print(Car.total_car)

# cannot access the brand without calling method
# print(my_electric_car.__brand)
# print(my_electric_car.get_brand())



# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


class Battery:
    def battery_info(selff):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass


my_new_electric = ElectricCarTwo("Tesla", "Model S")
print(my_new_electric.engine_info())
print(my_new_electric.battery_info())