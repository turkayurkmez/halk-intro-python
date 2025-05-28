import math
def addProduct(name, price):
    print(f"{name} ve {price} değerleri eklendi")


addProduct("Bezelye",30)

def createOrder(name, quantity, address, payment):
    print(f"{name} isimli üründen {quantity} adet {address} adresine gönderilecek. {payment} TL ödeme yapıldı")

#named parameters:
createOrder(quantity=5, name="Dell XPS", payment=100000, address="Eskişehir")

def get_area1(unit_length, geometry):
    if geometry.lower() == "kare":
        return unit_length ** 2
    elif geometry.lower() == "daire":
        return math.pi * (unit_length ** 2)
    else:
        print("hatalı parametre girdiniz")
        return 1

def get_area2(unit1, unit2, geometry):
    if geometry.lower() == "dikdörtgen":
        return unit1*unit2
    elif geometry.lower() == "üçgen":
        return  (unit1*unit2)/2
    else:
        print("hatalı parametre girdiniz")
        return 1
    
def optional_get_area(unit1, unit2=1, geometry="kare"):
    if geometry.lower() == "kare":
        return unit1 ** 2
    elif geometry.lower() == "daire":
        return math.pi * (unit1 ** 2)
    elif geometry.lower() == "dikdörtgen":
        return unit1 * unit2
    elif geometry.lower() == "üçgen":
        return  (unit1*unit2)/2
    else:
        print("hatalı parametre girdiniz")
        return 1
  
    

print(get_area1(unit_length = 5, geometry="Kare"))
print(get_area2(unit1= 4, unit2=7,geometry= "Dikdörtgen"))

print("Kare:",optional_get_area(10))
print("Daire:",optional_get_area(5,geometry="Daire"))
print("Üçgen:",optional_get_area(20,4,geometry="Üçgen"))

def create_order(payment_method="Credit card", isGift=False, ship_speed="normal"):
    pass