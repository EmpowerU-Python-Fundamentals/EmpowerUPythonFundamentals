from classes.sphere import Sphere

def main():
    sphere = Sphere(5, 10)
    print(f"Volume: {sphere.get_volume()}")
    print(f"Surface Area: {sphere.get_surface_area()}")
    print(f"Density: {sphere.get_density()}")
    print(f"Radius: {sphere.get_radius()}")
    print(f"Mass: {sphere.get_mass()}")

# https://www.codewars.com/kata/55c1d030da313ed05100005d
if __name__ == "__main__":
    main()