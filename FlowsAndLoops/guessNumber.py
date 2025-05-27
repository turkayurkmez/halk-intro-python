import random
#1. Bilgisayar bir sayı tutar:
oyun_bittimi = False

while not oyun_bittimi:
    number = random.randint(1,100)
#2. Kullanıcıdan tahmin etmesini ister:
    bilindi_mi = False
    while not bilindi_mi:    
        suggest =int(input("Tahmininizi girin:"))
        if number < suggest:
            print("Aşağı...")
        elif number > suggest:
            print("Yukarı")
        else:
            bilindi_mi = True
            print("Bildiniz")

    answer = input("Bir oyun daha ister misiniz (e/h)")
    oyun_bittimi = answer == "h"
    