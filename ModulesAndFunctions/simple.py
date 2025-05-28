import datetime
def get_today_date():
    """Bu günün tarihini döndürür"""
    today = datetime.date.today()
    return f"{today.day}/{today.month}/{today.year}"

def get_current_time():
    """Şu anki saati döndürür """
    currentTime = datetime.datetime.now()
    return f"{currentTime.hour:02d}:{currentTime.minute:02d}"

def kdvHesapla(fiyat, oran):
    return fiyat * (1+oran)
