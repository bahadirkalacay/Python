stokmiktari=10000
satilan=0
alinan=0
i=0
while True:
    satilan=0+500
    alinan=0+100
    stokmiktari=(stokmiktari-satilan)+alinan
    i=i+1
    if(stokmiktari<=0):
        print(i,"ay sonra stoklarınız tükenecektir.")
        break
