def count_vowels(*words):
    count = 0
    for word in words:
        if word == "a":
            count += 1 
        elif word == "e":
            count += 1
        elif word == "i":
            count += 1
        elif word == "o":
            count += 1
        elif word == "u":
            count += 1
    return count    
        
def reverse_string(name):
    r = ""
    for i in range(len(name)-1, -1,-1):
        r += name[i]   
    return r

def is_palindrome(user_input):
    r = ""
    for i in range(len(user_input)-1, -1,-1):
        r += user_input[i]   
    if r == user_input: 
        return True
    else: 
        return "NOT PALINDROM!"