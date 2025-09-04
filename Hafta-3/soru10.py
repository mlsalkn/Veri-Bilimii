print("\n--- SORU 10: Numpy 2 ---")
matris = np.random.rand(5, 5)
print("5x5 Rastgele matris:")
print(matris)

sutun_ortalamalari = np.mean(matris, axis=0)
print(f"\nSütun ortalamaları: {sutun_ortalamalari}")

binary_matris = (matris > 0.5).astype(int)
print("\nBinary matris (>0.5 = 1, <=0.5 = 0):")
print(binary_matris)
