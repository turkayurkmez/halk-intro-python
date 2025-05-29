class Product:
    """ E-ticaret uygulama evreninden bir Ürün varlığının tanımı """


    def __init__(self, name,price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - {self.price} TL ({self.stock} adet)"
    
    def __repr__(self):
        """ Yazılımcı için detay bilgisi """
        return f"nesnenin detayı: Product (name={self.name}, price={self.price}, stock = {self.stock})"
    
    def __len__(self):
        return self.stock
    
    def __bool__(self):
        return self.stock > 0 
    
    def __eq__(self, value):
        print(f"{self} ve {value} karşılaştırılıyor")
        return self.name == value.name and self.price == value.price
    
    def __lt__ (self,value):
        return self.price < value.price
    
    def __gt__(self,value):
         """ > işareti... """
         return self.price > value.price
    
    def __add__(self,value):
        return self.price + value.price
    
    def __contains__(self, feature):
        """ in keyword'ü ile kontrol yapmak isterseniz bu function'u kullanırsın  """
        pass

    def __ge__(self, other):
        """ >= """
        pass

    def __ne__ (self, other):
        """ not (!=) """
        pass




    def display_product_info(self):
        """ Ürün bilgilerini gösterir """
        return f"{self.name} - {self.price} TL (Stok: {self.stock})"

    def check_stock(self):
        if self.stock > 50:
            return "Stokta yeteri kadar var"
        elif self.stock > 0:
            return "Kritik stok"
        else:
            return "Stokta yok!"
        