print("="*60)
print("1. Temel Kullanım:")
language = "Python"
for letter in language:
    print("Harf:", letter)

weathers = [20,15,-5,22,-3,0,-9]
colds = []
for heat in weathers:
    if heat < 0:
      colds.append(heat)

print(weathers)
print(colds)

for x in range(1,21):
    #ternary operatör:
    result ="Çift" if x % 2 == 0 else "Tek"    
#    if x % 2 == 0:
#        result = "Çift"
#    else:
#       result = "Tek"  
    print(f"{x} -> {result}")
