#m2016= 2016 yılını müşterilerle çalışma süresi
#m2017= 2017 yılını müşterilerle çalışma süresi
#c2016= 2016 yılı çalışma süresi
#t2016= 2016 yılı toplam müşteri sayısı
#c2017= 2017 yılı çalışma süresi
#t2017= 2017 yılı toplam müşteri sayısı
c2016=170
t2016=50
c2017=c2016 + 50
t2017=t2016 + 20
def m2016(c2016,t2016):
    m2016 = c2016 / t2016
    return m2016
def m2017(c2017,t2017):
    m2017 = c2017 / t2017
    return m2017
hesapla=m2016(c2016,t2016)-m2017(c2017,t2017)
sonuc=format(float(hesapla),".3f")
print("2016-2017 yılları arasındaki müşterilerle çalışma sayısı farkı:",sonuc)
