sifre = input("Şifre girin: ")

if len(sifre) < 8:
    print("Şifre en az 8 karakter olmalı!")
elif not any(char.isupper() for char in sifre):
    print("Şifre en az 1 büyük harf içermeli!")
elif not any(char.isdigit() for char in sifre):
    print("Şifre en az 1 rakam içermeli!")
else:
    print("Şifre geçerli!")