reading_tens = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
reading_ones = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]

print("İki basamaklı bir sayı giriniz ")
number = int(input())
level_ten = number // 10
level_one = number % 10
print(reading_tens[level_ten],reading_ones[level_one])
