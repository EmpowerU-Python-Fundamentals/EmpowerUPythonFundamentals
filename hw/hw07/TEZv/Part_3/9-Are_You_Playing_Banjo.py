def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f'{name} plays banjo'
    else:         
        return f'{name} does not play banjo'
    
print(are_you_playing_banjo("Ringo"))  # Output: "Ringo plays banjo"
print(are_you_playing_banjo("John"))   # Output: "John does not play banjo"
print(are_you_playing_banjo("Paul"))   # Output: "Paul does not play banjo"
print(are_you_playing_banjo("George")) # Output: "George does not play banjo"

print(are_you_playing_banjo("ringo"))  # Output: "ringo plays banjo"
print(are_you_playing_banjo("john"))   # Output: "john does not play banjo"
print(are_you_playing_banjo("paul"))   # Output: "paul does not play banjo"
print(are_you_playing_banjo("george")) # Output: "george does not play banjo"