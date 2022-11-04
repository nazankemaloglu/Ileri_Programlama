
'''
vize=int(input("Vize notunu girin"))
final=int(input("Final notunu girin"))

ortalama=(vize*0.4)+(final*0.6)
print(ortalama)
if ortalama>40:
    print("Geçtiniz")
else: print("Kaldınız")


kelime="Python"
print(len(kelime))

taban=int(input("Tabanı girin"))
us=int(input("Üssü girin"))
carpim=1
for i in range(0,us):
    carpim=carpim*taban
    
    
print(taban,"'ın ",us,"inci kuvveti =",carpim)
print(taban**us)

import math 
print(int(math.pow(2, 5)))
 


sifirMi=True
eb=0
ek=0
while sifirMi:
    
    sayi=int(input("Bir sayı girin"))
    if sayi==0:
        break
    else:
        if sayi>eb:
            eb=sayi
        elif sayi<ek:
            ek=sayi
            
print("En büyük",eb)
print("En küçük",ek)


ad_soyad=input("Adınız ve soyadınızı girin")
yas=int(input("Yaşınızı girin"))
if yas>40:
    print("Yas sınırını aştınız.")
    print("Mülakat başarısız")
else:
    cevap=input("İngilizce ve ya Fransızca biliyor musunuz? E/H")
    if cevap=="H":
        print("Dil şartını sağlamıyorsunuz")
        print("Mülakat başarısız")
    elif cevap=="E":
        print("Tebrikler" , ad_soyad," Mülakat başarılı")
    else: print("Yanlış giriş")
'''

kelime1=input("1. Kelimeyi girin")
kelime2=input("2. Kelimeyi girin")

for i in kelime1:
    if i not in kelime2:
        print(i)
    
    








