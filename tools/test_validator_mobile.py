import re

def name_object(name,en_name,fa_name):
    if re.match(r"^[a-zA-Z\s]{3,30}$", name):
            if type(fa_name) == str and re.match(r'^[\sآ-ی]{3,30}$', fa_name):
                if re.match(r"^[A-Za-z\s]{3,30}$", en_name):
                    return True
                else:
                    print("error:invalid name !!!")
                    return False
            else:
                print("error:invalid name !!!")
                return False
    else:
        print("Invalid name")
        return False

assert name_object("leila","solmaz","لیلا")== True

print("ok")