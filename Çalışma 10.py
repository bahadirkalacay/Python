sm=10000
a=100
s=500
ay=1
while(sm>0):
    print(ay,"inci ayda stok miktarı",sm)
    sm+=a-s
    ay+=1
    if(sm<=0):
        print(ay,"inci ayda stoklar sıfırlanacaktır.")
