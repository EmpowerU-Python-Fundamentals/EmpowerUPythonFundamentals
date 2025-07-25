def get_user_choice():
    """Prompts the user for a choice and returns it."""
    print("Please choose an option:")
    print("1. Rectangle area")
    print("2. Circle area")
    print("3. Triangle area")
    choice = input("Enter your choice (1-3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (1-3): ")
    if choice == '1':
        a, b = map(float, input("Enter length and width (separated by space): ").split())
        return 'rectangle', a, b
    elif choice == '2':
        r = float(input("Enter radius: "))
        return 'circle', r
    elif choice == '3':
        a, h = map(float, input("Enter base and height (separated by space): ").split())
        return 'triangle', a, h
    return choice
__all__ = ['get_user_choice']