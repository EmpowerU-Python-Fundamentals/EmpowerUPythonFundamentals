from classes.myClass import MyClass

def main():
    my_class = MyClass()
    useful_class = MyClass.rename_class(my_class, "UsefulClass")
    second_useful_class = MyClass.rename_class(my_class, "SecondUsefulClass")

    print(my_class.__class__.__name__)
    print(useful_class.__name__)
    print(second_useful_class.__name__)

# https://www.codewars.com/kata/55ddb0ea5a133623b6000043/python
if __name__ == "__main__":
    main()