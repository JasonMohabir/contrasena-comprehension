def passwordCheckerLite(password):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    stuff = [1 if x in uppercase else
             2 if x in lowercase else
             3 if x in numbers else
             0 for x in password]
    print stuff
    if (1 in stuff and
        2 in stuff and
        3 in stuff):
        return True
    else:
        return False

def passwordStrenght(password):
    strength = 0
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    symbols = "?!&#,;:-_*"
    stuff = [1 if x in uppercase else
             2 if x in lowercase else
             3 if x in numbers else
             4 if x in symbols else
             0 for x in password]
    if (1 in stuff):
        strength += 2
    if (2 in stuff):
        strength += 2
    if (3 in stuff):
        strength += 2
    if (4 in stuff):
        strength += 2
    if (len(stuff) >= 10):
        strength += 2
    return str(strength)

