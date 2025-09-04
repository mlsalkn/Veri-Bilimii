def film_yorumu_analizi():
    # Kullanıcıdan yorumları al
    yorumlar = []
    print("Film yorumlarını girin (5-6 yorum):")
    
    for i in range(5):
        yorum = input(f"{i+1}. yorum: ")
        yorumlar.append(yorum)
    
    # Ekstra yorum iste (isteğe bağlı)
    ek_yorum = input("6. yorum (isteğe bağlı, boş bırakabilirsiniz): ")
    if ek_yorum.strip():
        yorumlar.append(ek_yorum)
    
    # Analizleri yap
    toplam_yorum = len(yorumlar)
    
    # "iyi" kelimesi geçen yorumları say
    iyi_gecen_sayi = 0
    for yorum in yorumlar:
        if "iyi" in yorum.lower():
            iyi_gecen_sayi += 1
    
    # Yorum uzunluklarını hesapla
    yorum_uzunluklari = [len(yorum) for yorum in yorumlar]
    
    # En uzun ve en kısa yorumları bul
    en_uzun_yorum = max(yorumlar, key=len)
    en_kisa_yorum = min(yorumlar, key=len)
    
    # Ortalama uzunluğu hesapla
    ortalama_uzunluk = sum(yorum_uzunluklari) / toplam_yorum
    
    # Sonuçları yazdır
    print("\n" + "="*50)
    print("FİLM YORUMU ANALİZ SONUÇLARI")
    print("="*50)
    print(f"Toplam yorum sayısı: {toplam_yorum}")
    print(f"\"iyi\" geçen yorum sayısı: {iyi_gecen_sayi}")
    print(f"En uzun yorum: {en_uzun_yorum}")
    print(f"En kısa yorum: {en_kisa_yorum}")
    print(f"Ortalama uzunluk: {ortalama_uzunluk:.1f} karakter")
    print("="*50)
    
    # Ek olarak tüm yorumları ve uzunluklarını göster
    print("\nTüm Yorumlar ve Uzunlukları:")
    for i, (yorum, uzunluk) in enumerate(zip(yorumlar, yorum_uzunluklari), 1):
        print(f"{i}. {yorum} ({uzunluk} karakter)")

# Programı çalıştır
if __name__ == "__main__":
    film_yorumu_analizi()