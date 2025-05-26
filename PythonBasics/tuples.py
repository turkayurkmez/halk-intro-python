days = ("Pazartesi","Salı","Çarşamba","Perşembe","Cuma")
print("İlk eleman:",days[0])
print("İlk üç eleman:",days[0:3])

try:
    days[0] = "Pazar"
except TypeError as e:
    print("Hata:",e)
    print("Tupple nesnesi immutable'dır değerini değiştiremezsiniz!")

single_element_tuple= ('pergel',)
print (type(single_element_tuple))

#veri paketleyerek tuple oluşturmak:
koordinat = 40.98, 29.02
print("Enlem:", koordinat[0])
print("Boylam:", koordinat[1])

latitude, longitude = koordinat
print("Paketten çıkan enlem:", latitude)
print("Paketten çıkan boylam:", longitude)

a,b = 5,10
print(f"Takastan önce a: {a}, b: {b}")
a,b = b,a
print(f"Takastan sonra a: {a}, b: {b}")

# Nerede tupple kullanırsınız?
  # Sabit koleksiyonlar (günler) -> immutable -> değişmez
  # Fonksiyondan birden fazla değer döndürmek isterseniz
  # Çoklu (a,b=b,a) atama işlemleri

