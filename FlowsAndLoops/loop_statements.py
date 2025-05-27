#break, continue ve pass

#sadece poizitif sayıları topla:
numbers = [45,-9,13,-4,1,-5,22,14]
positive_total=0
for number in numbers:
    if number < 0:
        continue
    positive_total += number
    print(f"{number} sayısı toplama ekleniyor. Sonuç:{positive_total}")

print("Toplam",positive_total)
#pass: hiçbir şey yapma!

for number in numbers:
    if number % 2 == 0:
        pass
        print("Hiçbir şey yapılmadı... Pas geçtik")
    else:
        print("Tek sayı")

#break: çık
#continue: bir sonrakinden devam et
#pass: Hiçbir şey yapma (ama sonradan düzeltilecek işlerde)
