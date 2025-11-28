#Q.1-
class Car:
   total_car=0
   def __init__(self,brand,model):
      self.__brand=brand
      self.__model=model
      Car.total_car+=1
   def full_name(self):
      return f"{self.__brand} {self.__model}"
   
   def get_brand(self):
      return self.__brand +"!"
   
   def fual_type(self):
      return "Petrol or Diesel"
   @staticmethod
   def general_description():
      return "Car are means of transport"
   @property
   def model(self):
      return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
       self.battery_size=battery_size
       super().__init__(brand, model)  
    def fual_type(self):
      return "Electric Car"

          
my_car =Car("Toyato","Corolla")
# print(my_car.brand)
# print(my_car.model)
print(my_car.full_name())
print(my_car.general_description())

# my_new_car=Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(myCar.get_brand())
# print(myCar.__brand)
# myCar=ElectricCar("Tesla","Model S","85kWh")
# print(myCar.fual_type())
# safari= Car("Tata","Safari")
# print(safari.fual_type())
# print(Car.total_car)
# print(Car.general_description())
# print(myCar.model)
# print(isinstance(myCar,ElectricCar))
# print(isinstance(myCar,Car))

class Battery:
   def battery_info(self):
      return "this is battery"
class Engine:
      def engine_info(self):
         return "this is engine"

class Electriccartwo(Battery,Engine,Car):
   pass
my_new_tesla=Electriccartwo("Tesla","Model s")
# print(my_new_tesla.engine_info())
# print(my_new_tesla.battery_info())