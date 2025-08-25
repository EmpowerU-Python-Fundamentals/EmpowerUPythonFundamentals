import area


def get_number(num):
  """Gets valid number with error handling"""
  
  while True:
      try:
          return float(input(num).replace(',', '.'))
      except ValueError:
          print("Not a number. Please try again.")

def get_shape():
  """Get valid shape choice with error handling"""
  
  print("Choose the number of the shape to calculate the area:")
  print("1. Rectangle\n2. Triangle\n3. Circle\n")
  while True:
        try:
            shape = int(input())
            if shape in [1, 2, 3]:
                return shape
            else:
                print ("Please enter 1, 2 or 3.")
        except ValueError:
            print("Not a number. Please try again.")



def main():
      """Main program loop"""
  
      while True:
          shape = get_shape()

          if shape == 1:
              print("Enter the length and width of the rectangle:")
              length = get_number("Enter the length: ")
              width = get_number("Enter the width: ")
              print(area.rect_area(length, width))

          elif shape == 2:
              print("Enter the base and height of the triangle:")
              base = get_number("Enter the base: ")
              height = get_number("Enter the height: ")
              print(area.triangle_area(base, height))

          elif shape == 3:
              print("Enter the radius of the circle:")
              radius = get_number("Enter the radius: ")
              print(area.circle_area(radius))

          
          while True:
              continue_calc = input("\nDo you want to calculate another area? (y/n): ").lower().strip()
              if continue_calc in ['y', 'yes']:
                  print()  
                  break
              elif continue_calc in ['n', 'no']:
                  return
              else:
                  print("Please enter 'y' for yes or 'n' for no.")


if __name__ == "__main__":
    main()