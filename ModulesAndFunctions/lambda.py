from functools import reduce


def square_normal(x):
    return x ** 2

lambda_square = lambda x: x**2 

print("Lambda ile 3'ün karesi:",lambda_square(3))
print("normal ile 3'ün karesi:",square_normal(3))

multiply = lambda x,y,z: x * y * z
print("3 x 8 x 4 = ",multiply(3,8,4))

fiyatlar = [100,250,500,375,450]
kdvli_fiyatlar = list(map(lambda fiyat: fiyat * 1.2,fiyatlar))
print(fiyatlar)
print(kdvli_fiyatlar)

employees = ["mehmet yılmaz","ayşe kaya","aylin aslım","şeyma ünver","ğazal çekoslovakya"]
normalized = list(map(lambda name: name.title(),employees))
print(employees)
print(normalized)

print()
print("="*50 + " Filter " + "="*50)

numbers = range(1,11)
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print("çift sayılar:",even_numbers)

emails = ["mehmet@gmail.com","ayse.kaya@Halkbank.com.tr","ayliaslim@outlook.com","seyma@halkbank.com.tr"]
company_emails = list(filter(lambda email: "halkbank.com.tr" in email.lower(), emails))
print(company_emails)

alt_company_emails = list(filter(lambda email: not email.endswith("outlook.com") and not email.endswith("gmail.com")  ,emails))
print(alt_company_emails)

calisanlar = [
    {"isim":"Türkay", "yas":45, "score":90},
    {"isim":"Nergiz", "yas":32, "score":86},
    {"isim":"Filiz", "yas":28, "score":100},
    {"isim":"Necati", "yas":38, "score":45},

]

yasa_gore_calisanlar = sorted(calisanlar,key=lambda calisan: calisan["yas"])
print(yasa_gore_calisanlar)

sayilar = [2,3,4,5]
carpim = reduce(lambda x,y: x*y,sayilar)
print(carpim)

words = ["python","çok","güçlü","ve","esnek"]
sentence = reduce(lambda x,y:x+ " "+y,words)
print(sentence)

## zip kullanımı:
isimler = ["Ahmet","Türkay","Filiz"]
maaslar = [100000, 75000, 90000]
departmanlar = ["IT","Pazarlama","Finans"]

calisan_bilgileri = list(zip(isimler,maaslar,departmanlar))

print(calisan_bilgileri)
print(type(calisan_bilgileri))

for isim, maas, departman in calisan_bilgileri:
    print(f"{isim} {maas} {departman}")

calisan_dict = dict(zip(isimler,maaslar))
print(calisan_dict, type(calisan_dict))

#enumerate (sıralama)
print (enumerate(calisan_bilgileri,start=1))
for calisan in enumerate(calisan_bilgileri, start=1):
    print(f"{calisan[0]} {calisan[1][0]} ")

# All() Tüm element üzerinde çalışan kriterler True ise
numbers = [2,4,7,8,10]
is_all_even= all(number % 2 == 0 for number in numbers)
print("Hepsi çift mi?",is_all_even)

project_criteria={
    "budged_approved":True,
    "tech_approved":True,
    "availability":True,
    "manager_approved":True
}

is_project_approved = all(project_criteria.values())
if is_project_approved:
    print("proje onaylandı")

rand_nums = [1,2,3,5]
any_even = any(num % 2 ==0 for num in rand_nums)
