# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Türkçe karakter desteği ve grafik ayarları
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.style.use('seaborn-v0_8')

def veri_hazirla():
    """Görselleştirme için veri hazırlama"""
    # Öğrenci verileri
    data = {
        'Öğrenci': ['Ali', 'Ayşe', 'Mehmet', 'Zeynep', 'Ahmet', 'Fatma', 'Can', 'Elif'],
        'Yaş': [20, 21, 19, 22, 20, 23, 19, 21],
        'Bölüm': ['Bilgisayar', 'Fizik', 'Kimya', 'Bilgisayar', 'Fizik', 'Kimya', 'Bilgisayar', 'Fizik'],
        'Matematik': [70, 60, 80, 90, 55, 75, 85, 65],
        'Fizik': [65, 75, 70, 85, 60, 80, 90, 70],
        'Kimya': [80, 85, 65, 95, 70, 85, 75, 80]
    }
    
    df = pd.DataFrame(data)
    df['Not_Ortalamasi'] = df[['Matematik', 'Fizik', 'Kimya']].mean(axis=1)
    
    # Simülasyon verileri
    np.random.seed(42)
    sinav_puanlari = np.random.normal(loc=70, scale=15, size=1000)
    sinav_puanlari = np.clip(sinav_puanlari, 0, 100)
    
    return df, sinav_puanlari

def histogram_ciz(df, sinav_puanlari):
    """Histogram grafikleri çizme"""
    print("📊 Histogram Grafikleri Çiziliyor...")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Histogram Grafikleri', fontsize=16, fontweight='bold')
    
    # 1. Matematik dağılımı
    axes[0, 0].hist(df['Matematik'], bins=8, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0, 0].set_title('Matematik Notları Dağılımı')
    axes[0, 0].set_xlabel('Puan')
    axes[0, 0].set_ylabel('Frekans')
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Fizik dağılımı
    axes[0, 1].hist(df['Fizik'], bins=8, alpha=0.7, color='lightgreen', edgecolor='black')
    axes[0, 1].set_title('Fizik Notları Dağılımı')
    axes[0, 1].set_xlabel('Puan')
    axes[0, 1].set_ylabel('Frekans')
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Kimya dağılımı
    axes[1, 0].hist(df['Kimya'], bins=8, alpha=0.7, color='salmon', edgecolor='black')
    axes[1, 0].set_title('Kimya Notları Dağılımı')
    axes[1, 0].set_xlabel('Puan')
    axes[1, 0].set_ylabel('Frekans')
    axes[1, 0].grid(True, alpha=0.3)
    
    # 4. Simülasyon verileri dağılımı
    axes[1, 1].hist(sinav_puanlari, bins=30, alpha=0.7, color='purple', edgecolor='black')
    axes[1, 1].set_title('1000 Öğrenci Sınav Puanları Dağılımı')
    axes[1, 1].set_xlabel('Puan')
    axes[1, 1].set_ylabel('Frekans')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('histogram_grafikleri.png', dpi=300, bbox_inches='tight')
    print("✅ Histogram grafikleri 'histogram_grafikleri.png' olarak kaydedildi")
    plt.show()

def bar_grafik_ciz(df):
    """Bar grafikleri çizme"""
    print("📊 Bar Grafikleri Çiziliyor...")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Bar Grafikleri', fontsize=16, fontweight='bold')
    
    # 1. Ders ortalamaları
    ders_ort = df[['Matematik', 'Fizik', 'Kimya']].mean()
    bars1 = axes[0, 0].bar(ders_ort.index, ders_ort.values, 
                          color=['skyblue', 'lightgreen', 'salmon'], alpha=0.8)
    axes[0, 0].set_title('Derslerin Ortalama Puanları')
    axes[0, 0].set_ylabel('Ortalama Puan')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Bar değerlerini gösterme
    for bar in bars1:
        height = bar.get_height()
        axes[0, 0].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                       f'{height:.1f}', ha='center', va='bottom')
    
    # 2. Bölüm bazında ortalamalar
    bolum_ort = df.groupby('Bölüm')['Not_Ortalamasi'].mean()
    bars2 = axes[0, 1].bar(bolum_ort.index, bolum_ort.values,
                          color=['lightcoral', 'lightskyblue', 'lightgreen'], alpha=0.8)
    axes[0, 1].set_title('Bölümlere Göre Ortalama Başarı')
    axes[0, 1].set_ylabel('Ortalama Puan')
    axes[0, 1].tick_params(axis='x', rotation=45)
    axes[0, 1].grid(True, alpha=0.3)
    
    # Bar değerlerini gösterme
    for bar in bars2:
        height = bar.get_height()
        axes[0, 1].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                       f'{height:.1f}', ha='center', va='bottom')
    
    # 3. Öğrenci not ortalamaları
    bars3 = axes[1, 0].bar(df['Öğrenci'], df['Not_Ortalamasi'], 
                          color='orange', alpha=0.8)
    axes[1, 0].set_title('Öğrenci Not Ortalamaları')
    axes[1, 0].set_ylabel('Ortalama')
    axes[1, 0].tick_params(axis='x', rotation=45)
    axes[1, 0].grid(True, alpha=0.3)
    
    # 4. Yaş dağılımı
    yas_dagilim = df['Yaş'].value_counts().sort_index()
    bars4 = axes[1, 1].bar(yas_dagilim.index, yas_dagilim.values, 
                          color='purple', alpha=0.7)
    axes[1, 1].set_title('Yaş Dağılımı')
    axes[1, 1].set_xlabel('Yaş')
    axes[1, 1].set_ylabel('Öğrenci Sayısı')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('bar_grafikleri.png', dpi=300, bbox_inches='tight')
    print("✅ Bar grafikleri 'bar_grafikleri.png' olarak kaydedildi")
    plt.show()

def korelasyon_analizi(df):
    """Korelasyon matrisi ve heatmap"""
    print("📊 Korelasyon Analizi...")
    
    # Sayısal veriler için korelasyon
    sayisal_veriler = df[['Yaş', 'Matematik', 'Fizik', 'Kimya', 'Not_Ortalamasi']]
    korelasyon = sayisal_veriler.corr()
    
    print("Korelasyon Matrisi:")
    print(korelasyon.round(3))
    
    # Heatmap çizme
    plt.figure(figsize=(10, 8))
    sns.heatmap(korelasyon, annot=True, cmap='coolwarm', center=0, 
                square=True, fmt='.2f', cbar_kws={'shrink': 0.8})
    plt.title('Dersler Arası Korelasyon Matrisi', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('korelasyon_matrisi.png', dpi=300, bbox_inches='tight')
    print("✅ Korelasyon matrisi 'korelasyon_matrisi.png' olarak kaydedildi")
    plt.show()
    
    # En yüksek korelasyonlar
    print("\n🔍 Önemli Korelasyonlar:")
    korelasyon_flat = korelasyon.unstack()
    korelasyon_flat = korelasyon_flat[korelasyon_flat != 1.0]  # Kendisiyle korelasyonu çıkar
    korelasyon_sirali = korelasyon_flat.abs().sort_values(ascending=False)
    
    print("En Yüksek 3 Korelasyon:")
    for i in range(3):
        if i < len(korelasyon_sirali):
            pair = korelasyon_sirali.index[i]
            value = korelasyon_flat[pair]
            print(f"  {pair[0]} - {pair[1]}: {value:.3f}")

def gelismis_grafikler(df, sinav_puanlari):
    """Daha gelişmiş grafikler"""
    print("📊 Gelişmiş Grafikler Çiziliyor...")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Gelişmiş Veri Görselleştirmeleri', fontsize=16, fontweight='bold')
    
    # 1. Box plot - Bölümlere göre not dağılımı
    bolum_notlar = []
    bolum_adlari = []
    for bolum in df['Bölüm'].unique():
        bolum_df = df[df['Bölüm'] == bolum]
        bolum_notlar.append(bolum_df['Not_Ortalamasi'])
        bolum_adlari.append(bolum)
    
    axes[0, 0].boxplot(bolum_notlar, labels=bolum_adlari)
    axes[0, 0].set_title('Bölümlere Göre Not Dağılımı (Box Plot)')
    axes[0, 0].set_ylabel('Not Ortalaması')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Scatter plot - Yaş vs Not ortalaması
    renkler = {'Bilgisayar': 'red', 'Fizik': 'blue', 'Kimya': 'green'}
    for bolum in df['Bölüm'].unique():
        bolum_df = df[df['Bölüm'] == bolum]
        axes[0, 1].scatter(bolum_df['Yaş'], bolum_df['Not_Ortalamasi'], 
                          label=bolum, color=renkler[bolum], alpha=0.7, s=100)
    
    axes[0, 1].set_title('Yaş vs Not Ortalaması')
    axes[0, 1].set_xlabel('Yaş')
    axes[0, 1].set_ylabel('Not Ortalaması')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Pie chart - Başarı dağılımı
    basari_90_plus = len(df[df['Not_Ortalamasi'] >= 90])
    basari_80_89 = len(df[(df['Not_Ortalamasi'] >= 80) & (df['Not_Ortalamasi'] < 90)])
    basari_70_79 = len(df[(df['Not_Ortalamasi'] >= 70) & (df['Not_Ortalamasi'] < 80)])
    basari_70_minus = len(df[df['Not_Ortalamasi'] < 70])
    
    labels = ['90+ (Mükemmel)', '80-89 (Çok İyi)', '70-79 (İyi)', '70- (Gelişmeli)']
    sizes = [basari_90_plus, basari_80_89, basari_70_79, basari_70_minus]
    colors = ['gold', 'lightgreen', 'lightskyblue', 'lightcoral']
    
    # Sadece sıfır olmayan değerleri göster
    filtered_data = [(label, size, color) for label, size, color in zip(labels, sizes, colors) if size > 0]
    if filtered_data:
        labels_filtered, sizes_filtered, colors_filtered = zip(*filtered_data)
        axes[1, 0].pie(sizes_filtered, labels=labels_filtered, colors=colors_filtered, 
                      autopct='%1.1f%%', startangle=90)
    axes[1, 0].set_title('Başarı Seviyesi Dağılımı')
    
    # 4. Çoklu bar chart - Her öğrencinin ders notları
    x_pos = np.arange(len(df))
    width = 0.25
    
    bars1 = axes[1, 1].bar(x_pos - width, df['Matematik'], width, 
                          label='Matematik', color='skyblue', alpha=0.8)
    bars2 = axes[1, 1].bar(x_pos, df['Fizik'], width, 
                          label='Fizik', color='lightgreen', alpha=0.8)
    bars3 = axes[1, 1].bar(x_pos + width, df['Kimya'], width, 
                          label='Kimya', color='salmon', alpha=0.8)
    
    axes[1, 1].set_title('Öğrencilerin Ders Notları Karşılaştırması')
    axes[1, 1].set_xlabel('Öğrenci')
    axes[1, 1].set_ylabel('Not')
    axes[1, 1].set_xticks(x_pos)
    axes[1, 1].set_xticklabels(df['Öğrenci'], rotation=45)
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('gelismis_grafikler.png', dpi=300, bbox_inches='tight')
    print("✅ Gelişmiş grafikler 'gelismis_grafikler.png' olarak kaydedildi")
    plt.show()

def istatistik_grafikleri(sinav_puanlari):
    """İstatistiksel grafikler"""
    print("📊 İstatistiksel Grafikler...")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('İstatistiksel Analizler', fontsize=16, fontweight='bold')
    
    # 1. Normal dağılım ile karşılaştırma
    axes[0, 0].hist(sinav_puanlari, bins=30, density=True, alpha=0.7, 
                   color='skyblue', label='Gerçek Veri')
    
    # Normal dağılım eğrisi
    mu = np.mean(sinav_puanlari)
    sigma = np.std(sinav_puanlari)
    x = np.linspace(0, 100, 100)
    y = ((1/(sigma * np.sqrt(2 * np.pi))) * 
         np.exp(-0.5 * ((x - mu) / sigma) ** 2))
    axes[0, 0].plot(x, y, 'r-', linewidth=2, label='Normal Dağılım')
    axes[0, 0].set_title('Sınav Puanları - Normal Dağılım Karşılaştırması')
    axes[0, 0].set_xlabel('Puan')
    axes[0, 0].set_ylabel('Yoğunluk')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Kümülatif dağılım
    sorted_data = np.sort(sinav_puanlari)
    cumulative = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
    axes[0, 1].plot(sorted_data, cumulative, linewidth=2, color='green')
    axes[0, 1].set_title('Kümülatif Dağılım Fonksiyonu')
    axes[0, 1].set_xlabel('Puan')
    axes[0, 1].set_ylabel('Kümülatif Olasılık')
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Q-Q Plot benzeri
    from scipy import stats
    try:
        stats.probplot(sinav_puanlari, dist="norm", plot=axes[1, 0])
        axes[1, 0].set_title('Q-Q Plot (Normal Dağılıma Uygunluk)')
        axes[1, 0].grid(True, alpha=0.3)
    except:
        # Scipy yoksa basit alternatif
        theoretical_quantiles = np.linspace(-3, 3, len(sinav_puanlari))
        sample_quantiles = np.sort(sinav_puanlari)
        axes[1, 0].scatter(theoretical_quantiles, sample_quantiles, alpha=0.6)
        axes[1, 0].set_title('Quantile-Quantile Analizi')
        axes[1, 0].set_xlabel('Teorik Quantiller')
        axes[1, 0].set_ylabel('Örnek Quantiller')
        axes[1, 0].grid(True, alpha=0.3)
    
    # 4. Başarı aralıkları
    aralıklar = ['0-50', '50-60', '60-70', '70-80', '80-90', '90-100']
    sayılar = [
        np.sum((sinav_puanlari >= 0) & (sinav_puanlari < 50)),
        np.sum((sinav_puanlari >= 50) & (sinav_puanlari < 60)),
        np.sum((sinav_puanlari >= 60) & (sinav_puanlari < 70)),
        np.sum((sinav_puanlari >= 70) & (sinav_puanlari < 80)),
        np.sum((sinav_puanlari >= 80) & (sinav_puanlari < 90)),
        np.sum((sinav_puanlari >= 90) & (sinav_puanlari <= 100))
    ]
    
    colors = ['red', 'orange', 'yellow', 'lightgreen', 'green', 'darkgreen']
    bars = axes[1, 1].bar(aralıklar, sayılar, color=colors, alpha=0.7)
    axes[1, 1].set_title('Başarı Aralıklarına Göre Öğrenci Dağılımı')
    axes[1, 1].set_xlabel('Puan Aralığı')
    axes[1, 1].set_ylabel('Öğrenci Sayısı')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    # Bar değerlerini gösterme
    for bar in bars:
        height = bar.get_height()
        axes[1, 1].text(bar.get_x() + bar.get_width()/2., height + 5,
                       f'{int(height)}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('istatistik_grafikleri.png', dpi=300, bbox_inches='tight')
    print("✅ İstatistiksel grafikler 'istatistik_grafikleri.png' olarak kaydedildi")
    plt.show()

def main():
    print("📊 VERİ BİLİMİ ÖDEVİ - GÖRSELLEŞTİRME BÖLÜMÜ")
    print("=" * 55)
    
    try:
        # Veri hazırlama
        print("🔧 Veriler hazırlanıyor...")
        df, sinav_puanlari = veri_hazirla()
        print(f"✅ {len(df)} öğrenci verisi ve {len(sinav_puanlari)} simülasyon verisi hazırlandı")
        
        # Histogram grafikleri
        histogram_ciz(df, sinav_puanlari)
        
        # Bar grafikleri
        bar_grafik_ciz(df)
        
        # Korelasyon analizi
        korelasyon_analizi(df)
        
        # Gelişmiş grafikler
        gelismis_grafikler(df, sinav_puanlari)
        
        # İstatistiksel grafikler
        istatistik_grafikleri(sinav_puanlari)
        
        print("\n📊 GÖRSELLEŞTİRME BÖLÜMÜ ÖZET:")
        print("-" * 40)
        print("✅ 4 farklı histogram grafiği")
        print("✅ 4 farklı bar grafiği") 
        print("✅ Korelasyon matrisi heatmap")
        print("✅ 4 gelişmiş grafik türü")
        print("✅ 4 istatistiksel analiz grafiği")
        print(f"✅ Toplam {len(df)} öğrenci analiz edildi")
        print(f"✅ {len(sinav_puanlari)} simülasyon verisi görselleştirildi")
        
        print("\n📁 Oluşturulan dosyalar:")
        dosyalar = [
            'histogram_grafikleri.png',
            'bar_grafikleri.png',
            'korelasyon_matrisi.png',
            'gelismis_grafikler.png',
            'istatistik_grafikleri.png'
        ]
        for dosya in dosyalar:
            print(f"  - {dosya}")
            
        return True
        
    except ImportError as e:
        print(f"❌ Eksik kütüphane hatası: {e}")
        print("💡 Gerekli kütüphaneler:")
        print("  pip install matplotlib seaborn pandas numpy scipy")
        return False
        
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Görselleştirme bölümü başlatılıyor...")
    
    basarili = main()
    
    if basarili:
        print("\n✅ Görselleştirme bölümü başarıyla tamamlandı!")
        print("🎨 Tüm grafikler yüksek kalitede PNG formatında kaydedildi")
    else:
        print("\n❌ Görselleştirme bölümü tamamlanamadı!")
    
    input("\n✨ Çıkmak için Enter'a basın...")