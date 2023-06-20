
def is_it_palindrom(str):
    str = str.lower().replace(' ','')
    if str == str[::-1]:
        return True
    else:
        return False

#test
print(is_it_palindrom ('А роза упала на лапу азора'))
print(is_it_palindrom ('12'))

