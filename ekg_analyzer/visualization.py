import matplotlib.pyplot as plt
import os

def plot_ecg(time, original, filtered, peaks, save_path):
    plt.figure(figsize=(10, 5))
    plt.plot(time, original, label='Original', alpha=0.5)
    plt.plot(time, filtered, label='Filtered', linewidth=2)
    plt.plot([time[p] for p in peaks], [filtered[p] for p in peaks], "x", label='Peaks')
    plt.title("ECG Signal Analysis")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (mV)")
    plt.legend()
    plt.tight_layout()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    plt.close()