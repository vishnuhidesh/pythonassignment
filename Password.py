# Write a Python program to check the validity of a password given by the user. The
# Password should
# satisfy the following criteria:
# 1. Contains at least one letter between a and z
# 2. Contains at least one number between 0 and 9
# 3. Contains at least one letter between A and Z
# 4. Contains at least one special character from $, #, @
# 5. Minimum length of password: 6


import re
def check(password):
    if len(password) < 6:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[$#@]', password):
        return False
    return True

password = input("Enter a password: ")
if check(password):
    print("Password is valid.")
else:
    print("Password is not valid.")
