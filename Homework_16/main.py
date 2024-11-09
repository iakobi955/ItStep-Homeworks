# 1. შექმენით პითონის კლასი Car, ატრიბუტებით: ბრენდი, მოდელი და წელი. 
#    ასევე, შექმენით კლასის მეთოდი car_info(), რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.
# 2. Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს.
# 3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car კლასს. 
#    დაამატეთ ახალი ატრიბუტი battery_life და მეთოდი battery_info(), რომელიც დაბეჭდავს 
#    შემდეგ სტრიქონს "ამ მანქანის ბატარეის ხანგრძლივობა არის [battery_life] საათი".
# 4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას. 
#    გაზარდეთ ეს ცვლადი ყოველ ჯერზე, მანქანის შექმნისას. 
# 5. Car კლასს დაამატეთ მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.

from datetime import datetime

current_year = datetime.now().year

class Car:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        Car.number_of_cars += 1

    def car_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}\n"

    def age_of_car(self):
        return f"Age of {self.brand} {self.model} is: {current_year - self.year} years\n"
    
    def total_cars(self):
        return f"Number of cars is: {Car.number_of_cars}\n"

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        return f"Battery life of {self.brand} {self.model} is {self.battery_life} hours\n"


#==================

ecar1 = ElectricCar(brand="Tesla", model="Model X", year= 2020, battery_life= 17)

print(ecar1.car_info())
print(ecar1.age_of_car())
print(ecar1.battery_info())
print(ecar1.total_cars())

