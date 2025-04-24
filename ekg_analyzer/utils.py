import csv
import os

def load_ecg_csv(filepath):
    time = []
    voltage = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            time.append(float(row['time']))
            voltage.append(float(row['voltage']))
    return time, voltage

def save_stats(peak_count, signal_duration, avg_heart_rate, filename: str = 'results/stats.txt'):

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as f:
        f.write(f"Liczba pików: {peak_count}\n")
        f.write(f"Czas trwania sygnału: {signal_duration} s\n")
        f.write(f"Srednie tetno: {avg_heart_rate} BPM\n")

    print(f"Zapisano do pliku {filename}")

