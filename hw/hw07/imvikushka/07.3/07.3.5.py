# Reversing Words in a String

def reverse(st):
    st_list = st.split()
    st_list.reverse() 
    result = " ".join(st_list)
    return result