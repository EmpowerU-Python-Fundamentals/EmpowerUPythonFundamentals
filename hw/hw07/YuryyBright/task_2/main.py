from .core import (
    greet, distance_between_points, remove_exclamation_marks,
    number_to_string, reverse_words, reverse_list,
    sum_of_multiples, can_reach, are_you_playing_banjo,
    bool_to_word, count_sheep, correct_tail
)

print(greet("Johnny"))  # => Hello, my love!
print(distance_between_points(1 + 1j, 4 + 5j))  # => 5.0
print(remove_exclamation_marks("Hello! World!"))  # => Hello World
print(number_to_string(123))  # => "123"
print(reverse_words("Python is great"))  # => "great is Python"
print(reverse_list([1, 2, 3]))  # => [3, 2, 1]
print(sum_of_multiples(10))  # => 23 (3 + 5 + 6 + 9)
print(can_reach(50, 25, 2))  # => True
print(are_you_playing_banjo("Rick"))  # => Rick plays banjo
print(bool_to_word(True))  # => Yes
print(count_sheep([True, False, True]))  # => 2
print(correct_tail("Fox", "x"))  # => True
