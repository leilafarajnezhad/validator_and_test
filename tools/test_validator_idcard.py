import re



def idcard(idcard_number):
    if re.match(r"^\d{3}-\d{6}-\d{1}$", idcard_number):
        return True
    return False


assert idcard("0a19999999")== False
assert idcard("001-999999-9")== True

print("all ok")
