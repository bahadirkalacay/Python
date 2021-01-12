#ilk6=İlk 6 ay dönemi
#yg=Yazılım gelirleri
#fg=Finansman gelirleri
#usg=Ürün satış gelirleri
#cm=Çalışan masrafları
#kg=Kira giderleri
#dm=Donanım maliyeti 
#son6=Son 6 ay dönemi
#yk=Yıllık kar
def ilk6(yg,fg,usg,cm,kg,dm):
    gelir_ilk6=yg+fg+usg
    gider_ilk6=cm+kg+dm
    global kar_ilk6
    kar_ilk6= gelir_ilk6 - gider_ilk6
    return kar_ilk6
a = int(input("İlk 6 ayın yazılım gelirinizi giriniz:"))
b = int(input("İlk 6 ayın finansman gelirinizi giriniz:"))
c = int(input("İlk 6 ayın ürün satış gelirini giriniz:"))
d = int(input("İlk 6 ayın çalışan maaşlarını giriniz:"))
e = int(input("İlk 6 ayın kira giderlerini giriniz:"))
f = int(input("İlk 6 ayın donanım maliyetini giriniz:"))
g=ilk6(a,b,c,d,e,f)
print("İlk 6 ayın karlılık sonucu:",kar_ilk6)
def son6(yg,fg,usg,cm,kg,dm):
    gelir_son6=yg+fg+usg
    gider_son6=cm+kg+dm
    global kar_son6
    kar_son6= gelir_son6 - gider_son6
    return kar_son6
z = int(input("son 6 ayın yazılım gelirinizi giriniz:"))
x = int(input("son 6 ayın finansman gelirinizi giriniz:"))
l = int(input("son 6 ayın ürün satış gelirini giriniz:"))
v = int(input("son 6 ayın çalışan maaşlarını giriniz:"))
b = int(input("son 6 ayın kira giderlerini giriniz:"))
n = int(input("son 6 ayın donanım maliyetini giriniz:"))
m=son6(z,x,l,v,b,n)
print("son 6 ayın karlılık sonucu:",kar_son6)
yk=kar_ilk6+kar_son6
if(yk>=5000):
    print("İşletme çok karlıdır. Yıllık karınız:",yk)
elif(yk>=1000 and genelkar<5000):
    print("İşletme karı normaldir. Yıllık karınız:",yk)
else:
    print("İşletmenin karı azdır. Yıllık karınız:",yk)
