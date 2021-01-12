#donem_basi=Dönem başı stoğu
#koltuk=Koltuk sayısı
#yatak=Yatak sayısı
#dolap=Dolap sayısı
#donem_sonu=Dönem sonu stoğu
#ort=Ortalama stok
def donem_basi(koltuk,yatak,dolap):
    global donem_basi
    donem_basi= koltuk+yatak+dolap
    return donem_basi
x=int(input("Koltuk sayısını giriniz:"))
y=int(input("Yatak sayısını giriniz:"))
z=int(input("Dolap sayısını giriniz:"))
t=donem_basi(x,y,z)
print("Dönem başı stoğunuz:",donem_basi)
def donem_sonu(koltuk,yatak,dolap):
    global donem_sonu
    donem_sonu= koltuk+yatak+dolap
    return donem_sonu
k=int(input("Koltuk sayısını giriniz:"))
l=int(input("Yatak sayısını giriniz:"))
m=int(input("Dolap sayısını giriniz:"))
n=donem_sonu(k,l,m)
print("Dönem sonu stoğunuz:",donem_sonu)
ortalama=(donem_basi + donem_sonu)/2
print("Ortalama stoğunuz:",ortalama)
