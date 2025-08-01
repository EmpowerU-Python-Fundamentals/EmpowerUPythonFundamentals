def reverse(st):
    return " ".join([w for w in st.split()[::-1]])

print(reverse("Hello World"))