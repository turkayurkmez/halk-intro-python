    #           0                  1                 2             3       
books = ["Benim Adım Kırmızı","Şeker Portakalı","Satranç", "Tutunamayanlar"]
print(books[0])

#list'in her elemanı farklı tipte olabilir.
prouct_infos = ["Güneş Gözlüğü","Aksesuar",1500,True]


print(prouct_infos)
# Liste İşlemleri
print(" --------------- Liste İşlemleri -----------------")
numbers = [10,15,25,30,50,50]
print("Orijinal liste:",numbers)
numbers.append(70)
print("Append'den sonra liste:",numbers)

numbers.insert(2,65)
print("Insert'den sonra liste:",numbers)

numbers.remove(50)
print("Remove'dan sonra liste:",numbers)

del numbers[0]

print("del işleminden sonra liste:",numbers)

last_item = numbers.pop()
print("Çıkan son eleman:",last_item)
print("Eleman çıktıktan sonra liste:",numbers)

list1 = [1,2,3]
list2 = [4,5,6]
merge_list = list1 + list2
print("Birleşik liste:",merge_list)

print("............... Liste kopyalama ....................")

a = [1,2,3]
b = a
c = a.copy()
a[0] = 100
print("Orijinal a:", a)
print("Referans kopya b:",b)
print("c değer kopyası:", c)

