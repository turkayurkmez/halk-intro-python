colors = {"kırmızı","mavi","yeşil","sarı","mavi"}
print("renkler kümesi (set):",colors)
print("renkler kümesinin eleman sayısı:",len(colors))

cities = ["Eskişehir","Yozgat","Yozgat","Bursa","Denizli","Bursa"]
cities_set = set(cities)

cities_list = list(set(cities))

print("Şehirler kümesi:",cities_set)
print("Eşsiz Liste:", cities_list)
print("Eşsiz ilk şehir:",cities_list[0])



bos_kume = set()

print("Tüm renkler")
for color in colors:
    print(color)

print("Bir elemanın kümedeki varlığını nasıl kontrol ediyoruz..........")
print("'mavi' değeri kümede var mı? ","mavi" in colors)
print("'pembe' değeri kümede var mı? ","pembe" in colors)


colors.add("mor")
colors.update(['pembe','turuncu','lacivert'])
colors.remove("turuncu")
print("renklerin son hali:", colors)
try:
    colors.remove("beyaz")
except KeyError as k :
    print("Aradığınız renk kümede yok!")

#eğer bulamazsa hata vermesin istiyorsanız:
print("Siyahı silmeye çalışıyoruz:")
colors.discard("siyah")

element = colors.pop()
print("Pop ne döndürür: ", element)
print("Renkler kümesi", colors)


print ("\n Küme İşlemleri" + "*"*60)
A ={1,2,3,4,5}
B ={4,5,6,7,8}

print("A Kümesi:", A)
print("B Kümesi:", B)

union  = A.union(B) # A | B 
print("Birleşim kümesi:", union) 

intersect = A.intersection(B) # alternatif : A & B
print("Kesişim kümesi:", intersect)

differentA = A.difference(B) #  A - B
differentB = B.difference(A)

print("A fark B", differentA)
print("B fark A", differentB)

print("A ve B simetrik fark:",A.symmetric_difference(B)) # A ^ B

C= {1,2}
#test = {["A","B","C"], [1,2,3]}
print(C)
print("C A'nın alt kümesi mi?: ", C.issubset(A) )
print("A C'nin üst kümesi mi?: ", A.issuperset(C) )
print("B ve C ayrık küme mi?: ", B.isdisjoint(C))


frozen = frozenset(A)
##frozen.add(20)

