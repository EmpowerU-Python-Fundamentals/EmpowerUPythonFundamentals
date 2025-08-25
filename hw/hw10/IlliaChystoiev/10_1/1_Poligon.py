class Polygon:
    def __init__(self, *sides: float):
        self.sides = list(sides)

    def perimeter(self) -> float:
        return sum(self.sides)

    def area(self) -> float:
        raise NotImplementedError("Area is not defined for generic Polygon")


class Rectangle(Polygon):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be > 0")
        self.width = width
        self.height = height
        super().__init__(width, height, width, height)

    def area(self) -> float:
        return self.width * self.height
