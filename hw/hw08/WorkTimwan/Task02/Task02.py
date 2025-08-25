password = input("Enter your password ")

tiny_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

big_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sumball= ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
 ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']



if 6 <= len(password) <= 16 :
    password=list(password)

    for i in password:
        for j in tiny_letter:
            
            if i == j:
                
                break

            else:
                pass
        for l in big_letter:
            
            if i == l:
                
                break
        
            else:
                pass
        
        for sym in sumball:
            if i == sym:
                
                break
        
            else:
                pass
        

        
        if i.isdigit():
            break
            

        else:
            pass


else:
    print("Your password is not validity")

print("Pasword is validity")