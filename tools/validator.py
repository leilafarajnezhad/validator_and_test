import re

mobile_list=[]


def code_object(code):
    if re.match(r"^[a-z][0-9]{3,}$", code):
        for name in mobile_list:
            if name["code"] == code:
                print("valid_cod")
                return True
            else:
                print("Invalid code")

#--------------------------
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
#--------------------------

def age(age_valid):
    if 18<= age_valid <= 30:
        return True
    else:
        print("Invalid age")
        return False


#--------------------------

def family(family_name):
   if re.match(r"^[A-Za-z\s]{3,30}$", family_name):
       return True
   return False
#--------------------------

def money():
    pass
#--------------------------

def mobile():
    if re.match(r"^\d{4}-\d{3}-\d{4]$", mobile):
        return True

#--------------------------

def email():
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email):
        return True


#--------------------------

def idcard():
    if re.match(r"^\d{3}-\d{6}-\d{1}$", idcard):
        return True

#--------------------------

def address():
    if re.match(r"^[a-zA-Z\s]{3,90}$]"):
        return True


#-----------brand---------------


def brand_object(name):
    if re.match(r"^[A-Z][a-z]$", name):
        brand_name = name




#-------------price-------------

def price_object():
        try:
            price = float(input("Enter price in dollars: "))
            if 1000 <= price <= 2000:
                print("The price is valid:", price)
                return price
            else:
                print("The price must be between 1000 and 2000 dollars.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None


#--------------------------

def fa_name_validator(fa_name):
    if type(fa_name) == str and re.match(r'^[\sآ-ی]{3,30}$', fa_name):
        return True
    else:
        print("error:invalid name !!!")
        return False

#--------------------------
def en_name_validator(en_name):
    if re.match(r"^[a-zA-Z\s]{3,30}$", en_name):
        return True
    else:
        print("error:invalid name !!!")
        return False

#--------------------------

def show_menu():

        print("menu")
        print("1) add product")
        print("2) find product by code")
        print("3) find product by name")
        print("4) show product list")
        print("0) exit")

        option = int(input("enter your option: "))

        print("-" * 50)

        return option

#--------------------------
#todo

def get_data():
      code = input("enter your code: ")
      name= input("enter your name: ")
      brand = input("enter your brand: ")
      price = input("enter your price: ")

      for item in mobile_list:
          if item["code"] == code:
              print("Code is duplicated.")
              return

      if code_object (code) and\
         name_object(name) and \
         brand_object(brand) and\
         price_object(price):

         product=[
             {"code":code,
              "name":name,
              "brand":brand,
              "price":price}
         ]
         mobile_list.append(product)
         print("success")


#------------------------------

def seve_mobile(name , code):
    name_object["code"]=code
    return name_object

#-----------------------------

def cheking():
    product = get_data()
    if code_object(product):
        seve_mobile(product,code_object(product))
    else:
        print("error")

#-----------------------------
def find_by_code(mobile_list, code):
    by_code=[]
    for name_object in mobile_list:
        if name_object is None:
            continue
        if name_object["code"] == code:
            by_code.append(name_object)
    return name_object


#-----------------------------
def find_by_price(mobile_list, price):
    by_price=[]
    for name_object in mobile_list:
        if name_object is None:
            continue
        if 1000 <= name_object["price"] <= 3000:
            by_price.append(name_object)
    return name_object


def show_list(mobile_list):
    for product in mobile_list:
        if product is None:
            continue
        print(product["code_object"],product["name_object"],product["brand_object"],product["price_object"])

