import mathFunc
#alternatif: Tüm fonksiyonlar değil, sadece kullanacaklarınız:
from mathFunc import add, subtract
from hangman import hangman_game
#from simple import get_current_time, get_today_date
import simple
import tuplereturn
import log

#print(__name__)
if __name__ == "__main__":
    print("Büyük uygulamanızın ilk ayağa kalkan kısmı burası olacak!")
    toplam = add(8,12)
    print(toplam)
    #hangman_game()
    
    print(f"{simple.get_today_date()} tarihi ve {simple.get_current_time()} anında işlem gerçekleştirildi")

    fiyatlar = [100,250,750,1000,75]
    kdvli_fiyatlar= []
    for fiyat in fiyatlar:
       kdvliFiyat = simple.kdvHesapla(fiyat,0.2)
       kdvli_fiyatlar.append(kdvliFiyat)
    
    print("Normal fiyatlar:",fiyatlar)
    print("KDV'li fiyatlar:",kdvli_fiyatlar)

    sales_list = [15000, 24000, 24750, 32600]
    total, avg, max,min, count =  tuplereturn.employee_performance(sales_list)
    print("Personelin performans raporu:")
    print("Toplam satış:",total)
    print("Ortalama satış:",avg)
    print("En yüksek satış:",max)
    print("En düşük:",min)
    print("Toplam adet:",count)

    log.log_register("Uygulama başlatıldı....")
    log.log_register("Kullanıcı girişi!","user@test.com",level="SUCCESS")
    log.log_register("Hata oluştu:", "Veritabanı bağlantısı kurulamadı",level="ERROR", file="dosya.log")
    






