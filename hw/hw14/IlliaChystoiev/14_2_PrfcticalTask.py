import json
file_cars = open("cars.json", "r")
file_cars2 = open("cars2.json", "r")
result_file = open("result.json", "w")

cars = json.load(file_cars)
car2 = json.load(file_cars2)
cars.append(car2)
cars_sorted = sorted(cars, key=lambda x: x["max_speed"])
json.dump(cars_sorted, result_file, ensure_ascii=False, indent=2)

file_cars.close()
file_cars2.close()
result_file.close()