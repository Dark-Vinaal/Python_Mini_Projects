import re

password = input("Enter your password to check: ")

is_valid = True

if len(password) < 8:
    is_valid = False
elif not re.search("[a-z]", password):
    is_valid = False
elif not re.search("[A-Z]", password):
    is_valid = False
elif not re.search("[0-9]", password):
    is_valid = False
elif not re.search(r"[_@#$&%*+\-\/\]]", password):
    is_valid = False
elif re.search(r"\s", password):
    is_valid = False

if is_valid:
    print(f"✓ '{password}' is a Valid Password")
else:
    print(f"✗ '{password}' is NOT a Valid Password (must have 8+ chars, A-Z, a-z, 0-9, and _@$)")
