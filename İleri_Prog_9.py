'''
liste=[]
#liste =list()

eleman_sayisi=int(input("Eleman sayısını girin"))
toplam=0
sayac=0
for i in range(0,eleman_sayisi):
    eleman=int(input("Elemanı girin"))
    liste.append(eleman)
    #liste.insert(i,eleman)
    #toplam=toplam+eleman
    
for i in range(0,eleman_sayisi):
    toplam=toplam+liste[i]
    
ortalama=toplam/eleman_sayisi
liste2=[]
for i in range(0,eleman_sayisi):
    if liste[i]>ortalama:
        sayac=sayac+1
        #print(liste[i])
        liste2.append(liste[i])
        
print(sayac," adet sayı ortalamanın üzerindedir. ")
print(liste2)
# ----------------------------------------------
liste1=[]
liste2=[]
boyut=int(input("Liste boyutunu girin"))

for i in range(0,boyut):
    eleman=int(input("1. liste Elemanı girin"))
    liste1.append(eleman)
    
for i in range(0,boyut):
    eleman=int(input("2. liste Elemanı girin"))
    liste2.append(eleman)
    
esitMi=True
for i in range(0,boyut):
    if liste1[i]!=liste2[i]:
        esitMi=False
        break
print(liste1)
print(liste2)
if esitMi:
    print("İki liste eşittir.")
else:
    print("İki liste eşit değildir.")
#--------------------------------------------
'''
sayi=int(input("Sayı girin"))

for i in range(1,sayi+1):
    if sayi%i==0:
        print(i)


