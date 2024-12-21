# Podstawowe operacje na danych w tablicach 
import numpy as np
tab_1 = np.array([1, 2, 3, 4, 5, 6])
tab_2 = np.array([5, 6, 7, 8, 9, 10])
tab_3 = np.arange(1, 21)
tab_4 = np.array([[i] for i in range(2, 13, 2)])

print('Dodawanie:', tab_1 + tab_2)
print('Pomnóż każdy element tablicy', tab_1 * 3)
print('Oblicz iloczyn elementów tab_4 z liczbą 05',tab_4 * 0.5 )
print('Podziel elementy tab_2 przez odpowiadające im elementy tab_1', tab_2 / tab_1)
print('Do każdego elementu tab_3 dodaj wektor [10, 20, 30, 40, 50]', tab_3.reshape(4,5) + np.array([10, 20, 30, 40, 50]))
print('Wykonaj dzielenie modulo tab_2 przez tab_1', np.mod(tab_2, tab_1))
print('Pomnóż macierz tab_4 przez wektor [1, 2, 3]', tab_4 * np.array([1, 2, 3]))
print('Podnieś elementy tab_1 do kwadratu i podziel przez 2', (tab_1 ** 2) / 2)
print('Wykonaj operację dzielenia całkowitego tab_3 przez 3', tab_3 // 3) 
print('Pomnóż tab_4 przez transponowaną wersję samej siebie', tab_4 @ tab_4.T)
print('Sprawdź także co otrzymasz w wyniku mnożenia tych macierzy w odwrotnej kolejności.', tab_4.T @ tab_4)