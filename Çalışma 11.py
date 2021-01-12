i=1
while True:
    girilen=int(input("3 e bölümünden kalan sayıyı bulmak istediğiniz sayıyı giriniz,çıkmak için sıfıra basınız"))
    i=girilen%3
    print(i)
    if(girilen==0):
        print("çıkmak istediniz")
        break
