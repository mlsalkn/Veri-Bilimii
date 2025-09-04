
# yaş hesaplama uygulaması
# Kullanıcıdan doğum tarihini alınız.
dogum_yili=input("dogum yılınızı giriniz:")
# Kullanıcının yaşını hesaplayınız (2025 yılına göre).
yas=2025-int(dogum_yili)
# Kullanıcının yaşını ekrana yazdırınız.
print("yasınız:",yas)
# Kullanıcıya yaşını ekrana yazdırınız.
if (yas == (0 <= 12 )):
    print("çocuksunuz")
elif( yas== (13<=17)):
    print("gençsiniz")
elif( 18<=yas):
    print("yetişkinsiniz.")
else:
    print("geçersiz yaş bilgisi.")

