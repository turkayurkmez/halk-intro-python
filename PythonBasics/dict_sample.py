plakalar = {}
# kullanıcı istediği sürece, plakalar içine yeni entry'ler ekler.
while True:
    plaka = input("Plaka kodunu girin (çıkmak için q): ")
    if plaka.lower() == 'q':
        break
    sehir = input("Şehir adını girin: ")
    if plaka in plakalar:
        print(f"{plaka} daha önce zaten eklenmiş...")        
    else:
        plakalar[plaka] = sehir
        print("Plaka kodu eklendi")

while True:
    plaka = input("aradığınız plaka kodunu girin (çıkmak için q): ")
    if plaka.lower() == 'q':
        break

    if plaka in plakalar:
        print(f"{plaka} plaka kodu: {plakalar[plaka]} şehrine aittir")
    else:
        print(f"Ne yazık ki {plaka} kodu sisteme kayıtlı değil.") 
   
print(plakalar)