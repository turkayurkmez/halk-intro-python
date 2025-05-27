import random
 
#Amaç sayısal loto için kullanılacak 6 farklı sayı üretmek.
lotto = []
# lotto 6 elemandan küçük olduğu sürece:
while len(lotto) < 6:
    random_number = random.randint(1,50)
    # kontrol et: rastgele sayı listede var mı?
    if random_number not in lotto:
        lotto.append(random_number)
    
print(lotto)
sorted_lotto = sorted(lotto)
print(sorted_lotto)