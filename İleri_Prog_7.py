#Girilen vize ve final notu ortalaması hesaplayan Python örneği?


vize =int(input("Vize notunuzu girin"))
final =int(input("Final notunuzu girin"))

ortalama=(vize*0.4)+(final*0.6)

if ortalama<=40:
    print("Kaldınız")
else:
    print("Geçtiniz")
    
    
#---------------------------------------------
#Klavyeden girilen taban ve üs değerine göre o sayının üssünü hesaplayan ve sonucu ekranda gösteren python kodunu yazınız.

taban=int(input("Tabanı girin"))
us=int(input("Üs girin"))

carpim=1

for i in range(0,us):
    carpim=carpim*taban
    
print(taban, " ün ",us," inci kuvveti =", carpim,"dir.")


import math

sonuc=math.pow(5, 3)
print(sonuc)
#----------------------------------------------------------------------

enBuyuk=0
enKucuk=0

sifirMi=True

while sifirMi:
    sayi=int(input("Bir sayı girin"))
    if sayi ==0:
        sifirMi=False
    elif sayi<enKucuk:
        enKucuk=sayi
    elif sayi>enBuyuk:
        enBuyuk=sayi
        
print("En büyük =",enBuyuk)
print("En küçük =",enKucuk)

#█------------------------------------------------------------------

ad_soyad=input("Adınız ve soyadınızı girin")
yas=int(input("Yaşınızı girin"))
if yas>40:
    print("Yas sınırını aştınız.")
    print("Mülakat başarısız")
else:
    cevap=input("İngilizce ve ya Fransızca biliyor musunuz? E/H")
    if cevap=="H" or cevap=="HAYIR" or cevap=="Hayır":
        print("Dil şartını sağlamıyorsunuz")
        print("Mülakat başarısız")
    elif cevap=="E":
        print("Tebrikler" , ad_soyad," Mülakat başarılı")
    else: print("Yanlış giriş")

#-----------------------------------------------------

kalinan_saat=int(input("Kaldığınız saati girin"))
toplam_ucret=0
if kalinan_saat<=1:
    toplam_ucret=5
elif (kalinan_saat>1) and (kalinan_saat<=5):
    toplam_ucret=kalinan_saat*4
elif kalinan_saat>5:
    toplam_ucret=kalinan_saat*3
    
print("Ödeyeceğiniz miktar =",toplam_ucret)

#------------------------------------------------------

metin1=input("Bir string girin")
metin2=input("Bir string girin")

for i in metin1:
    if i not in metin2:
        print(i)
        
        




