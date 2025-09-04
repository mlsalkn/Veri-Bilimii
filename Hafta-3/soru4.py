print("\n--- SORU 4: Modüller ---")
rastgele_sayilar = [random.randint(1, 100) for _ in range(10)]
print(f"Rastgele sayılar: {rastgele_sayilar}")

ortalama = statistics.mean(rastgele_sayilar)
standart_sapma = statistics.stdev(rastgele_sayilar)
print(f"Ortalama: {ortalama:.2f}")
print(f"Standart sapma: {standart_sapma:.2f}")