import re

passwords = input("Enter comma separated passwords: ")

valid = []

for pwd in passwords.split(","):
    pwd = pwd.strip()
    if (6 <= len(pwd) <= 12 and
        re.search("[a-z]", pwd) and
        re.search("[A-Z]", pwd) and
        re.search("[0-9]", pwd) and
        re.search("[$#@]", pwd)):
        valid.append(pwd)

print(",".join(valid))