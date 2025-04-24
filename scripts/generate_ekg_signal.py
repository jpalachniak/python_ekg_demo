import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fs = 250               # częstotliwość próbkowania (Hz)
t = np.linspace(0, 10, fs * 10)  # 10 sekund sygnału
signal = 0.01 * np.random.randn(len(t))  # szum

# „sztuczne skoki” imitujące QRS
for i in range(1, 10):
    idx = i * fs
    signal[idx:idx+5] += [0.2, 0.5, 1.0, 0.5, 0.2]

#  słaby rytm bazowy (sinusoidalny)
signal += 0.1 * np.sin(2 * np.pi * 1.0 * t)

# Zapisz do CSV
try: 
    df = pd.DataFrame({'time': t, 'voltage': signal})
    df.to_csv('data/sample_ecg.csv', index=False)
    print("Plik został zapisany pomyślnie.")
except FileNotFoundError:
    print("Nie znaleziono pliku. Upewnij się, że ścieżka jest poprawna")


# Wykres podglądowy
plt.plot(t, signal)
plt.title("Syntetyczny sygnał EKG")
plt.xlabel("Czas (s)")
plt.ylabel("Napięcie (mV)")
plt.grid()
plt.show()
