print("\n--- SORU 7: Lambda İfadeleri ---")
kelimeler = ["veri", "bilim", "analiz", "yapayzeka", "python"]
print(f"Orijinal kelimeler: {kelimeler}")

sirali_kelimeler = sorted(kelimeler, key=lambda x: len(x))
print(f"Uzunluğa göre sıralı: {sirali_kelimeler}")