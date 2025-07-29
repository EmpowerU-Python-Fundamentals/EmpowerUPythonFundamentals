import module

module.FREEZING_POINT = 0
module.BOILING_POINT = 100

temperature = float(input("Enter the temperature: "))
module.print_water_state(temperature)
