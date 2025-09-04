
"""4. Kullanıcıdan iki sayı alınız. Bu sayılar üzerinde toplama, çıkarma, çarpma, bölme ve mod 
işlemleri yapınız. 
5. Bir öğrencinin ortalaması 50’den büyükse 'Geçti', değilse 'Kaldı' çıktısını veren bir 
program yazınız. (Karşılaştırma ve mantıksal operatörler kullanılacak.) 
6. Kullanıcıdan yaşını alınız. Eğer yaş 18’den büyükse 'Ehliyet alabilirsiniz', değilse 'Ehliyet 
alamazsınız' çıktısı veriniz. 
7. Bir ürünün fiyatını (float) ve indirim oranını (yüzde) alınız. İndirimli fiyatı hesaplayıp 
ekrana yazdırınız. (Aritmetik operatörler kullanılacak.) 
8. True ve False değerlerini içeren değişkenlerle mantıksal operatörleri (and, or, not) 
uygulayarak örnekler yapınız ve sonuçlarını ekrana yazdırınız."""
#4
a,b=map(int,input("lütfen 2 sayi giriniz:").split())
print("sayi1:",a)
print("sayi2:",b)
"""map() bir dönüştürme fonksiyonudur.

İlk parametreye bir fonksiyon (ör. int, float) alır,

İkinci parametreye ise iterable (liste, string, tuple vs.) alır.
input() ile aldığımız veri string tipindedir.

split() metodu, stringi boşluklara göre parçalara ayırır ve liste döner."""
print("{}+{} toplamı={} dır".format(a,b,a+b))
print("{}*{} carpma={} dır".format(a,b,a*b))
print("{}/{} bölme={} dır".format(a,b,a/b))
print("{}-{} cıkarma={} dır".format(a,b,a-b))
print("{}%{} mod={} dır".format(a,b,a%b))
#5
a,b=map(int,input("lütfen 2 sayi giriniz:").split())
print("sayi1:",a)
print("sayi2:",b)

ortalama=(a+b)/2
if(ortalama>50):
    print("Geçti")
else:
     print("kaldı")

#6
yas=int(input("lütfen yaşınısı giriniz:"))
print("yasınız:",yas)
if(yas>=18):
     print("ehliyet alabilirsiniz.")
else:
     print("ehliyet alamazsınız.")

#7
fiyat=float(input("ürün fiyatını giriniz:"))
print("ürünün fiyatı:",fiyat)
indirim=float(input("indirim oranı (%):"))

print("indirim oranı:",indirim)

indirimli_fiyat=fiyat-(fiyat*indirim/100)
print("indirimli fiyat:",indirimli_fiyat)

#8
#değişkenler
a=True
b=False
#mantıksal operatörler örnekleri
print("a and b=",a and b )
print("a or b=",a or b )
print("not a=",not a)
print("not b=",not b)
#biraz daha örnek 
print("(a and true)=",a and True)
print("(a or false)=",a or False)
print ("(a or not b )=",a or not b)
print("(a and not b)=",a and not b)

