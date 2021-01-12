#kdc= Katma değer ciro
#tsm= Toplam satış miktarı
#hm= Hammadde maliyeti
#bom= Bakım onarım giderleri
#sg= Sevkiyat giderleri
#sahg= Satın alınan hizmet giderleri
def kdc(tsm,hm,bom,sg,sahg):
    global kdc
    kdc = tsm -(hm+bom+sg+sahg)
    return kdc
x=int(input("Toplam satış miktarını giriniz:"))
y=int(input("Hammadde maliyetini giriniz:"))
z=int(input("Bakım onarım giderlerini giriniz:"))
n=int(input("Sevkiyat giderlerini giriniz:"))
t=int(input("Satın alınan hizmet giderlerini giriniz:"))
l=kdc(x,y,z,n,t)
if(kdc>=1000):
    print("İşletme katma değer cirosu yüksektir. Katma değer cironuz:",kdc)
elif(kdc>=500 and kdc<=999):
    print("İşletme katma değer cirosu normaldir. Katma değer cironuz:",kdc)
else:
    print("İşletme katma değer cirosu düşüktür. Katma değer cironuz:",kdc)
