def isPhoneNumber(text): #415-555-1234
    if len(text) != 12:
        return False # not phone number-size
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no araea code
    if text[3] != '-':
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False # missing second dash  
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # no last 4 digits  
    return True

print(isPhoneNumber("415-555-1234"))