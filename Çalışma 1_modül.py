def isletmeKar():
    gelir=int(input("İşletme gelirinizi giriniz:"))
    gider=int(input("İşletme giderinizi giriniz:"))
    hesapla=gelir-gider
    kar=format(float(hesapla),".2f")
    if (hesapla>0):
        print("İşletme",kar,"TL kardadır.")
    elif(hesapla==0):
        print("İşletme başabaş noktasındadır.")
    else:
        print("İşletmeniz",kar,"TL zarardadır.")
        
def adamBasiCiro():
    toplamCiro=int(input("İşletmenin toplam cirosunu giriniz:"))
    toplamCalisanSayisi=int(input("İşletmenin toplam çalısan sayısını giriniz:"))
    hesapla=toplamCiro/toplamCalisanSayisi
    print("İşletmenin adambaşı cirosu:",hesapla)
