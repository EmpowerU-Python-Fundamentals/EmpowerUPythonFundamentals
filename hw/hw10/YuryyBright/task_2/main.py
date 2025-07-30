from core import Ball, SuperBall, Ghost, create_humans, Person, Sphere, ClassFactory

def demonstrate_tasks():
    """Demonstrate all practical tasks"""
    print("=== PRACTICAL TASKS DEMONSTRATION ===\n")

    # Task I: Ball-super-ball
    print("TASK I: Ball and SuperBall")
    print("-" * 40)
    try:
        ball = Ball()
        super_ball = SuperBall()
        print(f"Regular ball type: {ball.ball_type}")
        print(f"Super ball type: {super_ball.ball_type}")
    except Exception as e:
        print(f"Error: {e}")

    # Task II: Color-ghost
    print("\nTASK II: Color Ghost")
    print("-" * 40)
    try:
        ghosts = [Ghost() for _ in range(3)]
        for i, ghost in enumerate(ghosts, 1):
            print(f"Ghost {i} color: {ghost.color}")
    except Exception as e:
        print(f"Error: {e}")

    # Task III: Basic-subclasses-Adam-and-Eve
    print("\nTASK III: Adam and Eve")
    print("-" * 40)
    try:
        humans = create_humans()
        for human in humans:
            print(f"{human.name} is {human.gender()}")
    except Exception as e:
        print(f"Error: {e}")

    # Task IV: Classy-classes
    print("\nTASK IV: Classy Classes")
    print("-" * 40)
    try:
        person = Person("John", 30)
        print(person.get_info())
    except Exception as e:
        print(f"Error: {e}")

    # Task V: Building Spheres
    print("\nTASK V: Building Spheres")
    print("-" * 40)
    try:
        sphere = Sphere(2.0, 10.0)
        print(f"Sphere radius: {sphere.radius}")
        print(f"Sphere mass: {sphere.mass}")
        print(f"Sphere volume: {sphere.get_volume():.2f}")
        print(f"Sphere surface area: {sphere.get_surface_area():.2f}")
        print(f"Sphere density: {sphere.get_density():.2f}")
    except Exception as e:
        print(f"Error: {e}")

    # Task VI: Dynamic Classes
    print("\nTASK VI: Dynamic Classes")
    print("-" * 40)
    try:
        DynamicClass = ClassFactory.create_dynamic_class("DynamicPerson", ["name", "age"])
        dynamic_instance = DynamicClass("Alice", 25)
        print(f"Dynamic class instance: {dynamic_instance}")
        print(f"Name: {dynamic_instance.name}, Age: {dynamic_instance.age}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    demonstrate_tasks()