toplam = 0
sayac = 0

print("Sayıları girin (çıkmak için 0 girin):")

while True:
    try:
        sayi = float(input("Sayı: "))
        if sayi == 0:
            break
        toplam += sayi
        sayac += 1
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")

if sayac > 0:
    ortalama = toplam / sayac
    print(f"Girilen sayı adedi: {sayac}")
    print(f"Toplam: {toplam}")
    print(f"Ortalama: {ortalama:.2f}")
else:
    print("Hiç sayı girilmedi!")