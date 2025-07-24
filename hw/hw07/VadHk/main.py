from library import tasks
  

def main():
    part = int(input("Enter tasks part number (1 or 2): "))

    match part:
        case 1:
            print("Executing Part 1:")
            print("--------------------------")
            tasks.part_1()
        case 2:
            print("Executing Part 2:")
            print("--------------------------")
            tasks.part_2()
        case _:
            print("Invalid part number. Please enter 1 or 2.")
            main()
   
if __name__ == "__main__":
    main()