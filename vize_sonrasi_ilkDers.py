#Dizi içerisinde ortalama üstündeki sayıları 2. bir diziye aktarma
import random as rn

liste1=[]
toplam=0

for i in range(0,10):
    sayi=rn.randint(0,100)
    liste1.append(sayi)
    #toplam=toplam+sayi
    
eleman_sayisi=len(liste1)

for i in range(0,eleman_sayisi):
    toplam=toplam+liste1[i]
    
ortalama=toplam/eleman_sayisi

ortalama_ustu=[]

for i in range(0,10):
    if liste1[i]>ortalama:
        ortalama_ustu.append(liste1[i])

print(liste1)
print(ortalama)
print(ortalama_ustu)
        
#--------------------------------------------------------------

import random as rn

liste1=[]
toplam=0

for i in range(0,10):
    sayi=rn.randint(0,100)
    liste1.append(sayi)
print(liste1)
liste1.sort(reverse=False)
print(liste1)
#----------------------------------------
cumle="Belirli bir düzende otomatik listeler oluşturmak için liste üreteçleri kullanılır."
text=cumle.split(" ")

for i in text:
    if len(i)>7:
        print(i)
#-----------------------------------------------------------

#String içerisinde bir alt string arama

liste=['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
aranan_kelime="Geek"

sayac=len([a for a in liste if aranan_kelime in a])
print(sayac)


