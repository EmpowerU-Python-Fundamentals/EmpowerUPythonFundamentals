# import random
import math

# Клас Sphere для обчислення властивостей кулі (об'єм, площа, густина).
class Sphere:
    """
    Клас для моделювання кулі з радіусом та масою.
    """
    def __init__(self, radius: float, mass: float):
        """
        Ініціалізує об'єкт Sphere.
        
        Args:
            radius (float): Радіус кулі.
            mass (float): Маса кулі.
        """
        self._radius = radius
        self._mass = mass
        self._volume = None
        self._surface_area = None

    def get_radius(self):
        """Повертає радіус кулі."""
        return self._radius

    def get_mass(self):
        """Повертає масу кулі."""
        return self._mass

    def get_volume(self):
        """
        Обчислює та повертає об'єм кулі, округлений до 5 знаків.
        """
        if self._volume is None:
            self._volume = (4/3) * math.pi * self._radius**3
        return round(self._volume, 5)

    def get_surface_area(self):
        """
        Обчислює та повертає площу поверхні кулі, округлену до 5 знаків.
        """
        if self._surface_area is None:
            self._surface_area = 4 * math.pi * self._radius**2
        return round(self._surface_area, 5)

    def get_density(self):
        """
        Обчислює та повертає густину кулі, округлену до 5 знаків.
        """
        # Перераховуємо об'єм, якщо він ще не був обчислений
        volume = self.get_volume()
        if volume == 0:
            return 0.0
        return round(self._mass / volume, 5)

# Приклад використання
ball_sphere = Sphere(2, 50)
print(f"Radius: {ball_sphere.get_radius()}")
print(f"Mass: {ball_sphere.get_mass()}")
print(f"Volume: {ball_sphere.get_volume()}")
print(f"Surface Area: {ball_sphere.get_surface_area()}")
print(f"Density: {ball_sphere.get_density()}")
print("-" * 20)
