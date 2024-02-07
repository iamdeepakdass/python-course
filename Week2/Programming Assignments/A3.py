password = input()

def isValid(password):
    if(8 <= len(password) <= 32): #first condition
        if(password[0].isalpha()): # second condition
            forbidden = {"/", "\\", "'", '"'}
            if(not any(char in forbidden for char in password)): # third condition
                if ' ' not in password: #fourth condition
                    return True
    return False

print(isValid(password), end="")

