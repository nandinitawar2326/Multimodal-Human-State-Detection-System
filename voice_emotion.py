import librosa
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

SAMPLE_RATE = 22050
DURATION = 4

def record_voice(filename="test.wav"):
    audio = sd.rec(int(DURATION * SAMPLE_RATE),
                    samplerate=SAMPLE_RATE,
                    channels=1,
                    dtype='float32')
    sd.wait()
    write(filename, SAMPLE_RATE, audio)

def predict_voice_emotion():
    record_voice("test.wav")

    y, sr = librosa.load("test.wav", sr=SAMPLE_RATE)

    energy = np.mean(y ** 2)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc0 = np.mean(mfcc[0])
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))

    if energy < 0.005:
        return "calm"
    elif energy < 0.01:
        return "sad"
    elif energy > 0.02 and zcr > 0.12:
        return "angry"
    else:
        return "happy"
