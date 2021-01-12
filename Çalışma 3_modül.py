def etkilesimOrani():
    global oran
    x=int(input("Beğeni sayısını giriniz:"))
    y=int(input("Yorum sayısını giriniz:"))
    z=int(input("Paylaşım sayısını giriniz:"))
    t=int(input("İçerik sayısını giriniz:"))
    k=int(input("Takipçi sayısını giriniz:"))
    oran=(((x+y+z)/t)/k)
    print("Etkileşim oranınız:",oran)

etkilesimOrani()

if oran<0.2:
    print("Başarısız")
else:
    print("Başarılı")
