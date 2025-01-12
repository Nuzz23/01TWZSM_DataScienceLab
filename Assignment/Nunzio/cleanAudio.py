import noisereduce as nr
import torchaudio
from scipy.io import wavfile

audio_clip, sample_rate = torchaudio.load("Assignment/data/audios_development/2931.wav")
wavfile.write("1.wav", sample_rate, nr.reduce_noise(y=audio_clip, sr=sample_rate, stationary=False)[0])