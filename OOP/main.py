from product import Product
from employee import Employee

if __name__ == "__main__":
    
    some_employee = Employee("Ahmet Bakar",50000,"Yazılım")
    salary =  float(input("Ne kadar maaş alıyor?"))
    ## Her instance için aşağıdaki denetim yanlış olduğundan; bu denetimi, sınıfın icra etmesi gerekir.
    # if salary >= 22000 and salary <= 100000:
    #     print("Uygundur")
    #     some_employee.salary = salary
    # else:
    #     print("Asgari üzcet ve max dışında maaş giremezsiniz ")
    some_employee.salary = salary
    some_employee.salary = salary * 1.25
    some_employee.full_name = "ABC"

    print(some_employee.salary_history)





    print("Main ayağa kalktı")
    laptop = Product("MacBook Pro",120000,100)
 
    

    print(laptop)

    print ("Ürün Bilgisi:",laptop.display_product_info())

    phone = Product("Samsung A35",14000,250)
    print(phone)
    # phone.name = "Samsung A35"
    # phone.price = 14000
    # phone.stock = 250

    
    print("Ürün Detayı",phone.display_product_info())
    
    shopping_card = [laptop,phone]

    discounted_list = list(map(lambda p: p.price * (0.9),shopping_card))
    print(shopping_card)
    print(discounted_list)

    print(laptop.check_stock())

    print(laptop,phone)
    print(repr(laptop))
    print("phone sock:",len(phone))
    laptop.stock = 10

    if laptop:
        print('stokta var',bool(laptop))
    else:
        print('stokta yok',bool(laptop))

    laptop2 = Product("MacBook Pro",120000,100)        
    if laptop == laptop2:
        print("Bu iki ürün aynı")
    else:
        print("Farklı ürünler..")

    if phone > laptop:
        print("Telefon pahalı")
    else:
        print("Laptop pahalı")

    total_price = phone + laptop
    print(total_price)

    ## toplu koleksiyon örnekleri:
    total_product = Product("",0,0)
    total_price_in_card=0
    print(total_product)
    for product in shopping_card:
        #total_product = product
        ##print("toplam değeri:",total_price_in_card)
        total_price_in_card = product + total_product
        total_product.price = total_price_in_card
        ##print("şu anki toplam",total_price_in_card)

    print("Ürünler toplamı:", total_price_in_card)

    orderedBasket = sorted(shopping_card)
    print("Sıralı:", orderedBasket)


        

