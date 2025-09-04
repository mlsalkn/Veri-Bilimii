print("\n--- SORU 2: Armstrong Sayısı ---")

def armstrong_kontrol(sayi):
    """Bir sayının Armstrong sayısı olup olmadığını kontrol eder"""
    str_sayi = str(sayi)
    basamak_sayisi = len(str_sayi)
    toplam = sum(int(basamak) ** basamak_sayisi for basamak in str_sayi)
    return toplam == sayi

# Test
test_sayilari = [153, 371, 9474, 123, 1634]
for sayi in test_sayilari:
    result = armstrong_kontrol(sayi)
    print(f"{sayi} Armstrong sayısı mı? {result}")
