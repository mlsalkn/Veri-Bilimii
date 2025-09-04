#9

# Kullanıcıdan 3 ürünün fiyatını alınız.
urun1_fiyat=float(input("1.ürünün fiyatını giriniz:"))
urun2_fiyat=float(input("2.ürünün fiyatını giriniz:"))
urun3_fiyat=float(input("3.ürünün fiyatını giriniz"))
#toplam fiyat hesaplama 
toplam_fiyat=urun1_fiyat+urun2_fiyat+urun3_fiyat
print("toplam fiyat:",toplam_fiyat)
# Kullanıcıdan indirim oranını alınız ve toplam fiyat üzerinden indirimli fiyatı hesaplayınız.
indirim_orani=float(input("indirim oranını giriniz:"))
indirimli_fiyat=toplam_fiyat-(toplam_fiyat*indirim_orani/100)
print("indirimli fiyat:",indirimli_fiyat)
# Kullanıcıdan ödeme yöntemini seçmesini isteyiniz (nakit, kredi kartı).
odeme_yontemi=input("ödeme yöntemini seçiniz (nakit mi ? kredi kartı mı?):")
if odeme_yontemi.lower()=="nakit":
    print("nakit ödeme seçildi.")
elif odeme_yontemi.lower()=="kredi kartı":
    print("kredi kartı ödeme seçildi.")
else:
    print("geçersiz ödeme yöntemi.")
# Kullanıcıya indirimli fiyatı ve ödeme yöntemini ekrana yazdırınız.
print("indimli fiyat:",indirimli_fiyat)    
print("ödeme yöntemi:",odeme_yontemi)
