"""

Bölüm 1: Veri Tipleri
1. Kullanıcıdan adını, yaşını ve boyunu (float) input() ile alınız. Bu bilgileri uygun veri
tiplerinde değişkenlerde saklayınız ve ekrana anlamlı bir şekilde yazdırınız.
2. Bir öğrencinin notlarını (Matematik, Fizik, Kimya) int tipinde değişkenlere atayın.
Ortalamasını float tipinde hesaplayıp ekrana yazdırınız.
3. Bir string değişkeni tanımlayın. Bu stringin ilk ve son karakterini, uzunluğunu ve ters
çevrilmiş halini ekrana yazdırınız  """
#1
a= input("lütfen adınızı giriniz:")
print("ad:",a)

b=float(input("lütfen ysşınızı giriniz:"))
print("yasınız:",b)

c=float(input("boyunuzu giriniz:"))
print("boy:",c)
#stringte int kullanmıyoruz.
#2
a=int(input("lütfen matematik notunuzu giriniz:"))
print("mat not:",a)
b=int(input("lütfen fizik notunuzu giriniz:"))
print("fizik not",b)
c=int(input("lütfen kimya notunuzu giriniz:"))
print("kimya not:",c)

ortalama=(a+b+c)/3
print("ortalama:",ortalama)
#3
metin="melisa"

ilk=metin[0]
son=metin[-1]
uzunluk=len(metin)
ters=metin[::-1]

print("metin:",metin)
print("metin ilk harf:",ilk)
print("metin son harf :",son)
print("metin uzunluk:",uzunluk)
print("metin ters:",ters)
