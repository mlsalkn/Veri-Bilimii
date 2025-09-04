liste = [12, 4, 9, 25, 30, 7, 18]
ortalama = sum(liste) / len(liste)
buyukler = [x for x in liste if x > ortalama]

print(f"Listenin ortalaması: {ortalama}")
print(f"Ortalamadan büyük sayılar: {buyukler}")