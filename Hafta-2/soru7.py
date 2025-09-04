kelime = input("Bir kelime girin: ").lower()
if kelime == kelime[::-1]:
    print("Palindrom")
else:
    print("Palindrom değil")