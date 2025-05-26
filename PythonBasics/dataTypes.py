number = 54
number2 = -15

big_number = 123456789012345678901234567890

print("Tam sayı tipleri:")
print(f"number, {type(number)} tipinde. Değeri ise {number}")
print(f"number2, {type(number)} tipinde. Değeri ise {number2}")
print(f"big_number, {type(big_number)} tipinde. Değeri ise {big_number}")

some_value = None
print(type(some_value))
some_value = 'Türkay'
print(type(some_value))
some_value = 35
print(type(some_value))

# Float (ondalıklı) sayılar
pi = 3.14
scientific_display = 6.02e23
print(f"Bilimsel gösterim: {type(scientific_display)}: {scientific_display}")
print(f"Pi sayısı: {pi} ve tipi: {type(pi)}")

int_number = 9
convert_to_float = float(int_number)
convert_to_int = int(4.99)

print(f"\nTür Dönüşümleri")
print(f"{int_number} - {convert_to_float}")
print(f"4.99 -> {convert_to_int}")

complex_number = 3 + 4j
print(f"Değer: {complex_number}. Tip: {type(complex_number)}")

complex_number2 = complex(2,5)

print(f"Değer: {complex_number2}. Tip: {type(complex_number2)}")
print(f"Real kısmı: {complex_number2.real} imag ise {complex_number2.imag}")

print(f"Basit bölme: {15 / 2}")
print(f"Tam sayı bölme: {15 // 2}")

