print("\n--- SORU 3: Kümeler ---")
A = {"Python", "R", "SQL", "Java"}
B = {"C++", "Python", "JavaScript", "SQL"}

# Ortak diller
ortak_diller = A & B
print(f"Ortak diller: {ortak_diller}")

# Sadece A'da olan diller
sadece_A = A - B
print(f"Sadece A'da olan diller: {sadece_A}")

# Birleşim (alfabetik sırada)
birlesim = sorted(A | B)
print(f"Birleşim (alfabetik): {birlesim}")
