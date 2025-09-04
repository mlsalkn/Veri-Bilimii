print("\n--- SORU 5: Fonksiyonlar ---")

def kelime_sayaci(metin):
    """Metin analizi yapan fonksiyon"""
    kelimeler = metin.lower().split()
    
    toplam_kelime = len(kelimeler)
    en_uzun_kelime = max(kelimeler, key=len)
    
    kelime_frekansi = Counter(kelimeler)
    en_sik_kelime = kelime_frekansi.most_common(1)[0][0]
    
    return { 'toplam_kelime': toplam_kelime,
        'en_uzun_kelime': en_uzun_kelime,
        'en_sik_kelime': en_sik_kelime
    }

test_metin = "Python veri bilimi için harika bir dil. Python öğrenmek kolay ve Python ile analiz yapmak eğlenceli."
sonuc = kelime_sayaci(test_metin)
print(f"Test metni: {test_metin}")
print(f"Toplam kelime sayısı: {sonuc['toplam_kelime']}")
print(f"En uzun kelime: {sonuc['en_uzun_kelime']}")
print(f"En sık geçen kelime: {sonuc['en_sik_kelime']}")