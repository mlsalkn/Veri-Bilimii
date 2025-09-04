print("\n--- SORU 8: String Metodları ---")

def rakam_toplami(metin):
    """String içindeki rakamların toplamını bulur"""
    return sum(int(char) for char in metin if char.isdigit())

test_string = "abc12def3"
toplam = rakam_toplami(test_string)
print(f"'{test_string}' içindeki rakamların toplamı: {toplam}")
