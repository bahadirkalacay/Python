saat=1
while(saat>0):
    saat=int(input("haftalık personel çalışma saati giriniz"))
    if(saat>62):
        print("haftalık 22 saatten fazla personele mesai yaptırılamaz")
        break
        
    mesai=saat-40
    omaas=40*90+(mesai*9)
    print("ödenecek maaş=",omaas)
    
