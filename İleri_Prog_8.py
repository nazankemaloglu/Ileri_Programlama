#7. HAFTA

liste=[]

elemansayisi=int(input("Eleman sayısını girin"))

toplam=0
for i in range(0,elemansayisi):
    eleman=int(input(" elemanı girin"))
    liste.append(eleman)
    toplam=toplam+eleman
    
    
print("Liste = ",liste)
print("Elemanların toplamı =",toplam)

#----------------------------------------------
import random

liste=[]
count=0

for i in range(0,10):
    sayi=random.randint(0,100)  
    liste.append(sayi)
    

for i in range(0,10):
    if liste[i]<50:
        count=count+1
        
print("50'den küçük eleman sayısı =",count)
print(liste)
    

