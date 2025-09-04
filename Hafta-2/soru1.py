sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    durum = "Pozitif"
elif sayi < 0:
    durum = "Negatif"
else:
    durum = "Sıfır"

if sayi % 2 == 0:
    tek_cift = "Çift"
else:
    tek_cift = "Tek"

print(f"{durum} {tek_cift}")