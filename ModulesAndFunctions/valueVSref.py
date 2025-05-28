print("-------------------Immutable veri tipleri: int, float, string, tuple")
# number = 5
# print(id(number),number)
# number = 9
# print(id(number),number)
# print(number)
def change_number(number):
    print("Fonksiyona gönderilen sayı:", number)
    number *=2
    print("Değişimden sonra sayı:", number)
    return number

original_number = 50
print("Orijinal sayı:", original_number)
result = change_number(original_number)
print("Fonksiyon çalıştıktan sonra orijinal sayı:", original_number)
print("Fonksiyonun döndürdüğü değer:", result)


print("-------------------mutable veri tipleri: list, dict, set")


def add_item_to_list(list):
    print("Fonkisona gönderilen liste:",list)
    list.append('yeni eleman')
    list[0] = "Güncellendi"
    print("Fonksiyon sonucu:", list)

orijinal_liste = ["A","B","C"]
print("orijinal liste:",orijinal_liste)
add_item_to_list(orijinal_liste)
print("fonksiyon çalıştıktan sonra orijinal liste:",orijinal_liste)

