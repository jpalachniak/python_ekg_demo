import argparse
from ekg_analyzer.utils import load_ecg_csv
from ekg_analyzer.processing import butter_lowpass_filter, detect_peaks, calculate_hr
from ekg_analyzer.visualization import plot_ecg

def main():
    parser = argparse.ArgumentParser(description="EKG Signal Analyzer")
    parser.add_argument('--input', required=True, help="Path to input CSV file")
    parser.add_argument('--output', default="results/ecg_plot.png", help="Path to output image")
    parser.add_argument('--fs', type=int, default=250, help="Sampling frequency")
    parser.add_argument('--cutoff', type=float, default=40.0, help="Lowpass filter cutoff frequency")
    parser.add_argument('--distance', type=int, default=50, help="Minimum distance between peaks")
    
    args = parser.parse_args()

    time, voltage = load_ecg_csv(args.input)
    filtered = butter_lowpass_filter(voltage, cutoff=args.cutoff, fs=args.fs)
    peaks = detect_peaks(filtered, distance=args.distance)
    plot_ecg(time, voltage, filtered, peaks, args.output)

    print(f"Analysis complete. Found {len(peaks)} peaks. Output saved to {args.output}")
    duration = len(time)/args.fs
    hr= calculate_hr(len(peaks),duration) 
    print(f'Srednie tetno: {hr:.2f}')

if __name__ == "__main__":
    main()