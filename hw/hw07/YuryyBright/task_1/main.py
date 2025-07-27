from .core import NumberComparer, ShapeAreaCalculator, CharacterCounter

def main():
    # Task 1: Max of two numbers
    print("Task 1:")
    print("Max of 10 and 20:", NumberComparer.max_of_two(10, 20))

    # Task 2: Shape area calculations
    print("\nTask 2:")
    print("Rectangle area (5 x 3):", ShapeAreaCalculator.rectangle_area(5, 3))
    print("Triangle area (base=4, height=2):", ShapeAreaCalculator.triangle_area(4, 2))
    print("Circle area (radius=3):", ShapeAreaCalculator.circle_area(3))

    # Task 3: Count characters in a string
    print("\nTask 3:")
    input_str = "hello"
    result = CharacterCounter.count_characters(input_str)
    print(f"Character count for '{input_str}':", result)

if __name__ == "__main__":
    main()
