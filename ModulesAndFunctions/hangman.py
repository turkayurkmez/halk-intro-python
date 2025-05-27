import random
# Amaç:
# Adam asmaca oyunu
# 1. bir kelime listesi içerisinden rastgele kelime seç.,
# 2. bu kelimeyi ---- biçiminde göster
# 3. Kullanıcıdan harf iste
# 4. Eğer harf varsa, kelimedeki yerini göster.
# 5. Hakkından bir azalt
# 6. Kelimeyi bilene dek devam etsin

def getRandomWord(word_list):
    """ Verilen kelime listesinden rastgele kelime döndürür"""
    return random.choice(word_list)

def displayPuzzle(word, guessed_letters):
    """ Kelime bulmacasını gösterir... """
    puzzle =""
    for letter in word:
        if letter in guessed_letters:
            puzzle+=letter + " "
        else:
            puzzle+="_ "
    return puzzle.strip()

def getGuess():
    while True:
        guess = input("Bir harf tahmin edin:").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Lütfen sadece harf girin")


def isRenewGame():
    while True:
        response = input("Tekrar oynamak ister misiniz (e/h)").lower()
        if response in ["e","h"]:
            return response == "e"
        else:
            print("Lütfen e ya da h giriniz!")


def hangman_game():
    """ Oyunu başlatan fonksiyon """
    word_list = ["menemen","salata","ayna","dolap"]
    word = getRandomWord(word_list)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\n kalan deneme: ",attempts)
        print("Tahmin edilen harfler:",guessed_letters)
        print("Kelime: ",displayPuzzle(word,guessed_letters))

        guess = getGuess()
    

        if guess in guessed_letters:
            print("Bu harfi daha önce söylediniz...")
            continue
        guessed_letters.append(guess)

        

        if guess not in word:
            attempts-=1
            print("Yanlış tahmin")
        
        if all(letter in guessed_letters for letter in word):
            print("Tebrikler! Kelime: ", word)
            break
    else:
        print("\n Üzgünüm hakkınızı kaybettiniz. Doğru kelime:",word)
    
    if isRenewGame():
        hangman_game()  


# word = getRandomWord(["python","csharp"])
# letter=""
# print(displayPuzzle(word,'p'))
#print(getGuess())
