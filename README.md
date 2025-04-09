Prosty analizator sygnału EKG z interfejsem wiersza poleceń (CLI).

## Dane wejściowe
CSV z dwiema kolumnami: `time`, `voltage`

## Użycie
```bash
python scripts/run_analysis.py --input data/sample_ecg.csv --output results/ecg_plot.png
```

Dostępne opcje:
--fs : częstotliwość próbkowania (domyślnie 250 Hz)  
--cutoff : częstotliwość odcięcia filtru dolnoprzepustowego  
--distance : minimalna odległość między peakami