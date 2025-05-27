print("="*60)
print("1. Temel Kullanım:")
language = "Python"
for letter in language:
    print("Harf:", letter)

weathers = [20,15,-5,22,-3,0,-9]
colds = []
for heat in weathers:
    if heat < 0:
      colds.append(heat)

print(weathers)
print(colds)

for x in range(1,21):
    #ternary operatör:
    result ="Çift" if x % 2 == 0 else "Tek"    
#    if x % 2 == 0:
#        result = "Çift"
#    else:
#       result = "Tek"  
    print(f"{x} -> {result}")

#Sıralı olarak koleksiyon kullanımı:
participants = ["Arzu","Enes","Batuhan","Türkay"]
print("enumerate kullanarak sıralama:")
for order,participant in enumerate(participants,10):
    print(f"{order}. {participant}")

#1'den 100'e kadar var olan asal sayılar:
prime_numbers = []
for number in range(1,101):
   
    isPrime = True
    for division in range(2,number):
        if number % division == 0:
            isPrime = False
            break
    if isPrime:
        prime_numbers.append(number)
print(prime_numbers)

for order,prime in enumerate(prime_numbers,1):
    print(f"{order}....{prime}")


names = ["Yeşim","Mehmet","Aytuğ"]
ages = [45,30,19]
cities = ["Ankara","İstanbul","İstanbul"]
mergedList = list(zip(names,ages,cities))
print(mergedList)
for orderNo,value in enumerate(mergedList,1):
    print(f"{orderNo}. {value[0]} isimli kişi, {value[1]} yaşında ve {value[2]} şehrinde.")


#bir dict. senaryosu:
countries = ["Türkiye","Avusturya","Türkiye","İngiltere","Almanya","Almanya","Almanya","Türkiye","İsveç","Türkiye"]
country_analysis = {}
for country in countries:
    if country not in country_analysis:
        count = countries.count(country)
        country_analysis[country] = count
    
print(country_analysis)

