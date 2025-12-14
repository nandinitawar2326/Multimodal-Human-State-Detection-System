import sounddevice as sd
import soundfile as sf

duration = 5  # seconds
samplerate = 22050

print("Recording...")
audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
sd.wait()
print("Recording finished")

sf.write("test.wav", audio, samplerate)
print("Saved as test.wav")

