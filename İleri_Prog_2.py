'''
#1-10 arası sayıların toplamı 
toplam=0
for i in range(0,11):
    toplam=toplam+i

print("Toplam =",toplam)

#while 
toplam=0
i=0
while i<11:
    toplam=toplam+i
    i=i+1
print("Toplam =",toplam)
# klavyeden girilen sayıya kadar olan sayıların toplamı
a=int(input("Bir sayı girin"))
toplam=0
while a>0:
    toplam=toplam+a
    a=a-1
print("Toplam =",toplam)

Cift_toplam=0
Tek_toplam=0
i=0
while i<11:
    if i%2==0:
        Cift_toplam=Cift_toplam+i
    else:
        Tek_toplam=Tek_toplam+i
    i=i+1
    
print("Tek sayıların toplamı =",Tek_toplam)
print("Çift sayıların toplamı =",Cift_toplam)


sayi=int(input("Bir sayı girin"))

birler=sayi%10
yuzler=(int)(sayi/100)
onlar_1=(int)(sayi/10)
onlar=onlar_1%10

print("Yüzler ",yuzler," Onlar ", onlar," Birler",birler)


sayi=int(input("Faktoriyeli hesaplanacak sayıyı girin"))
carpim=1
for i in range(1,sayi+1):
    carpim=carpim*i
    
print("Faktoriyel =" , carpim)

sayi=int(input("Faktoriyeli hesaplanacak sayıyı girin"))
carpim=1
while sayi>0:
    carpim=carpim*sayi
    sayi=sayi-1
print("Faktoriyel =" , carpim)

    '''

  