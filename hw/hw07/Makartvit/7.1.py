# task_1
def max_two(a, b):
    return max(a, b)


print(max_two(21, 10))
print(max_two(-10, -3))


# task_2
def area_rectangle(width, height):
    return width * height


def area_triangle(base, height):
    return 0.5 * base * height


def area_circle(radius):
    return 3.14 * radius ** 2


print("1) Rectangle\n2) Triangle\n3) Circle")
square = input("Square (1–3): ")

if square == '1':
    w = float(input("Width: "))
    h = float(input("Height: "))
    print("Area =", area_rectangle(w, h))

elif square == '2':
    b = float(input("Base: "))
    h = float(input("Height: "))
    print("Area =", area_triangle(b, h))

elif square == '3':
    r = float(input("Radius: "))
    print("Area =", area_circle(r))

else:
    print("Invalid square")


# task_3

def count(s):
    counts = {}
    for i in s:
        counts[i] = counts.get(i, 0) + 1
    return counts


print(count("hello"))
