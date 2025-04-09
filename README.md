Prosty analizator sygnału EKG z interfejsem wiersza poleceń (CLI).

```bash
PYTHON_EKG_DEMO/
├── .venv/                         # Środowisko wirtualne (lokalne)
├── data/
│   └── sample_ecg.csv            # Przykładowy plik z sygnałem EKG (czas i napięcie)
│
├── ekg_analyzer/                 # Główna logika aplikacji
│   ├── __init__.py               # Plik inicjalizujący moduł
│   ├── cli.py                    # Interfejs CLI – uruchamianie analizy z parametrami
│   ├── processing.py             # Filtrowanie i detekcja peaków w sygnale EKG
│   ├── utils.py                  # Wczytywanie danych z pliku CSV
│   └── visualization.py          # Tworzenie i zapisywanie wykresu
│
├── results/
│   ├── ecg_plot.png              # Wygenerowany wykres sygnału EKG
│   └── stats.txt                 # (obecnie pusty lub niedziałający – do zadań)
│
├── scripts/                      # Skrypty pomocnicze (uruchamianie, generowanie danych)
│   ├── generate_ekg_signal.py    # Skrypt do wygenerowania syntetycznego EKG (np. sinus z peakami)
│   └── run_analysis.py           # Główny skrypt uruchamiający analizę EKG
│
├── .gitignore                    # Ignorowane pliki w repozytorium (np. .venv, __pycache__)
└── README.md                     # Dokumentacja projektu

```

## Dane wejściowe
CSV z dwiema kolumnami: `time`, `voltage`. Jednostką "Time" jest sekunda.

## Użycie skryptu do generowania przykładowego sygnału
```bash
python scripts/generate_ekg_signal.py       
```
Kod ten stworzy przykładowy sygnał w folderze "data". 

## Użycie skryptu do analizy
```bash
python scripts.run_analysis --input data/sample_ecg.csv
```

Dostępne opcje:
--fs : częstotliwość próbkowania (domyślnie 250 Hz)  
--cutoff : częstotliwość odcięcia filtru dolnoprzepustowego  
--distance : minimalna odległość między peakami
