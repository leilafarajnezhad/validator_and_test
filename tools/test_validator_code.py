import re


def code_object(code):
    if re.match(r"^[a-z][0-9]{3,}$", code):
        return True
    return False



assert code_object("0000") == False
assert code_object("a555") == True
assert code_object("asoo") == False

print("All tests passed")
