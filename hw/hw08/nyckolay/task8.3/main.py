"""08.3 Practical tasks. Task 2 'Largest Number" """

import areacalc

result = 0
shape = ""
var = ""
func_to_call = ""

figures = ["", "rectangle", "triangle", "circle"]
param_text = ["", 
              "height and width separated by spaces",
              "base and height separated by spaces",
              "radius"]

figure = int(input("Which figure's area do you want to calculate?\n1 - rectangle, 2 - triangle,  3 - circle: "))

if figure in (1, 2, 3):
    var = [float(i) for i in input(f"Enter {param_text[figure]}: ").split()]
    shape = figures[figure]
    func_to_call = 'areacalc.' + figures[figure] + '_area(var)'
    result = eval(func_to_call)
else:
    result = False

if result:
    print(f"{shape.capitalize()} area is {result}")
else:
    print("Wrong figure")
