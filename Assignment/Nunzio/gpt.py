import numpy as np
import os
import torch
from scipy.signal import spectrogram
import parselmouth  # for pitch extraction
import torchaudio
import pandas as pd

def extract_f0(audio_path):
    # Use Parselmouth (Praat) to extract pitch (F0)
    snd = parselmouth.Sound(audio_path)
    pitch = snd.to_pitch()
    f0_values = pitch.selected_array['frequency']
    # Exclude invalid values (0 Hz)
    f0_values = f0_values[f0_values > 0]
    
    f0_mean = np.mean(f0_values) if len(f0_values) > 0 else 0
    f0_std = np.std(f0_values) if len(f0_values) > 0 else 0
    f0_min = np.min(f0_values) if len(f0_values) > 0 else 0
    f0_max = np.max(f0_values) if len(f0_values) > 0 else 0
    return f0_mean, f0_std, f0_min, f0_max

def extract_spectral_features(audio_tensor, sr):
    # MFCC (13 Coefficients)
    mfcc_transform = torchaudio.transforms.MFCC(sample_rate=sr, n_mfcc=13)
    mfcc = mfcc_transform(audio_tensor)
    mfcc_mean = torch.mean(mfcc, dim=-1).numpy()

    # Spectrogram
    f, t, Sxx = spectrogram(audio_tensor.numpy(), fs=sr)
    
    # Spectral Centroid
    spectral_centroid = np.sum(f * np.sum(Sxx, axis=1)) / np.sum(Sxx) if np.sum(Sxx) > 0 else 0

    # Spectral Bandwidth
    spectral_bandwidth = np.sqrt(np.sum(((f - spectral_centroid) ** 2) * np.sum(Sxx, axis=1)) / np.sum(Sxx)) if np.sum(Sxx) > 0 else 0

    # Spectral Rolloff (85%)
    cumulative_energy = np.cumsum(np.sum(Sxx, axis=1))
    spectral_rolloff = f[np.where(cumulative_energy >= 0.85 * cumulative_energy[-1])[0][0]] if len(cumulative_energy) > 0 else 0

    return mfcc_mean, spectral_centroid, spectral_bandwidth, spectral_rolloff

def extract_temporal_features(audio_path):
    # Load the audio file
    audio, sr = torchaudio.load(audio_path)
    audio = audio[0].numpy()
    
    # Duration
    duration = len(audio) / sr
    
    # RMS Energy
    rms = np.sqrt(np.mean(audio ** 2))
    
    return duration, rms

def extract_prosodic_features(audio):
    energy = np.square(audio)
    mean_energy = np.mean(energy)
    std_energy = np.std(energy)
    return mean_energy, std_energy

def extract_jitter_shimmer_hnr(audio_path):
    # Placeholder function for jitter, shimmer, HNR (requires Praat or Parselmouth)
    jitter = 0  # Placeholder
    shimmer = 0  # Placeholder
    hnr = 0  # Placeholder
    return jitter, shimmer, hnr

def process_audio_file(audio_path):
    # Load the audio as tensor with torchaudio
    waveform, sr = torchaudio.load(audio_path)
    if waveform.shape[0] > 1:  # Stereo to Mono
        waveform = torch.mean(waveform, dim=0, keepdim=True)
    
    # Extract all features
    f0_features = extract_f0(audio_path)  # F0 extracted using Parselmouth
    spectral_features = extract_spectral_features(waveform[0], sr)
    temporal_features = extract_temporal_features(audio_path)
    prosodic_features = extract_prosodic_features(waveform[0].numpy())
    jitter_shimmer_hnr = extract_jitter_shimmer_hnr(audio_path)
    
    # Combine all features into a single array
    return np.hstack([
        f0_features,
        spectral_features,
        temporal_features,
        prosodic_features,
        jitter_shimmer_hnr
    ])

# Apply the pipeline on a directory
features = []
for file in pd.read_csv('Assignment/Nunzio/NonAfrica.csv', header=0, index_col=0)['path']:
    if file.endswith(".wav"):
        file_path = os.path.join('Assignment/data/audios_development/', file)
        features.append(process_audio_file(file_path))

# Convert the features list to a DataFrame
df_features = pd.DataFrame(features, columns=[
    'f0_mean', 'f0_std', 'f0_min', 'f0_max', 
    'mfcc1', 'mfcc2', 'mfcc3', 'mfcc4', 'mfcc5', 'mfcc6', 'mfcc7', 'mfcc8', 'mfcc9', 'mfcc10', 'mfcc11', 'mfcc12', 'mfcc13', 
    'spectral_centroid', 'spectral_bandwidth', 'spectral_rolloff', 
    'duration', 'rms', 
    'mean_energy', 'std_energy', 
    'jitter', 'shimmer', 'hnr'
])

# Save the DataFrame to a CSV or other desired format
df_features.to_csv('output_features.csv', index=False)
