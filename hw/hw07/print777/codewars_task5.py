#V. Reversing Words in a String

def reverse(text):
    words = text.strip().split()
    return ' '.join(words[::-1])
print(reverse("   Hello    World "))

