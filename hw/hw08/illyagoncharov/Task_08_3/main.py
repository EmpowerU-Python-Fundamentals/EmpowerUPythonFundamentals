from calculation import area_calculate
from request_data import figure_and_params


def area_figure():
    try: figure, params = figure_and_params()
    except:
        print("Incorrect data")
        return
    res = area_calculate(figure, params)
    print(f"{figure} area = {res}")
    return res


area_figure()