
# -*- coding: utf-8 -*-

import numpy as np

def numpy_matris_islemleri():
    """1.1 Numpy ile Matris İşlemleri"""
    print("1.1 Numpy ile Matris İşlemleri:")
    print("-" * 30)

    # 5x5 boyutunda rastgele tam sayı matrisi oluşturma
    np.random.seed(42)  # Sonuçların tekrarlanabilir olması için
    matris = np.random.randint(0, 101, size=(5, 5))

    print("5x5 Rastgele Matris:")
    print(matris)
    print()

    # Matris istatistikleri
    ortalama = np.mean(matris)
    std_sapma = np.std(matris)
    varyans = np.var(matris)
    en_buyuk = np.max(matris)
    en_kucuk = np.min(matris)

    print(f"Ortalama: {ortalama:.2f}")
    print(f"Standart Sapma: {std_sapma:.2f}")
    print(f"Varyans: {varyans:.2f}")
    print(f"En Büyük Değer: {en_buyuk}")
    print(f"En Küçük Değer: {en_kucuk}")

    # Köşegen elemanların toplamı
    kosegen_toplam = np.trace(matris)
    print(f"Köşegen Elemanların Toplamı: {kosegen_toplam}")
    
    
    return {
        'matris': matris,
        'ortalama': ortalama,
        'std_sapma': std_sapma,
        'varyans': varyans,
        'en_buyuk': en_buyuk,
        'en_kucuk': en_kucuk,
        'kosegen_toplam': kosegen_toplam
    }

def numpy_veri_simulasyonu():
    """1.2 Numpy ile Veri Simülasyonu"""
    print("\n1.2 Numpy ile Veri Simülasyonu:")
    print("-" * 30)

    # 1000 öğrencinin sınav puanları (normal dağılım)
    np.random.seed(123)
    sinav_puanlari = np.random.normal(loc=70, scale=15, size=1000)
    # 0-100 arasına sınırlama
    sinav_puanlari = np.clip(sinav_puanlari, 0, 100)

    sim_ortalama = np.mean(sinav_puanlari)
    sim_medyan = np.median(sinav_puanlari)
    sim_std = np.std(sinav_puanlari)

    print(f"1000 Öğrencinin Sınav Puanları İstatistikleri:")
    print(f"Ortalama: {sim_ortalama:.2f}")
    print(f"Medyan: {sim_medyan:.2f}")
    print(f"Standart Sapma: {sim_std:.2f}")

    # 50'den düşük alan öğrenci sayısı
    dusuk_puan = np.sum(sinav_puanlari < 50)
    print(f"50'den düşük alan öğrenci sayısı: {dusuk_puan}")
    
    # Histogram için veri hazırlama
    histogram_data = np.histogram(sinav_puanlari, bins=10)
    print(f"\nPuan Dağılımı (10 aralık):")
    for i in range(len(histogram_data[0])):
        alt_sinir = histogram_data[1][i]
        ust_sinir = histogram_data[1][i+1]
        sayi = histogram_data[0][i]
        print(f"{alt_sinir:.1f}-{ust_sinir:.1f}: {sayi} öğrenci")
    
    return {
        'sinav_puanlari': sinav_puanlari,
        'ortalama': sim_ortalama,
        'medyan': sim_medyan,
        'std_sapma': sim_std,
        'dusuk_puan_sayisi': dusuk_puan,
        'histogram': histogram_data
    }

def numpy_ek_analizler(matris, sinav_puanlari):
    """Ek numpy analizleri"""
    print("\n🔍 EK NUMPY ANALİZLERİ:")
    print("-" * 30)
    
    # Matris üzerinde ek işlemler
    print("Matris Ek İşlemleri:")
    print(f"- Matris determinantı: {np.linalg.det(matris):.2f}")
    print(f"- Satır ortalamaları: {np.mean(matris, axis=1)}")
    print(f"- Sütun ortalamaları: {np.mean(matris, axis=0)}")
    
    # Sınav puanları üzerinde ek işlemler
    print(f"\nSınav Puanları Ek İstatistikler:")
    print(f"- 25. yüzdelik: {np.percentile(sinav_puanlari, 25):.2f}")
    print(f"- 75. yüzdelik: {np.percentile(sinav_puanlari, 75):.2f}")
    print(f"- 90+ puan alan: {np.sum(sinav_puanlari >= 90)} öğrenci")
    print(f"- 80-89 arası: {np.sum((sinav_puanlari >= 80) & (sinav_puanlari < 90))} öğrenci")
    print(f"- 70-79 arası: {np.sum((sinav_puanlari >= 70) & (sinav_puanlari < 80))} öğrenci")
    print(f"- 60-69 arası: {np.sum((sinav_puanlari >= 60) & (sinav_puanlari < 70))} öğrenci")

def main():
    print("🔢 VERİ BİLİMİ ÖDEVİ - NUMPY BÖLÜMÜ")
    print("=" * 50)
    
    try:
        # 1.1 Matris işlemleri
        matris_sonuclari = numpy_matris_islemleri()
        
        # 1.2 Veri simülasyonu
        simulasyon_sonuclari = numpy_veri_simulasyonu()
        
        # Ek analizler
        numpy_ek_analizler(
            matris_sonuclari['matris'], 
            simulasyon_sonuclari['sinav_puanlari']
        )
        
        # Sonuçları dosyaya kaydetme
        try:
            # Matris verilerini kaydetme
            np.savetxt('rastgele_matris.csv', matris_sonuclari['matris'], 
                      delimiter=',', fmt='%d')
            print(f"\n✅ Rastgele matris 'rastgele_matris.csv' olarak kaydedildi")
            
            # Sınav puanlarını kaydetme
            np.savetxt('sinav_puanlari.csv', simulasyon_sonuclari['sinav_puanlari'], 
                      delimiter=',', fmt='%.2f')
            print(f"✅ Sınav puanları 'sinav_puanlari.csv' olarak kaydedildi")
            
        except Exception as e:
            print(f"⚠️ Dosya kaydetme hatası: {e}")
        
        print("\n📊 NUMPY BÖLÜMÜ ÖZET:")
        print("-" * 30)
        print(f"✓ 5x5 matris ortalaması: {matris_sonuclari['ortalama']:.2f}")
        print(f"✓ Matris köşegen toplamı: {matris_sonuclari['kosegen_toplam']}")
        print(f"✓ 1000 öğrenci sınav ortalaması: {simulasyon_sonuclari['ortalama']:.2f}")
        print(f"✓ 50'den düşük alan: {simulasyon_sonuclari['dusuk_puan_sayisi']} öğrenci")
        
        return {
            'matris': matris_sonuclari,
            'simulasyon': simulasyon_sonuclari
        }
        
    except ImportError:
        print("❌ Numpy kütüphanesi bulunamadı!")
        print("💡 Lütfen şu komutu çalıştırın: pip install numpy")
        return None
        
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")
        return None

if __name__ == "__main__":
    print("🚀 Numpy bölümü başlatılıyor...")
    
    sonuclar = main()
    
    if sonuclar:
        print("\n✅ Numpy bölümü başarıyla tamamlandı!")
        print("📁 Oluşturulan dosyalar:")
        print("  - rastgele_matris.csv")
        print("  - sinav_puanlari.csv")
    else:
        print("\n❌ Numpy bölümü tamamlanamadı!")
    
    input("\n✨ Çıkmak için Enter'a basın...")