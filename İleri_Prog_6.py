'''
#Klavyeden girilen bir şifrenin karakterlerini kontrol ederek girilen şifrenin 4 karakter olana kadar yeni şifre isteyen, girilince de doğru şifreyi ekranda gösteren python kodunu yazınız.

kontrol=True
while kontrol:
    sifre=input("Şifrenizi girin")
    uzunluk=len(sifre)
    if uzunluk==4:
        print("Şifreniz oluşturuldu")
        kontrol=False
    else:
        print("Şifreyi yeniden girin")
    

kalinan_saat=int(input("Kaldığınız saati girin"))
toplam_ucret=0
if kalinan_saat<=1:
    toplam_ucret=5
elif (kalinan_saat>1) and (kalinan_saat<=5):
    toplam_ucret=kalinan_saat*4
elif kalinan_saat>5:
    toplam_ucret=kalinan_saat*3
    
print("Ödeyeceğiniz miktar =",toplam_ucret)
 '''   

kontrol=True
turkce_karakter="ığüşöçĞÜİÖÇ"

while kontrol:
    sifre=input("Şifrenizi girin")
    for i in sifre:
        if i not in turkce_karakter:
             print("Şifreniz oluşturuldu")
             kontrol=False
        else:
             kontrol=False
             print("Türkçe karakter kullanmayın")