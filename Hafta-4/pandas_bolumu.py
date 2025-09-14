
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

def pandas_dataframe_olustur():
    """2.1 Veri setini Pandas DataFrame olarak oluşturma"""
    print("2.1 Veri setini Pandas DataFrame olarak oluşturma:")
    print("-" * 50)

    # Örnek veri seti
    data = {
        'Öğrenci': ['Ali', 'Ayşe', 'Mehmet', 'Zeynep', 'Ahmet'],
        'Yaş': [20, 21, 19, 22, 20],
        'Bölüm': ['Bilgisayar', 'Fizik', 'Kimya', 'Bilgisayar', 'Fizik'],
        'Matematik': [70, 60, 80, 90, 55],
        'Fizik': [65, 75, 70, 85, 60],
        'Kimya': [80, 85, 65, 95, 70]
    }

    df = pd.DataFrame(data)
    print("Öğrenci DataFrame:")
    print(df)
    print()
    
    # DataFrame hakkında bilgi
    print("DataFrame Bilgileri:")
    print(f"- Satır sayısı: {len(df)}")
    print(f"- Sütun sayısı: {len(df.columns)}")
    print(f"- Sütun adları: {list(df.columns)}")
    
    return df

def pandas_ders_ortalama(df):
    """2.2 Her ders için ortalama puan"""
    print("\n2.2 Her ders için ortalama puan:")
    print("-" * 35)

    ders_sutunlari = ['Matematik', 'Fizik', 'Kimya']
    ders_ortalamalari = df[ders_sutunlari].mean()

    print("Ders Ortalamaları:")
    for ders in ders_sutunlari:
        print(f"  {ders}: {ders_ortalamalari[ders]:.2f}")
    
    return ders_ortalamalari

def pandas_en_yuksek_not(df):
    """2.3 En yüksek matematik notunu alan öğrenci"""
    print("\n2.3 En yüksek matematik notunu alan öğrenci:")
    print("-" * 45)

    en_yuksek_mat = df[df['Matematik'] == df['Matematik'].max()]
    print(f"En yüksek matematik notu: {df['Matematik'].max()}")
    print(f"Öğrenci: {en_yuksek_mat['Öğrenci'].values[0]}")
    
    # Tüm notları göster
    print(f"Bu öğrencinin tüm notları:")
    ogrenci_bilgi = en_yuksek_mat.iloc[0]
    print(f"  - Matematik: {ogrenci_bilgi['Matematik']}")
    print(f"  - Fizik: {ogrenci_bilgi['Fizik']}")
    print(f"  - Kimya: {ogrenci_bilgi['Kimya']}")
    
    return en_yuksek_mat

def pandas_not_ortalamasi(df):
    """2.4 Her öğrencinin not ortalamasını hesaplama"""
    print("\n2.4 Her öğrencinin not ortalamasını hesaplama:")
    print("-" * 45)

    ders_sutunlari = ['Matematik', 'Fizik', 'Kimya']
    df['Not_Ortalamasi'] = df[ders_sutunlari].mean(axis=1)
    
    print("Öğrenci Not Ortalamaları:")
    ogrenci_notlar = df[['Öğrenci', 'Not_Ortalamasi']].copy()
    ogrenci_notlar['Not_Ortalamasi'] = ogrenci_notlar['Not_Ortalamasi'].round(2)
    print(ogrenci_notlar.to_string(index=False))
    
    return df

def pandas_bolum_gruplama(df):
    """2.5 Bölümlere göre gruplama ve ortalama başarı"""
    print("\n2.5 Bölümlere göre ortalama başarılar:")
    print("-" * 40)

    ders_sutunlari = ['Matematik', 'Fizik', 'Kimya']
    bolum_ortalamalari = df.groupby('Bölüm')[ders_sutunlari + ['Not_Ortalamasi']].mean()
    
    print("Bölümlere göre ortalamalar:")
    print(bolum_ortalamalari.round(2))
    
    # Her bölüm için ayrıntılı bilgi
    print("\nBölüm bazında detay:")
    for bolum in df['Bölüm'].unique():
        bolum_df = df[df['Bölüm'] == bolum]
        print(f"\n{bolum} Bölümü:")
        print(f"  - Öğrenci sayısı: {len(bolum_df)}")
        print(f"  - Ortalama yaş: {bolum_df['Yaş'].mean():.1f}")
        print(f"  - Genel not ortalaması: {bolum_df['Not_Ortalamasi'].mean():.2f}")
    
    return bolum_ortalamalari

def pandas_basarili_ogrenciler(df):
    """2.6 Ortalaması 70'in üzerinde olan öğrenciler"""
    print("\n2.6 Ortalaması 70'in üzerinde olan öğrenciler:")
    print("-" * 50)

    basarili_ogrenciler = df[df['Not_Ortalamasi'] > 70]
    
    if len(basarili_ogrenciler) > 0:
        print("Başarılı öğrenciler (ortalama > 70):")
        basarili_tablo = basarili_ogrenciler[['Öğrenci', 'Bölüm', 'Not_Ortalamasi']].copy()
        basarili_tablo['Not_Ortalamasi'] = basarili_tablo['Not_Ortalamasi'].round(2)
        print(basarili_tablo.to_string(index=False))
        
        print(f"\nToplam başarılı öğrenci sayısı: {len(basarili_ogrenciler)}")
        print(f"Başarı oranı: %{len(basarili_ogrenciler)/len(df)*100:.1f}")
    else:
        print("70'in üzerinde ortalaması olan öğrenci bulunamadı.")
    
    return basarili_ogrenciler

def pandas_ek_analizler(df):
    """Ek Pandas analizleri"""
    print("\n🔍 EK PANDAS ANALİZLERİ:")
    print("-" * 30)
    
    ders_sutunlari = ['Matematik', 'Fizik', 'Kimya']
    
    print("Genel İstatistikler:")
    print(df[ders_sutunlari + ['Not_Ortalamasi']].describe().round(2))
    
    print(f"\nEn Başarılı Öğrenci:")
    en_basarili = df.loc[df['Not_Ortalamasi'].idxmax()]
    print(f"  - İsim: {en_basarili['Öğrenci']}")
    print(f"  - Bölüm: {en_basarili['Bölüm']}")
    print(f"  - Ortalama: {en_basarili['Not_Ortalamasi']:.2f}")
    
    print(f"\nEn Düşük Performanslı Öğrenci:")
    en_dusuk = df.loc[df['Not_Ortalamasi'].idxmin()]
    print(f"  - İsim: {en_dusuk['Öğrenci']}")
    print(f"  - Bölüm: {en_dusuk['Bölüm']}")
    print(f"  - Ortalama: {en_dusuk['Not_Ortalamasi']:.2f}")

def pandas_grafik_ciz(df):
    """Basit grafikler çizme"""
    print("\n📊 GRAFİK OLUŞTURMA:")
    print("-" * 25)
    
    try:
        plt.style.use('default')
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle('Pandas Bölümü - Veri Görselleştirmeleri', fontsize=14, fontweight='bold')
        
        ders_sutunlari = ['Matematik', 'Fizik', 'Kimya']
        
        # 1. Her dersin bar grafiği
        df[ders_sutunlari].mean().plot(kind='bar', ax=axes[0,0], color=['skyblue', 'lightgreen', 'salmon'])
        axes[0,0].set_title('Derslerin Ortalama Puanları')
        axes[0,0].set_ylabel('Puan')
        axes[0,0].tick_params(axis='x', rotation=45)
        
        # 2. Öğrenci not ortalamaları
        df.plot(x='Öğrenci', y='Not_Ortalamasi', kind='bar', ax=axes[0,1], color='orange')
        axes[0,1].set_title('Öğrenci Not Ortalamaları')
        axes[0,1].set_ylabel('Ortalama')
        axes[0,1].tick_params(axis='x', rotation=45)
        
        # 3. Bölüm bazında ortalamalar
        bolum_ort = df.groupby('Bölüm')['Not_Ortalamasi'].mean()
        bolum_ort.plot(kind='bar', ax=axes[1,0], color=['lightcoral', 'lightskyblue', 'lightgreen'])
        axes[1,0].set_title('Bölümlere Göre Ortalama Başarı')
        axes[1,0].set_ylabel('Ortalama Puan')
        axes[1,0].tick_params(axis='x', rotation=45)
        
        # 4. Yaş dağılımı
        df['Yaş'].value_counts().sort_index().plot(kind='bar', ax=axes[1,1], color='purple', alpha=0.7)
        axes[1,1].set_title('Yaş Dağılımı')
        axes[1,1].set_ylabel('Öğrenci Sayısı')
        axes[1,1].set_xlabel('Yaş')
        
        plt.tight_layout()
        
        # Grafikleri kaydetme
        plt.savefig('pandas_grafikleri.png', dpi=300, bbox_inches='tight')
        print("✅ Grafikler 'pandas_grafikleri.png' olarak kaydedildi")
        plt.show()
        
    except ImportError:
        print("⚠️ Matplotlib bulunamadı, grafikler çizilemedi")
        print("💡 Grafik için: pip install matplotlib")
    except Exception as e:
        print(f"⚠️ Grafik çizme hatası: {e}")

def main():
    print("🐼 VERİ BİLİMİ ÖDEVİ - PANDAS BÖLÜMÜ")
    print("=" * 50)
    
    try:
        # 2.1 DataFrame oluşturma
        df = pandas_dataframe_olustur()
        
        # 2.2 Ders ortalamaları
        ders_ort = pandas_ders_ortalama(df)
        
        # 2.3 En yüksek not
        en_yuksek = pandas_en_yuksek_not(df)
        
        # 2.4 Not ortalaması ekleme
        df = pandas_not_ortalamasi(df)
        
        # 2.5 Bölüm gruplama
        bolum_ort = pandas_bolum_gruplama(df)
        
        # 2.6 Başarılı öğrenciler
        basarili = pandas_basarili_ogrenciler(df)
        
        # Ek analizler
        pandas_ek_analizler(df)
        
        # Grafik çizme
        pandas_grafik_ciz(df)
        
        # CSV kaydetme
        try:
            df.to_csv('ogrenci_verileri_pandas.csv', index=False, encoding='utf-8')
            print(f"\n✅ Tüm veriler 'ogrenci_verileri_pandas.csv' olarak kaydedildi")
        except Exception as e:
            print(f"⚠️ CSV kaydetme hatası: {e}")
        
        print("\n📊 PANDAS BÖLÜMÜ ÖZET:")
        print("-" * 30)
        print(f"✓ Toplam öğrenci sayısı: {len(df)}")
        print(f"✓ En yüksek ortalama: {df['Not_Ortalamasi'].max():.2f}")
        print(f"✓ En düşük ortalama: {df['Not_Ortalamasi'].min():.2f}")
        print(f"✓ Genel sınıf ortalaması: {df['Not_Ortalamasi'].mean():.2f}")
        print(f"✓ Başarılı öğrenci sayısı (>70): {len(basarili)}")
        
        return df
        
    except ImportError:
        print("❌ Pandas kütüphanesi bulunamadı!")
        print("💡 Lütfen şu komutu çalıştırın: pip install pandas")
        return None
        
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")
        return None

if __name__ == "__main__":
    print("🚀 Pandas bölümü başlatılıyor...")
    
    df = main()
    
    if df is not None:
        print("\n✅ Pandas bölümü başarıyla tamamlandı!")
        print("📁 Oluşturulan dosyalar:")
        print("  - ogrenci_verileri_pandas.csv")
        print("  - pandas_grafikleri.png")
    else:
        print("\n❌ Pandas bölümü tamamlanamadı!")
    
    input("\n✨ Çıkmak için Enter'a basın...")