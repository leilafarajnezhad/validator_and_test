import re

def family(family_name):
   if re.match(r"^[A-Za-z\s]{3,30}$", family_name):
       return True
   return False

assert family("Alipur") == True
assert family("kayed") == True
assert family("1faraj") == False

print("All tests passed")