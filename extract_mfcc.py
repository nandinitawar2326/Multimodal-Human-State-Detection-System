import librosa
import numpy as np

audio_path = "test.wav"

y, sr = librosa.load(audio_path, sr=22050)

mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
mfcc_mean = np.mean(mfcc.T, axis=0)

print("MFCC shape:", mfcc.shape)
print("Feature vector:", mfcc_mean)
