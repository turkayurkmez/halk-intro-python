import math
def get_total(*numbers):
    print("-"*50) 

    return sum(numbers)

print(get_total(10))
print(get_total(10,20,30))
print(get_total(10,20,30,1,21,3,4,5,6))

def get_state(*scores):
    if len(scores) == 0:
        return 0
    
    scores_sum = sum(scores)
    avg =  scores_sum  / len(scores)

    print("Notlar:",scores)
    print(f"Ortalama:{avg:.2f}")

    if avg >= 85:
        print("Çok başarılı")
    elif avg >=70:
        print("Başarılı")
    elif avg >= 50:
        print("Ortalama")
    else:
        print("Kaldı")    

    return avg

get_state(85,90,76,80,90)

print("Sınırsız key-value...")

def get_employee_profile(**kwargs):
    """ çalışan profili oluşturur. maas, yas ve email zorunludur."""
    for key, value in kwargs.items():
        if key == "maas":
            print(f"{key.capitalize()}, {value:,} TL")
        elif key == "yas":
            print(key.capitalize(),f"{value}  yaşında")
        elif key == 'email':
            print(key.capitalize(),value + "mail adresini kullanıyor")
        else:
            print(key.capitalize(),value)
            
            


get_employee_profile(maas=70000, yas=45,email="turkay.urkmez@gmail.com")
print("-"*100)
get_employee_profile(isim="Ayşe Demir",departman="yazılım", telefon="0532 201 01 01", adres="Ankara", pozisyon="Takım lideri")


print("--- Args ve kwargs --- ")

#zorunlu, *i **x
def create_report(format, *categories, **details):
    print(f"=== {format} Türünde Rapor oşulturuluyor ===")
    print("="*100)
    if categories:
        print(f"Kategoriler: {','.join(categories)}")
    
    print("Detaylar:")
    for key,value in details.items():
        if isinstance(value,(int,float)) and key.endswith(("_tutari", "_fiyat","_maas")):
            print(f"$$ {key}:{value:.2f} TL")
        elif isinstance(value,(int,float)) and key.endswith("_sayisi"):
            print(f"!! {key}:{value:,} adet")
        else:
            print(f"** {key}:{value}")
    print("="*100)


create_report("PDF","Pazarlama","Satış",aylik_satis=15000, hedef_tutari=10000,donem_bilgisi="qt3")


    
 











