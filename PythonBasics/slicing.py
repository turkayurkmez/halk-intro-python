fruits = ["elma","armut","kivi","muz","çilek","erik","üzüm","incir"]
print("Bütün meyveler:",fruits)
print("Toplam meyve sayısı:",len(fruits))

print("-2 index'li eleman:", fruits[-2])
print("İlk üç:", fruits[0:3])
print("İlk üç alternatif:", fruits[:3])
print("ikinci indeks'den 5. İndexe kadar", fruits[2:5])
print("4. indeks'den son elemana kadar", fruits[4:])

print("Son üç eleman", fruits[-3:])

print("2'şer atlayarak meyve listesi:", fruits[::2])

print("Acaba ne olur?: ", fruits[::-1])

#liste[başlangıç:bitiş:adım]