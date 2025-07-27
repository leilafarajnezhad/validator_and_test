import re

def email(email_chek):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email_chek):
        return True
    return False



assert email("farajnezhad.leila@gmail.com")== True


print("ok")