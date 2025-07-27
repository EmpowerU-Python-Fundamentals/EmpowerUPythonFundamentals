# Write a function taking in a string like 
#   "WOW this is REALLY          amazing"
#   and returning "Wow this is really amazing".
# String should be capitalized and properly spaced.
# Using re and string is not allowed.

def filter_words(st: str):
    return " ".join(
        filter(lambda w : w, [word for word in st.split(" ")])
        ).capitalize()


# print(f"\"{filter_words('now    THIS is REALLY interesting')}\"") #=> Now this is really interesting
# print(f"\"{filter_words('HELLO CAN   YOU  HEAR ME  ')}\"") #=> Hello can you hear me
# print(f"\"{filter_words('THAT was    EXTRAORDINARY!   ')}\"") #=> That was extraordinary!
