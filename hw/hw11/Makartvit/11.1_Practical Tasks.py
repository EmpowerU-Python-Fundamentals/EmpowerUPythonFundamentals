# tasks_1
def analyze_age(text):
    age = int(text)
    if age < 0:
        raise ValueError("age cannot be negative")
    return "even" if age % 2 == 0 else "odd"


user_input = input("Enter your age: ")
try:
    print(f"Age is {analyze_age(user_input)}.")
except ValueError as e:
    print(f"Error: {e}")

print("The program works:")
for sample in ["22", "15", "-3", "abc"]:
    try:
        print(sample, "---", f"Age is {analyze_age(sample)}.")
    except ValueError as e:
        print(sample, "---", f"Error: {e}")


# tasks_2

def day_of_week(text):
    n = int(text)
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    if n not in days:
        raise ValueError("number must be between 1 and 7")
    return days[n]


user_input = input("Enter a number (1-7): ")
try:
    print(day_of_week(user_input))
except ValueError as e:
    print(f"Error: {e}")

print("The program works:")
for sample in ["1", "7", "8", "food"]:
    try:
        print(sample, "---", day_of_week(sample))
    except ValueError as e:
        print(sample, "---", f"Error: {e}")
