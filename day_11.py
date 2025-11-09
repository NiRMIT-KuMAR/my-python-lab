car = {
  "make" : "Honda" ,
  "model" : "Civic" ,
  "year" : 2020 ,
  "color" : "Red"
  }

print(f"I have a {car["color"]} {car["make"]} {car["model"]}")

car["milage"] = 45000

car["color"] = "Orange"

for key , value in car.items() :
  print(f"{key} : {value}")