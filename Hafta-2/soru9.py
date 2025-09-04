cumle = input("Bir cümle girin: ")
kelimeler = cumle.split()
buyuk_harfli = ' '.join([kelime.capitalize() for kelime in kelimeler])
print(f"Düzenlenmiş cümle: {buyuk_harfli}")