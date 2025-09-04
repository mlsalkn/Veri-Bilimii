kelime = input("Bir kelime girin: ").lower()
frekans = {}

for harf in kelime:
    if harf in frekans:
        frekans[harf] += 1
    else:
        frekans[harf] = 1

print(f"Harf frekansı: {frekans}")