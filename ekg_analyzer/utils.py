import csv

def load_ecg_csv(filepath):
    time = []
    voltage = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            time.append(float(row['time']))
            voltage.append(float(row['voltage']))
    return time, voltage