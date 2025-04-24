import numpy as np
from scipy.signal import find_peaks, butter, filtfilt

def butter_lowpass_filter(signal, cutoff=40, fs=250, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low')
    filtered = filtfilt(b, a, signal)
    return filtered

def detect_peaks(signal, distance=50):
    peaks, _ = find_peaks(signal, distance=distance)
    return peaks

def calculate_hr(num_peaks, duration_signal):
    bpm = ((num_peaks-1)/duration_signal) *60
    return bpm