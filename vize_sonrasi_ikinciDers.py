
# Faktoriyel hesaplayan fonksiyon
def faktoriyel(a):
    carpim=1
    for i in range(1,a+1):
        carpim=carpim*i
    print(carpim)    


def faktoriyel(a):
    carpim=1
    for i in range(1,a+1):
        carpim=carpim*i
    return carpim


sayi=int(input("Bir sayı girin"))
#faktoriyel(sayi)
print(faktoriyel(sayi))
degisken=faktoriyel(sayi)
#----------------------------------

#Ortalama üstü sayıları farklı diziye aktaran fonksiyon
import random as rn
liste1=[]
for i in range(0,10):
    sayi=rn.randint(0,100)
    liste1.append(sayi)
    #toplam=toplam+sayi


def ortalama_ustu_bul(liste1):
    toplam=sum(liste1)
    eleman_sayisi=len(liste1)
    ortalama=toplam/eleman_sayisi
    liste2=[]

    for i in range(0,eleman_sayisi):
        if liste1[i]>ortalama:
            liste2.append(liste1[i])

    return liste2
print(ortalama_ustu_bul(liste1))
print(liste1)
#-------------------------------------------------

#Liste içerisinde string ifade arayan fonksiyon
liste=['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
aranan=input("Bir ifade girin")

def metin_ara(liste,a):
    liste1=[x for x in liste if aranan in x]
    return liste1

print(len(metin_ara(liste,aranan)))
#----------------------------------------------

#Belirli bir strin içerisinde karakter sayısına göre eleman arama

cumle="Belirli bir düzende otomatik listeler oluşturmak için liste üreteçleri kullanılır."
karakter_sayisi=int(input("Karakter sayısı girin"))

def bul(cumle,a):    
    liste=cumle.split(" ")
    for i in liste:
        if len(i)>a:
            print(i)          
bul(cumle,karakter_sayisi)






    
