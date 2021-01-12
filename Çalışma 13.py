gunlukuretilen=200
gunlukdefolu=0
toplamdefolu=0
i=0
while(gunlukdefolu<=gunlukuretilen*0.20):
    gunlukdefolu=int(input("Günlük defolu ürün miktarı:"))
    toplamdefolu=toplamdefolu+gunlukdefolu
    i=i+1
    if(gunlukdefolu>gunlukuretilen*0.20):
        print("defolu ürün sayısı limiti aştı")
        break

    print(i,"günlük","defolu ürün sayısı:",toplamdefolu)
