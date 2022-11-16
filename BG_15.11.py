

liste=[]
#liste=list()

eleman_sayisi=int(input("Eleman sayısını girin"))
toplam=0
for i in range(0,eleman_sayisi):
    eleman=int(input("Eleman girin"))
    liste.append(eleman)
    #liste.insert(i,eleman)
    #toplam=toplam+eleman
    
print(liste)

boyut=len(liste)

for i in range(0,boyut):
    toplam=toplam+liste[i]

print("Eleman toplamı =",toplam)

#╚----------------------------------
liste=[]

eleman_sayisi=int(input("Eleman sayısını girin"))
toplam=0
for i in range(0,eleman_sayisi):
    eleman=int(input("Eleman girin"))
    liste.append(eleman)
    
    
for i in range(0,eleman_sayisi):
    toplam=toplam+liste[i]
    
ortalama=toplam/eleman_sayisi
sayac=0

for i in range(0,eleman_sayisi):
    if liste[i]>ortalama:
        sayac=sayac+1
        print(liste[i])
        
print("Ortalama üzerinde", sayac," adet sayı vardır.")

#--------------------------------------------------------

liste1=[]
liste2=[]

eleman_sayisi=int(input("Eleman sayısını girin"))

for i in range(0,eleman_sayisi):
    eleman=int(input("Eleman girin"))
    liste1.append(eleman)
    
for i in range(0,eleman_sayisi):
    eleman=int(input("Eleman girin"))
    liste2.append(eleman)

esitMi=True
for i in range(0,eleman_sayisi):
    if liste1[i]!=liste2[i]:
        esitMi=False
        break
    
if esitMi:
    print("İki liste eşit")
else:
    print("İki liste eşit değil")





















