'''
#1-10 arası sayıların toplamı
toplam=0
for i in range(0,11):
    toplam=toplam+i
print(toplam)

#1-10 arası tek sayıların toplamı
toplam=0
for i in range(0,11):
    if i%2==1:
        toplam=toplam+i
print(toplam)

i=0
toplam=0
while i<11:
    toplam=toplam+i
    i=i+1
print(toplam)

sayi=int(input("Bir sayı girin"))
carpim=1
for i in range(1,sayi+1):
    carpim=carpim*i
print(carpim)

sayi=int(input("Bir sayı girin"))
carpim=1

while sayi>0:
    carpim=carpim*sayi
    sayi=sayi-1
print(carpim)
'''  

dogruSayisi=int(input("Doğru sayısını girin"))
yanlisSayisi=int(input("Yanlış sayısını girin"))

dogruPuan=0
yanlisPuan=0
toplamPuan=0

toplamSoru=dogruSayisi+yanlisSayisi

if toplamSoru==10:
    dogruPuan=dogruSayisi*10
    yanlisPuan=yanlisSayisi*-5
    toplamPuan=yanlisPuan+dogruPuan
    print("Toplam puanınız =",toplamPuan,"tir.")
else:
    print("Soru sayılarını kontrol edin")
    







