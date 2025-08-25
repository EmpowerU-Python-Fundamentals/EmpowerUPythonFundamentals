import re
   
password = input("Enter your password to check its validity: ")
pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[$@#]).{6,16}$') 

if pattern.match(password): 
    print("Your password is accepted") 
else: 
    print("Your password didn't match the description")

    
    

