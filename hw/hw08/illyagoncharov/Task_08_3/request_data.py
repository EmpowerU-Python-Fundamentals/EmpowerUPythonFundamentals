def figure_and_params():
    params = {}
    figure = input("Which shape do you need to calculate the area of? \n"
               " Choose: \n"
               " 1 - if it is a rectangle, \n"
               " 2 - if it is a triangle, \n"
               " 3 - if it is a circle \n")
    if figure =='1':
        params['a'] = float(input("Specify the length of one side:"))
        params['b'] = float(input("Specify the length of second side:"))
        figure = "Rectangle"
    elif figure =='2':
        params['a'] = float(input("Specify the length of height of triangle:"))
        params['b'] = float(input("Specify the length of base of triangle:"))
        figure = "Triangle"
    elif figure =='3':
        params['a'] = float(input("Specify the radius of circle:"))
        params['b'] = 1
        figure = "Circle"
    else:
        return
    return figure, params