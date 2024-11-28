def mag_kv(matrix):
    summa = sum(matrix[0])
    for i in range(len(matrix)):
        kolv = 0
        for j in range(len(matrix)):
            kolv += matrix[j][i]
        if kolv != summa or sum(matrix[i]) != summa:
            return False
    return True
I = [[3, 2, 2], [2, 3, 2], [2, 2, 3]]
print(mag_kv(I))
II = [[5, 4, 5], [4, 5, 4], [4, 4, 5]]
print(mag_kv(II))
