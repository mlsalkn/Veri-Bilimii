
print("\n--- SORU 1: Liste Metotları ---")
notlar = [85, 92, 76, 92, 100, 76, 85, 92]
print(f"Orijinal notlar: {notlar}")

# Benzersiz liste oluştur
benzersiz_notlar = list(set(notlar))
print(f"Benzersiz notlar: {benzersiz_notlar}")

# En yüksek ve en düşük not
en_yuksek = max(notlar)
en_dusuk = min(notlar)
print(f"En yüksek not: {en_yuksek}")
print(f"En düşük not: {en_dusuk}")

# Sıralama
sirali_notlar = sorted(notlar)
print(f"Sıralı notlar (küçükten büyüğe): {sirali_notlar}")