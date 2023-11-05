def Toplama(x, y):
    return x + y

def Çıkarma(x, y):
    return x - y

def Çarpma(x, y):
    return x * y

def Bölme(x, y):
    if y == 0:
        return "Sıfıra bölme hatası"
    else:
        return x / y

while True:
    print("Lütfen yapmak istediğiniz işlemi seçiniz.")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")
    
    secim = input("Seçiminiz (1/2/3/4/5): ")
    
    if secim == "5" :
        print("Hesap makinesi kapanıyor")
        break
    
    sayi1 = float(input("Birinci sayıyı giriniz: "))
    sayi2 = float(input("İkinci sayıyı giriniz: "))
    
    if secim == "1":
        print("İşlemin sonucu", Toplama(sayi1, sayi2))
    
    elif secim == "2":
        print("İşlemin sonucu", Çıkarma(sayi1, sayi2))
    
    elif secim == "3":
        print("İşlemin sonucu", Çarpma(sayi1, sayi2))
    
    elif secim == "4":
        print("İşlemin sonucu", Bölme(sayi1, sayi2))
    
    else:
        print("Geçersiz Sayı")