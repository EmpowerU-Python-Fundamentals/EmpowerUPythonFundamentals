def calculate_area(choice, *dimensions):
    """Calculates the area based on the user's choice."""
    if choice == 'rectangle':
        length, width = dimensions
        area = length * width
        return 'rectangle', area
    elif choice == 'circle':
        radius = dimensions[0]
        import math
        area = math.pi * math.pow(radius, 2)
        return 'circle', area
    elif choice == 'triangle':
        base, height = dimensions
        area = 0.5 * base * height
        return 'triangle', area
    else:
        raise ValueError("Invalid choice")