def check(password):
    if len(password) < 6:
        return False
    elif 'password' in password.lower():
        return False
    elif not any(map(str.isdigit, password)):
        return False
    elif not any(map(str.isalpha, password)):
        return False
    return True
