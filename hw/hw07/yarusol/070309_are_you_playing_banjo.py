# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r",
#   you are playing banjo!
#
# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"

def are_you_playing_banjo(name:str):
    if name[:1].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print(f"{are_you_playing_banjo("qwer")}")
print(f"{are_you_playing_banjo("rqwer")}")
print(f"{are_you_playing_banjo("Rqwer")}")