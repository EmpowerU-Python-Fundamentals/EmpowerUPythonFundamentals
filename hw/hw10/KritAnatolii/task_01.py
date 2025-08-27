#TASK 1
class Polygon:
    def __init__(self):
        pass

class Rectangle(Polygon):
  def __init__(self, width, height):
      self.width = width
      self.height = height
      
  def area(self):
      return self.width * self.height

#TASK 2
class Human:
    human_species = "\"Homosapiens\""

    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print ("Hello, I am {}.".format(self.name))
    
    def species (cls):
        print (f"I belong to {cls.human_species}")
    
    @staticmethod
    def message():
        print ("This is a Human class.")
   
#TASK 3
