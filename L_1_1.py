
def is_it_palindrom(str):
    str = str.lower().replace(' ','')
    if str == str[::-1]:
        return True
    else:
        return False



print(palindrom('12'))

