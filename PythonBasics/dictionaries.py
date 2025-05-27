film = {
    "title":"Yüzüklerin Efendisi: Yüzük Kardeşliği",
    "director":"Peter Jackson",
    "year": 2001,
    "acts":["Elijah Wood","Orlando Bloom"],
    "rating":9.0,
    "oscar_count":4
}

print(f"film nesnesi: {type(film)} tipinde ve değeri: {film}")
print("Filmin adı:",film["title"])
print("Film adı (get):",film.get("title"))
print("İlk oyuncu:", film.get("acts")[0])

#yeni entry eklemek:
film["duration"] = 180
print(f"film nesnesi değeri: {film}")
#key denetimi:
print("duration bilgisi var mı?:", "duration" in film)
print("filmin özeti:", film.get("summary","Summary bilgisi bulunamadı"))
film["duration"] = 150

for key,value in film.items():
    print(key,value)

#son entry'yi (LIFO) silme:
choosingItem = film.popitem()
print(choosingItem)
print(film)

#1. Liste ve Dict dönüşümleri:
apps = ['pomodoro','todoList','notion','notion']
scores = [4.6, 3.9, 5.0,4.8]

app_analyze = zip(apps,scores)
print(f"app_analyze tipi: {type(app_analyze)}, değeri: {app_analyze}")
app_analyze_dict = dict(app_analyze)
print(f"app_analyze tipi: {type(app_analyze_dict)}, değeri: {app_analyze_dict}")

#2. Boş dictionary:
sample = {}
sample["key1"] = "value1"
sample["key2"] = "value2"

#3. dict() kullanmak:
sample2 = dict(title="Matrix",year=1999)

sample3 = dict([("title","Jurassic Park")("year","1995")])

