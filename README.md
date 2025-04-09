Prosty analizator sygnału EKG z interfejsem wiersza poleceń (CLI).

## Dane wejściowe
CSV z dwiema kolumnami: `time`, `voltage`. Jednostką "Time" jest sekunda.

## Użycie
```bash
python scripts.run_analysis --input data/sample_ecg.csv
```

Dostępne opcje:
--fs : częstotliwość próbkowania (domyślnie 250 Hz)  
--cutoff : częstotliwość odcięcia filtru dolnoprzepustowego  
--distance : minimalna odległość między peakami
