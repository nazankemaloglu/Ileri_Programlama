

yazi="Python üst düzey basit söz dizimine sahip, öğrenmesi oldukça kolay, modülerliği, okunabilirliği destekleyen, platform bağımsız nesne yönelimli yorumlanabilir bir script dilidir."

sesli="aeıioöuü"

for i in yazi:
     if i in sesli:
         print(i,end=",")
         
         
sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
sesliler=""
sessizler=""
a=input("bir metin giriniz")

for i in a:
     if i in sesli_harfler:
           sesliler=sesliler+i
     if i in sessiz_harfler:
           sessizler=sessizler+i

print("sesli harfler",sesliler)
print("sessiz harfler",sessizler)

harf="a"
sayac=0

for i in yazi:
     if i=="a":
         sayac=sayac+1
print("cümle içerisinde geçen a harfi sayısı: ",sayac)

a=True
poz=0
neg=0
while a:
    sayi=int (input())
    if sayi==0:
        a=False 
        break
    elif sayi>0:
        poz=poz+1
    else:
        neg=neg+1
            
print("Toplam",poz,"poztif",neg,"negatif sayı var")
        
harf=input()
sayac=0

for i in yazi:
     if i==harf:
         sayac=sayac+1
print("cümle içerisinde geçen a harfi sayısı: ",sayac)