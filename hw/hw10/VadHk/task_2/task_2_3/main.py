from classes.human import Human
from classes.man import Man
from classes.woman import Woman


def main():
    Adam = Man("Adam")
    Eve = Woman("Eve")
    for human in Human.humans():
        print(human)

# https://www.codewars.com/kata/basic-subclasses-adam-and-eve
if __name__ == "__main__":
    main()