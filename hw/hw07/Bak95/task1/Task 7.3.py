input_str = input("Введіть рядок для підрахунку символів: ")
char_count = {}
for char in input_str:
    char_count[char] = char_count.get(char, 0) + 1

print(f"Вихідний словник: {char_count}")