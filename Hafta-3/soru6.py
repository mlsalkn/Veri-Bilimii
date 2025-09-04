print("\n--- SORU 6: Gömülü Fonksiyonlar ---")
sayilar = [5, 12, 7, 18, 24, 3, 16]
print(f"Orijinal sayılar: {sayilar}")

# Çift sayıları filtrele
cift_sayilar = list(filter(lambda x: x % 2 == 0, sayilar))
print(f"Çift sayılar: {cift_sayilar}")

# Karelerini bul
kareler = list(map(lambda x: x**2, cift_sayilar))
print(f"Çift sayıların kareleri: {kareler}")

# Azalan sırada sırala
azalan_kareler = sorted(kareler, reverse=True)
print(f"Kareler (azalan sırada): {azalan_kareler}")