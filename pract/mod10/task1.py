import re
 
def check_password(password):
    """
    >>> check_password("rtG3FG!Tr^e")
    True
    >>> check_password("aA1!*!1Aa")
    True
    >>> check_password("oF^a1D@y5e6")
    True
    >>> check_password("enroi#$rkdeR#$092uWedchf34tguv394h")
    True
    >>> check_password("пароль")
    False
    >>> check_password("password")
    False
    >>> check_password("qwerty")
    False
    >>> check_password("lOngPa$$$W0Rd")
    False
    """
    # Регулярное выражение для проверки пароля
    if len(password) < 6:
        return False
 
    if len(re.findall(r'[A-Z]', password)) < 2:
        return False
 
    if len(re.findall(r'\d', password)) < 1:
        return False
 
    if len(re.findall(r'[^A-Za-z0-9]', password)) < 2:
        return False
 
    if re.search(r'(.)\1\1', password):
        return False
 
    return True
# Запуск doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)