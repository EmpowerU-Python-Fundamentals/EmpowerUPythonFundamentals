def reverse(st):
    return " ".join(st.split()[::-1])

print(reverse("Hello World"))  # Output: "World Hello"
print(reverse("Python is fun"))  # Output: "fun is Python"