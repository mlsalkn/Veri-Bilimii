print("\n" + "=" * 60)
print("PROJE: KİTAP SATIŞ ANALİZ SİSTEMİ")
print("=" * 60)

# Veri
kitaplar = [
    {"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
    {"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil": 2020},
    {"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
    {"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
    {"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
    {"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500, "yil": 2021},
    {"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]

# 1. Fonksiyon Yazma
def en_cok_satan(kitaplar):
    """En çok satan kitabın bilgilerini döndürür"""
    return max(kitaplar, key=lambda x: x['satis'])

def yazar_satislari(kitaplar):
    """Her yazarın toplam satışını döndürür"""
    yazar_dict = {}
    for kitap in kitaplar:
        yazar = kitap['yazar']
        if yazar in yazar_dict:
            yazar_dict[yazar] += kitap['satis']
        else:
            yazar_dict[yazar] = kitap['satis']
    return yazar_dict

print("--- 1. Fonksiyon Sonuçları ---")
en_cok_satan_kitap = en_cok_satan(kitaplar)
print(f"En çok satan kitap: {en_cok_satan_kitap['isim']} ({en_cok_satan_kitap['satis']} satış)")

yazar_satislari_dict = yazar_satislari(kitaplar)
print(f"Yazar satışları: {yazar_satislari_dict}")

# 2. Liste ve Küme İşlemleri
print("\n--- 2. Liste ve Küme İşlemleri ---")
turler = set(kitap['tur'] for kitap in kitaplar)
print(f"Tüm türler: {turler}")

yuksek_satisli = [kitap['isim'] for kitap in kitaplar if kitap['satis'] > 1000]
print(f"1000'den fazla satan kitaplar: {yuksek_satisli}")

# 3. Lambda / Filter / Map Kullanımı
print("\n--- 3. Lambda / Filter / Map ---")
yeni_kitaplar = list(filter(lambda x: x['yil'] > 2020, kitaplar))
print(f"2020'den sonra çıkan kitaplar: {[k['isim'] for k in yeni_kitaplar]}")

artirılmis_satislar = list(map(lambda x: x['satis'] * 1.1, kitaplar))
print(f"Satışlar %10 artırılmış: {[round(s, 1) for s in artirılmis_satislar]}")

satis_sirali = sorted(kitaplar, key=lambda x: x['satis'], reverse=True)
print("Satış miktarına göre sıralı kitaplar:")
for kitap in satis_sirali:
    print(f"  - {kitap['isim']}: {kitap['satis']} satış")

# 4. İstatistiksel Analiz
print("\n--- 4. İstatistiksel Analiz ---")
tum_satislar = [kitap['satis'] for kitap in kitaplar]
ortalama_satis = statistics.mean(tum_satislar)
standart_sapma_satis = statistics.stdev(tum_satislar)

print(f"Ortalama satış: {ortalama_satis:.1f}")
print(f"Standart sapma: {standart_sapma_satis:.1f}")

# En çok satış yapan tür
tur_satislari = {}
for kitap in kitaplar:
    tur = kitap['tur']
    if tur in tur_satislari:
        tur_satislari[tur] += kitap['satis']
    else:
        tur_satislari[tur] = kitap['satis']

en_cok_satan_tur = max(tur_satislari, key=tur_satislari.get)
print(f"En çok satış yapan tür: {en_cok_satan_tur} ({tur_satislari[en_cok_satan_tur]} toplam satış)")

# 5. Train/Test Simülasyonu
print("\n--- 5. Train/Test Simülasyonu ---")
random.seed(42)  # Tekrarlanabilir sonuçlar için

n_train = int(len(kitaplar) * 0.7)
train_indices = random.sample(range(len(kitaplar)), n_train)
test_indices = [i for i in range(len(kitaplar)) if i not in train_indices]

train_data = [kitaplar[i] for i in train_indices]
test_data = [kitaplar[i] for i in test_indices]

print(f"Train veri sayısı: {len(train_data)}")
print(f"Test veri sayısı: {len(test_data)}")

# Train verisi analizi
train_yazar_satislari = yazar_satislari(train_data)
train_ortalama = statistics.mean([kitap['satis'] for kitap in train_data])

print(f"\nTrain verisi ortalama satış: {train_ortalama:.1f}")

# Test verisi analizi
test_ortalama_ustunde = []
for kitap in test_data:
    if kitap['satis'] > train_ortalama:
        test_ortalama_ustunde.append(kitap['isim'])

print(f"Test verisinde train ortalaması üzerinde satan kitaplar: {test_ortalama_ustunde}")

# Karşılaştırma
test_ortalama = statistics.mean([kitap['satis'] for kitap in test_data])
print(f"\nKarşılaştırma:")
print(f"Train ortalama: {train_ortalama:.1f}")
print(f"Test ortalama: {test_ortalama:.1f}")
print(f"Fark: {abs(train_ortalama - test_ortalama):.1f}")

print("\n--- Analiz Yorumu ---")
print("Train ve test verileri arasındaki ortalama satış farkı küçük,")
print("bu da verimizin homojen dağıldığını gösteriyor.")
if train_ortalama > test_ortalama:
    print("Train verisinde daha yüksek satışlı kitaplar bulunuyor.")
else:
    print("Test verisinde daha yüksek satışlı kitaplar bulunuyor.")

print("\n" + "=" * 60)
print("TÜM SORULAR TAMAMLANDI!")
print("=" * 60)