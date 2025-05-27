import mathFunc
#alternatif: Tüm fonksiyonlar değil, sadece kullanacaklarınız:
from mathFunc import add, subtract
from hangman import hangman_game

#print(__name__)
if __name__ == "__main__":
    print("Büyük uygulamanızın ilk ayağa kalkan kısmı burası olacak!")
    toplam = add(8,12)
    print(toplam)
    hangman_game()
    

